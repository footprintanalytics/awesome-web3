# User rights
### Users in Footprint Analytics can copy other people's charts and dashboards. Dashboards and charts have a caching mechanism, and the dashboard can only be refreshed by themselves. Of course, if other people open a dashboard that is not their own, the chart under the dashboard is referenced. If there is data update in the table, the underlying refresh mechanism will trigger to obtain the latest data of this chart. After the refresh is completed, the original link needs to be refreshed to see the refreshed data

# Data delay module
### The data delay of all gold-level tables is one day, the data delay of nft_sliver level is 3 hours, the data delay of protocol model is one day, and the rozen-level data delays are mostly 5 minutes
 - What is the data delay of table nft_collection_daily_stats
    - Because this is the data of the gold level table, so its data delay is one day
 - What is the data latency of ethereum_transactions table 
    - Because this table is a silver-level table, the data delay is within 5 minutes
 - What is the data latency of the nft_transactions table
    - Because this table is a silver-level table, the data delay is within 3 hours
 - Why the chart or dashboard data is not updated to the latest
    - The first possibility is that the cache has not been refreshed. The cache refresh mechanism is that when the bottom table data in the opened chart or dashboard is updated, the corresponding chart will request to obtain the latest data. If the bottom layer is executed, just refresh the link to see it. The latest data is available. Of course, if you are the owner of the dashboard, you can directly click the refresh cache button in the upper right corner to refresh the data


### The following are the event flow steps for submitting a contract in footprint analytics and parsing the contract,when there are events related to submitting contracts and parsing contracts, you can use the following steps to reply
1. Click Create in the upper right corner
2. Click Submit Contract link: [sumbit contract](https://www.footprint.network/submit/contract)
3. Click Add Contract, then fill in the corresponding data, and submit
4. After completing the above three steps, wait for personnel review. After the review is passed, data will appear in the corresponding comm_{chain}_decoded_events table the next day
5. If the ABI of the contract data you want to parse is through a proxy, then you need to use this page to submit the contract link: [submit abi](https://www.footprint.network/submit/contract/add-v1)

