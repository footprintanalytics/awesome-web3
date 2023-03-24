import pandas as pd
import numpy as np
import sys 
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
sys.path.append('/utils/')
from connection import get_connection
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import networkx as nx


def get_data(sql_cont):
    data = pd.read_sql(sql_cont, con = conn)
    return data

def get_nft_data(sql_cont1,sql_cont2):
    print("get_data(sql_cont1)")
    nft_tra_data = get_data(sql_cont1)
    print("get_data(sql_cont2)")
    nft_tsf_data = get_data(sql_cont2)
    col1 = ['transaction_hash','log_index','nft_token_id', 'block_number','block_date','block_timestamp','seller_address','buyer_address','amount']
    col2 = ['transaction_hash','log_index','nft_token_id','block_number','block_date','block_timestamp','from_address','to_address']
    nft_tsf_data_new = nft_tsf_data[col2]
    nft_tsf_data_new = nft_tsf_data_new.rename(columns={'from_address':'seller_address',
                                                       'to_address':'buyer_address'})



    # tra_hash = nft_tra_data['transaction_hash'].unique().tolist()
    # nft_tsf_data_new = nft_tsf_data_new[~nft_tsf_data_new['transaction_hash'].isin(tra_hash)]
    nft_tsf_data_new['amount'] = 0
    nft_tra_data_new = nft_tra_data[col1]
    nft_data = pd.concat([nft_tsf_data_new,nft_tra_data_new],ignore_index=True)
#     nft_data = nft_data.sample(frac=0.1)
    
    print("开始排序")
    nft_data['rank11'] = nft_data.groupby(['seller_address','buyer_address','nft_token_id','block_timestamp']).amount.transform(lambda x:x.rank(ascending=False))
    nft_data = nft_data[nft_data['rank11']==1]
    
    
    
    nft_data_count = nft_data.groupby(['transaction_hash']).agg({'log_index':'count'}).rename(columns={'log_index':'hash_count'}).reset_index()
    nft_data_count = nft_data_count[nft_data_count['hash_count'] == 1]
#     nft_data_count[['transaction_hash','hash_count']]


    print("排序完成")

    nft_data = nft_data.sort_values(by=['block_timestamp','block_number'])
    nft_data = nft_data.drop_duplicates()
    nft_data['rank1'] = nft_data.groupby(['nft_token_id','block_timestamp']).log_index.transform(lambda x:x.rank())
    nft_data_cp = nft_data[['nft_token_id','block_timestamp']].drop_duplicates()

    nft_data_cp['rank2'] = nft_data_cp.groupby(['nft_token_id']).block_timestamp.transform(lambda x:x.rank())
    nft_data = nft_data.merge(nft_data_cp,how='left',on=['nft_token_id','block_timestamp'])
    nft_data['rank_final'] = nft_data['rank1'] + nft_data['rank2']*0.1
    nft_data['rank3'] = nft_data.groupby(['nft_token_id']).rank_final.transform(lambda x:x.rank())
    print("rank finish")
    return nft_data,nft_data_count



def merge_gap_data(nft_data,gap_v):

    nft_data['rank_gap'] = nft_data['rank3'] + gap_v
    sv_nft_data = nft_data[save_cols_or]
    sv_nft_data_new = nft_data[save_cols]
    rename_col = {}
    for col in ['seller_address', 'buyer_address','amount','block_timestamp']:
        rename_col[col] = "%s_%s"%(col,gap_v)
    rename_col['rank_gap'] = 'rank3'
    sv_nft_data_new = sv_nft_data_new.rename(columns=rename_col)
#     sv_nft_data = sv_nft_data.merge(sv_nft_data_new,how='left',on=['nft_token_id','rank3'])
    return sv_nft_data_new





# address_list = [
# '0x4e1f41613c9084fdb9e34e11fae9412427480e56'
# # ,'0xa0bae4c0410d79398703cbd9a30d010d414ab0da'
# # ,'0x1dfe7ca09e99d10835bf73044a23b73fc20623df'
# # ,'0xa5d37c0364b9e6d96ee37e03964e7ad2b33a93f4'
# # ,'0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258'
# # ,'0xce25e60a89f200b1fa40f6c313047ffe386992c3'
# # ,'0x7bd29408f11d2bfc23c34f18275bbf23bb716bc7'
# # ,'0x81ae0be3a8044772d04f32398bac1e1b4b215aa8'
# ]

data = pd.read_csv("./tmp/austen_file/query_result_2022-09-20T04_27_50.026266Z.csv")
data = data.sort_values(by=['Sum of Volume'],ascending=False)
address_list = data['nft_collection_info → Contract Address'].tolist()[:600]

