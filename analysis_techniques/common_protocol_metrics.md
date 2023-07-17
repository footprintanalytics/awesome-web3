---
title:  "Training of GPT model-Protocol Data"

---

# Data Overview 

### Data Relationship

```mermaid
erDiagram
    protocol_info {
      varchar chain pk
      varchar protocol_slug pk
      varchar protocol_name
      varchar protocol_type
      varchar protocol_sub_type
      varchar logo
    }
    
    contract_info {
      varchar chain pk
      varchar contract_address pk
      varchar contract_name
      varchar protocol_slug
      varchar standard
      varchar deployer_address
      timestamp deploy_block_timestamp
      integer deploy_block_number
    }
    
    protocol_address_retention_monthly {
 varchar cohort
 varchar protocol_slug
 varchar "chain"
 varchar protocol_name
 integer number_of_new_users
 double month_1
 double month_2
 double month_3
 double month_4
 double month_5
 double month_6
 double month_7
 double month_8
 double month_9
 double month_10
 double month_11
 double month_12
 date start_date
 date end_date
    }

protocol_daily_stats {
 date on_date
 varchar "chain"
 varchar protocol_slug
 varchar protocol_name
 integer number_of_active_users
 integer number_of_new_users
 integer number_of_total_users
 double new_users_1d_pct_change
 double new_users_7d_pct_change
 double new_users_30d_pct_change
 double new_users_180d_pct_change
 double new_users_360d_pct_change
 double active_users_1d_pct_change
 double active_users_7d_pct_change
 double active_users_30d_pct_change
 double active_users_180d_pct_change
 double active_users_360d_pct_change
 double volume
 double number_of_transactions
    }

    token_daily_stats {
 date on_date
 varchar token_slug
 varchar protocol_slug
 varchar token_symbol
 varchar token_name
 double price
 double circulating_supply
 double fully_diluted_valuation
 double market_cap
 double max_supply
 double total_supply
 double trading_vol_24h
    }
ud_defi_fundraising_stats {
varchar id
 varchar fundraising_rounds
 timestamp "day"
 double amount
 varchar investor
 varchar protocol_slug
 varchar project_slug
 varchar project
 varchar website
 varchar founder
 varchar category
 varchar sub_category
 varchar description
 double valuation
 varchar announcement
 varchar "unique"
 varchar round
 timestamp updated_at
 timestamp created_at
}
    protocol_info ||--|{ contract_info : contains
		contract_info ||--|{ protocol_address_retention_monthly : contains
	

```

# analysis techniques for specific protocol
##  This section is the content of the protocol data indicators. The following examples include tvl including the protocol, active users, new users and user retention, financing status, and token status
### Query the tvl ranking of each protocol on the chain 
  ``` sql
  select 
  logo
  ,ds.protocol_slug
  ,tvl as TVL
  ,(tvl - D1_tvl)/D1_tvl as D1_change_Rate
  ,(tvl - D7_tvl)/D1_tvl as D7_change_Rate
  ,(tvl - D30_tvl)/D1_tvl as D30_change_Rate
  ,row_number() over (partition by chain order by tvl desc) ranking
  from
  (
  select
      chain,
      protocol_slug,
      tvl,
      D1_tvl,
      D7_tvl,
      D30_tvl
  from 
      (select 
      on_date,
      chain,
      protocol_slug,
      tvl,
      lag(tvl,1)  over (partition by protocol_slug order by on_date) as D1_tvl,
      lag(tvl,7)  over (partition by protocol_slug order by on_date) as D7_tvl,
      lag(tvl,30)  over (partition by protocol_slug order by on_date) as D30_tvl
      from 
      "defi_protocol_daily_stats" 
          where 1=1 
          [[and {{chain}} ]]
      )t1
      where  on_date = (select max(on_date) from "defi_protocol_daily_stats" where date(on_date) != current_date )
  )ds
  left join
      (
      select max(logo) as logo,protocol_slug from "protocol_info" where protocol_type='DeFi' group by protocol_slug 
      )pi 
  on ds.protocol_slug = pi.protocol_slug
  order by ranking
```

### Query the daily number of new and active users of the planet-ix platform on the polygon chain
``` sql
 select
      on_date
      ,number_of_new_users
      ,number_of_active_users
  from protocol_daily_stats
  where protocl_slug = 'planet-ix'
  and chain ='Polygon
```

### Query the monthly user retention rate of the planet-ix platform on the polygon chain
``` sql
select
*
from
protocol_address_retention_monthly
where chain ='Polygon'
and protocol_slug = 'planet-ix' 
```

### Query the IXT token currency price and market value, transaction volume and circulation of the planet-ix platform, etc.
``` sql
  select
      token_symbol
      ,token_slug
      ,price
      ,trading_vol_24h
      ,market_cap
      ,circulating_supply
      ,max_supply
      ,total_supply
      ,on_date as last_update_at
from
    token_daily_stats
where protocol_slug = 'planet-ix'
    and on_date = ( select max(on_date) from token_daily_stats where on_date >= date_add('day',-3,current_date))
```

### Query the amount and frequency of Animoca Brands platform financing
``` sql
with nfts as (
    SELECT
        day
        ,project
        ,amount
        ,fundraising_rounds 
      FROM "ud_defi_fundraising_stats"
    where 1=1
    and sub_category ='Gaming'
    [[and {{day}}]]
    and project ='Animoca Brands'
    group by day,project,amount,fundraising_rounds
)
select 
  date_trunc('month',day) as month,project,
  sum(amount) as "Financing amoun",count(1) as nums 
from nfts
group by 1,2
order by 3 desc
```