save_cols = ['nft_token_id','seller_address', 'buyer_address','amount','rank_gap','block_timestamp']
save_cols_or = ['nft_token_id','seller_address', 'buyer_address','amount','rank3','block_timestamp']
conn = get_connection()
gap_v = 2
hash_list_collect = []
nft_data_count_list = []
cycle_df = []

for index_nft,addr in enumerate(address_list):
    print("="*30)
    print("%s/%s"%(index_nft,len(address_list)))
    print(addr)
    
    print("="*30)
    sql_cont1 = f'''
    select * from `nft_transactions` where  lower(`nft_transactions`.`collection_contract_address`)=lower('{addr}')
    '''
    sql_cont2 = f'''
    select * from `nft_transfers` where lower(`nft_transfers`.`token_address`)=lower('{addr}') 
    '''
    nft_data,nft_data_count = get_nft_data(sql_cont1,sql_cont2)
    
    
    
    
    data_nft_weight = nft_data[['seller_address','buyer_address','amount']]
    data_nft_weight['weight'] = (data_nft_weight['amount'] > 0).astype(int)
    data_nft_weight['weight'] = data_nft_weight['weight'] + 1
    G = nx.MultiDiGraph()
    
    for i in range(len(data_nft_weight)):
        buy = data_nft_weight.iloc[i]['buyer_address']
        sel = data_nft_weight.iloc[i]['seller_address']
        wg = data_nft_weight.iloc[i]['weight']
        G.add_weighted_edges_from([(sel,buy,wg)])
        
    data_degree = pd.DataFrame(G.degree)
    data_degree = data_degree.rename(columns={0:'address',1:'degree'})
    zero_add = '0x0000000000000000000000000000000000000000'
    data_degree_cp = data_degree.copy()
    data_degree_cp = data_degree_cp.rename(columns={'address':'seller_address','degree':'selll_address'})
    nft_data_anom = nft_data[['transaction_hash','seller_address','buyer_address']]
    nft_data_anom = nft_data_anom.merge(data_degree_cp,how='left',on=['seller_address'])
    data_degree_cp = data_degree.copy()
    data_degree_cp = data_degree_cp.rename(columns={'address':'buyer_address','degree':'buy_address'})
    nft_data_anom = nft_data_anom.merge(data_degree_cp,how='left',on=['buyer_address'])
    nft_data_anom = nft_data_anom[nft_data_anom['seller_address'] != zero_add]
    circle_list = nx.find_cycle(G, orientation="original")
    
    
    circle_address = []
    for index,cir in enumerate(circle_list):
        for c in cir:
            if ('0x' in str(c)) & (c not in circle_address):
#                 print("添加地址")
                circle_address.append(c)
    cir_df = pd.DataFrame(circle_address)
    
    cir_df_cp = cir_df.copy()
    cir_df_cp = cir_df_cp.rename(columns={0:'seller_address'})
    cir_df_cp['sell_circle'] = 1
    nft_data_anom = nft_data_anom.merge(cir_df_cp,how='left',on=['seller_address'])
    cir_df_cp = cir_df.copy()
    cir_df_cp = cir_df_cp.rename(columns={0:'buyer_address'})
    cir_df_cp['buy_circle'] = 1
    nft_data_anom = nft_data_anom.merge(cir_df_cp,how='left',on=['buyer_address'])
    circle_th = nft_data_anom[(nft_data_anom['sell_circle'] == 1) & (nft_data_anom['buy_circle'] == 1)]
    circle_th['collection_contract_address'] = addr
#     circle_th.to_csv("%s.csv"%(addr),index=False)
    
    hash_list_collect.append(circle_th)
    cycle_df.append(circle_th)
    if (index_nft % 5 == 0) & (index_nft != 0):
        cycle_df_new = pd.concat(cycle_df,ignore_index=True)
        cycle_df_new.to_csv("/tmp/austen_file/%s_part.csv"%(index_nft))
        print("%s is fnish"%(index_nft))
        cycle_df = []

#     nft_data_merge,col_sell,col_buy,col_amount = get_nft_data_merge(nft_data)
#     nft_data_merge = process_feat(nft_data_merge)
#     nft_data_merge,zero_nft = model_predict(nft_data_merge)
#     hash_list = get_hash_list(nft_data_merge)
#     hash_list['collection_contract_address'] = addr
#     hash_list_collect.append(hash_list)
#     nft_data_count_list.append(nft_data_count)
print("code finish")
# hash_list_collect_df = pd.concat(hash_list_collect,ignore_index=True)
# hash_list_collect_df.to_csv("/tmp/austen_file/nft_anomaly_v5.csv",index=False)