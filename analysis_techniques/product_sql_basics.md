
# SQL Basics Part 1
### Footprint analytics uses the framework of iceberg + trino, so the sql syntax used needs to be based on trino sql syntax. This is the [link](https://trino.io/docs/current/functions.html) of trino sql syntax documentation
### Basic Introduction.
#### 1. What is a data lake?

A data lake is a large repository that stores an enterprise's wide variety of raw data, which is available for access, processing, analysis, and transfer. A data lake is a system or repository of data stored in its natural format, usually as an object blob or file. A data lake is typically a single store for all of an enterprise's data, including raw copies of source system data, as well as transformed data for tasks such as reporting, visualization, analysis, and machine learning. Data lakes can include structured data from relational databases (rows and columns), semi-structured data (CSV, logs, XML, JSON), unstructured data (emails, documents, PDFs) and binary data (images, audio, video)

#### 2. What is SQL ?

SQL , also known as Structured Query Language, is a database query and programming language for accessing data and querying, updating and managing relational database systems.

For example, if you want to eat pizza, durian flavor, and you are not available now, so you call an errand boy and the errand boy say: buy a pizza for me, want durian flavor, the errand boy will go to the pizza store and buy a durian flavor pizza for you and send it to your home. The most basic syntactic structure of SQL consists of three modules, and almost all SQL consists of these three parts.

 select: Which field to select?

 from: Which table to fetch data from?

 where: What are the conditions for filtering or restricting? 

#### 3. What does the data inside the data lake look like?

Take ethereum_transactions (transactions records on ethereum) as an example:

![img](https://lh4.googleusercontent.com/-wkLF87H_CyyyxOZckHT-_lencAUKKgOKZiroftSQVnn55rPvRJXx6nN-DcDaR1AcLD7G_c2fH9yCCL70nDTG1hYCzMFVRkDEEHS5P2lVvWqwvb1r3mpogidUU-PPsNfOSx1V_rEdtxKwSReby988Ww)

Here are some of the more used fields in this table

- block_timestamp : The time of the packaged transaction
- hash : The hash of this transaction stream
- block_number : The block height of the transaction
- value   : the ETH transferred out (need to divide by the ETH token's 18-decimals conversion precision, power(10,18))
- from_address : The wallet address of the outgoing ETH token
- to_address : The address of the contract to which the ETH tokens are transferred
- receipt_gas_used : The total amount of gas consumed by the executed command
- receipt_effective_gas_price : gas the price per unit of gas in the transaction (in ETH tokens)

### Common syntax and examples

####  1.Basic Structure + Operators + Order by

- Case 1:Query the wallet of Justin Sun (0x3DdfA8eC3052539b6C9549F12cEA2C295cfF5296) in January 2022 for every transfer amount greater than 1,000 ETH and the exact amount of transfers and the amount of Gas consumed per transfer.

  ``` sql
     select -- Select followed by the field to be queried, multiple fields separated by commas
      block_timestamp 
      ,from_address
      ,to_address
      ,hash
      ,value /power(10,18) as value -- convert the precision by dividing value by /power(10,18), 18 is the precision of ETH tokens
      ,(receipt_gas_used*receipt_effective_gas_price*power(0.1,18)) as gas_fee
  from ethereum_transactions -- get data from ethereum.transactions table
  where block_timestamp > date '2022-01-01' -- restrict the transfer time to be after January 1, 2022
  and from_address = lower('0x3DdfA8eC3052539b6C9549F12cEA2C295cfF5296') -- restrict Sun's wallet, here use lower() to turn the letters in the string into lowercase format (the pattern stored in the footprint database is lowercase, paste directly from the Ethernet browser may be larger mixed with lowercase)
  and value /power(10,18) >1000 -- Limit ETH Transfer to more than 1000
  order by block_timestamp -- based on block_timestamp to do ascending order, if you want to descending order need to add desc at the end, because the default is asc, so do not need to add asc at the end also line
  
  ```

  

- Footprint Query URL

[https://www.footprint.network/chart/Jastin-Sun-Transfers-%3E1000ETH-Transactions-fp-34869](https://www.footprint.network/chart/Jastin-Sun-Transfers->1000ETH-Transactions-fp-34869)

![img](https://lh6.googleusercontent.com/J0a_TdvSfpJTafA63GhQymtOtaq18kGENG_VC2bNNnwoTVw2m1RBB9K1AN4ZOAX3PoQayFc_NX4qm1OfOCHj9DjJuAS3tWhnGtfLLsX22VO6BNVhv1pmL_MCd8bWU4dUfmLmOBwGdT_HI6c2JCWRmCE)

Syntax Description :

- select 

- - select : followed by the field to be queried, with multiple fields separated by commas

- from

- - from : followed by the table of the data source

- where 

- - where :followed by the filter criteria for the data

- Operator symbols: and / or

- - If there are multiple filter conditions, you can use the operator to join them
  - and: the concatenation of multiple conditions
  - or : the intersection of multiple conditions

- order by :

- -  order by [field A] , according to the A field ascending, if you need to sort in descending order at the end of the field plus desc, because the default is ascending, so the need to ascend when you do not have to add asc at the end

- Power multiplication calculation: 

- - user conversion accuracy, the function is Power(Number, Power), where number means the bottom number, power means the index

- conversion of letters in the string case

- - lower([field]): the letters in the string are converted to lower case

  - upper([field]) :the letters in the string are converted to upper case

    

#### 2. Aggregation functions

- Case 2:The data in the table are all detailed data, if I need to summarize the data and understand the overview of the data, how do I need to do it?

``` sql
select 
    sum( value /power(10,18) ) as value -- sum the value field of the data that meets the requirements
    ,max( value /power(10,18) ) as max_value -- find the maximum value
    ,min( value /power(10,18) ) as min_value -- find the minimum value
    ,count( hash ) as tx_count -- count the data that match the requirements, count how many items
    ,count( distinct to_address ) as tx_to_address_count -- count the number of data that match the requirements (to be de-duplicated according to the destination address)
from ethereum_transactions -- get data from ethereum.transactions table
where block_timestamp > date '2022-01-01' -- restrict the transfer time to be after January 1, 2022
and from_address = lower('0x3DdfA8eC3052539b6C9549F12cEA2C295cfF5296') -- restrict Sun's wallet, here use lower() to turn the letters in the string into lowercase format (the pattern stored in the footprint database is lowercase, paste directly from the Ethernet browser may be larger mixed with lowercase)
and value /power(10,18) > 1000 -- Limit ETH Transfer to more than 1000

```

- Footprint Query URL [https://www.footprint.network/chart/Summary-of-Justin-Sun%27s-transfer-of-ETH-tokens-%3E-1000-fp-34870](https://www.footprint.network/chart/Summary-of-Justin-Sun's-transfer-of-ETH-tokens->-1000-fp-34870)

![img](https://lh6.googleusercontent.com/li4w-XNfSAfOyHK7be_N7eDTO6vnsnWdurLLdt1YVEhqACX4kXwyrmI5f81kNumqh1CkgPoxAZMX8hY8A8dTzmQKDw1fl3pnadV1231_6yMG4f7JvkAQhQHRfLZEXDodi91Kg6-1QCsD1Di1jXxZ3V4)

Syntax Description:

Aggregate function

- count(): count, count how many; if you need to re-count, add distinct in parentheses
- sum(): summation
- min(): to find the minimum value
- max(): find the maximum value
- avg(): average

#### 3. Date and time functions + group aggregation

- Case 3: Aggregated data by day

- - After processing the time field with the date_trunc function, use group by + sum to complete the group aggregation,the "--" symbol is followed by an explanation
  - ``` sql
    select -- Select followed by the field to be queried, multiple fields separated by commas
        date_trunc('day',block_timestamp) as block_date -- convert to day granularity
        ,sum(value /power(10,18)) as value -- convert precision by dividing value by /power(10,18), 18 is the precision of ETH tokens
        ,sum(receipt_gas_used*receipt_effective_gas_price*power(0.1,18)) as gas_fee
    from ethereum_transactions -- get data from ethereum.transactions table
    where block_timestamp > date '2022-01-01' -- restrict the transfer time to be after January 1, 2022
    and from_address = lower('0x3DdfA8eC3052539b6C9549F12cEA2C295cfF5296') -- restrict Sun's wallet, here use lower() to turn the letters in the string into lowercase format (the pattern stored in the footprint database is lowercase, paste directly from the Ethernet browser may be larger mixed with lowercase)
    and value /power(10,18) >1000 -- limit the amount of ETH Transfer greater than 1000
    group by 1 -- group by the first field, i.e. date_trunc('day',block_timestamp) converted field
    order by block_date -- based on block_date, do ascending order, block_date is to use 'as' to date_trunc('day',block_time) to take alias, can also write '1' that is, the first few fields of the table, if you want to descending order need to add desc at the end, because default is asc, so do not need to add asc at the end of the line
    
    ```

![img](https://lh5.googleusercontent.com/lM_lVw8IMxdvqVO33OUymlBfq8cL59wh3futGprWtEFsWJx43Sp_BMAVrAv3uWqlo0xsARiH9U-VpCgN72GN5q23-3aqOXZmg_xYiKbD1ixGZmWt3BPfICdNjUVUGR-1bnd4fS03m_x1GcJDADKoHuk)

- Footprint Query URL [https://www.footprint.network/chart/Jastin-Sun-Transfers-%3E1000ETH-Transactions-by-day-fp-34877](https://www.footprint.network/chart/Jastin-Sun-Transfers->1000ETH-Transactions-by-day-fp-34877)

Syntax Description:

- Group aggregation (group by)

- - The syntax of group aggregation is group by + grouped fields, as the name implies, is grouped first and then aggregated, and needs to be used together with the aggregation function

![img](https://lh6.googleusercontent.com/ZJkuzye6ae-6OaYirePZRP7IMUY1HMuo2XkGUCrfSSt8XR7yZ-nmxdYu-oI9gWE6SOw5wXOGwODaQZMxzS4YhE02YsDX9mBhbG6xMQ3N_5BVmMw9INZPrwo3d4bxxnvHxNfqoR7JszHEhO7ig8whJ9s)

- Suppose the table above is the sales of three sales members for the first 2 months of 2020, if you use sum, then you can only get 497000; if you want to get the two statistics on the right, then you need to use group by group aggregation group by member or month group aggregation

#### 4. Join Table

- Case 4: I want to see how much Sun converted back to USD when he transferred out ETH

  ``` sql
  select 
  block_timestamp
  ,transactions_info.block_hour as block_hour
  ,from_address
  ,to_address
  ,eth_amount
  ,hash
  ,price
  ,eth_amount*price as usd_value - the number of eth multiplied by the price of the coin
  from 
  (
      select --Select followed by the field to be queried, multiple fields separated by commas
           block_timestamp
          ,date_trunc('hour',block_timestamp) as block_hour - use date_trunc to process block_timestamp as hour, so that it can be associated as primary key
          ,from_address
          ,to_address
          ,hash
          ,value /power(10,18) as eth_amount -- convert the precision by dividing value by /power(10,18), 18 is the precision of ETH tokens
          ,(receipt_gas_used*receipt_effective_gas_price*power(0.1,18)) as gas_fee
      from ethereum_transactions -- get data from ethereum.transactions table
      where block_timestamp > date '2022-01-01' -- Restrict the transfer time to be after January 1, 2022
      and from_address = lower('0x3DdfA8eC3052539b6C9549F12cEA2C295cfF5296') -- restrict Sun's wallet, here use lower() to turn the letters in the string into lowercase format (the pattern stored in the footprint database is lowercase, paste directly from the Ethernet browser may be larger mixed with lowercase)
      and value /power(10,18) >1000 -- Limit ETH Transfer to more than 1000
      order by block_timestamp -- based on block_timestamp to do ascending order, if you want to descending order need to add desc at the end, because the default is asc, so do not need to add asc at the end also line
  ) as transactions_info
  left join 
   -- associate transactions_info with price_info data, the association method is left join
  (
       select 
          date_trunc('hour',timestamp) as block_hour -- The timestamp is processed as hour by date_trunc, so that it can be used as the primary key to correlate
          ,avg(price) as price
      from     
          "token_price_5min"
      where token_symbol = 'ETH' -- take the data of ETH tokens
      and chain = 'Ethereum' -- fetch the price data on Ether
      group by 1
   ) price_info 
   on transactions_info.block_hour = price_info.block_hour
  
  
  ```

![img](https://lh3.googleusercontent.com/5HUAbOQJkwhTsHv3z1VrCnwpfpN-dx3Wlg4tGkxTb-rtgxRXG93pf42upKvivJevJqhNIWX0_wWsd3aPwxpxtAMW-Pav_m7oOi02bleoY1g2IN5BEml2GRIFykSbIOrYAk0W7-j9H7Fb7nxds9m-E0Y)

- Footprint Query URL[https://www.footprint.network/chart/Jastin-Sun-Transfers-%3E1000ETH-Transactions-left-join-Price-fp-34884](https://www.footprint.network/chart/Jastin-Sun-Transfers->1000ETH-Transactions-left-join-Price-fp-34884)

- Join Table 

- - In most cases, the data we need is not in the same table, for example, the transactions table only contains transaction data, not token price data. If we want to calculate the USD value of the transaction, we need to use a join query to correlate the price data.

  - A join table query can be understood as a virtual table with two tables related by certain conditions, so you can easily do more processing on the virtual table.

  - A join query consists of two parts

  - - Join method (join, left join rigth join , cross join , full join)
    - Association conditions (on) multiple conditions with and joins

1. Here is the structure of the join condition

![img](https://lh4.googleusercontent.com/n1qZBJ-uw7eViI80vnzRZJHzQeJLpEGq9nA4-IcHT77UmpQZz4uzEKNC3x_7FjKxcZYy7DW1apC7xzh8upc4JCWIaAQvEiGX06GhtekeeRsVNarxXP-ISmq8PcuaLp23Zl3adg7cC95OG7F2GWYCjn4)

- The more used join method is left join, here is an example

![img](https://lh6.googleusercontent.com/nv4Tlb_FhLWo5NSKHRrRzCSPVaI_gOtXR0yROrf6PgQznDTXwf6qpQkUASMP3jj4rnj-gyY-0qfqthuaxWM9hzY7V91-ParVoEOoGYpl10PqiOBFEXi0YdanRP38DWE-yEqSYwQ2ItUDlVPb1yFW50I)

1. left join

2. - the left table is the main table, the right table according to the association conditions (on) to the left table to associate, if the association can not be filled with null
   - Table A and Table B are associated by name, because the left table is the main, so although the left table lucy and in the right table does not meet the association conditions of data, but lucy will appear in the results, the right table part because the association can not be data, so they are filled with null

#### 5. Sub-queries

- Case 5: Aggregate the detail data of case 4 by day grouping, don't want to nest too many layers of sql

  ``` sql
  with transaction_info as -- create a subquery with as and name it transaction_info
  (  
      select 
      block_timestamp
      ,transactions_info.block_hour as block_hour
      ,from_address
      ,to_address
      ,eth_amount
      ,hash
      ,price
      ,eth_amount*price as usd_value
      from 
      (
          select --Select followed by the field to be queried, multiple fields separated by commas
               block_timestamp
              ,date_trunc('hour',block_timestamp) as block_hour --The block_timestamp is processed as hour with date_trunc, which is convenient to associate as primary key
              ,from_address
              ,to_address
              ,hash
              ,value /power(10,18) as eth_amount -- convert the precision by dividing value by /power(10,18), 18 is the precision of ETH tokens
              ,(receipt_gas_used*receipt_effective_gas_price*power(0.1,18)) as gas_fee
          from ethereum_transactions -- get data from ethereum.transactions table
          where block_timestamp > date '2022-01-01' -- Restrict the transfer time to be after January 1, 2022
          and from_address = lower('0x3DdfA8eC3052539b6C9549F12cEA2C295cfF5296') -- restrict Sun's wallet, here use lower() to turn the letters in the string into lowercase format (the pattern stored in the footprint database is lowercase, paste directly from the Ethernet browser may be larger mixed with lowercase)
          and value /power(10,18) >1000 -- Limit ETH Transfer to more than 500
          order by block_timestamp -- based on block_timestamp to do ascending order, if you want to descending order need to add desc at the end, because the default is asc, so do not need to add asc at the end also line
      ) as transactions_info
      left join 
       -- associate transactions_info with price_info data, the association method is left join
      (
           select 
              date_trunc('hour',timestamp) as block_hour -- The timestamp is processed as hour by date_trunc, so that it can be used as the primary key to correlate
              ,avg(price) as price
          from     
              "token_price_5min"
          where token_symbol = 'ETH' -- take the data of ETH tokens
          and chain = 'Ethereum' -- fetch the price data on Ether
          group by 1
       ) price_info 
       on transactions_info.block_hour = price_info.block_hour
   )
   
   select 
      date_trunc('day',block_timestamp) as block_date
      ,sum(eth_amount) as eth_amount
      ,sum(usd_value) as usd_value
  from transaction_info -- fetch the required data from the 'virtual table', transactions_info, formed by the subquery
  group by 1 -- group by first field, can also use date_trunc('day',block_timestamp) for replacement
  order by 1 -- sort by the first field in ascending order, you can also use date_trunc('day',block_timestamp) or alias block_date to replace it to do ascending order
  
  ```

  

![img](https://lh5.googleusercontent.com/z_N1ItcA21Eo5XD78O3GwZQB0hVdjJa3seTi-x-A1gxNKaJHZo-UIru558Hg6oKc33CvSRmVJEEF05hbCchNedKsrEKoqoV0dNbRj4Nq1DL_AoGP5R9b3h3dPsJIqkqVTgeluHvVWf_LjlBK1GMjrUU)

- Footprint Query URL[https://www.footprint.network/chart/Jastin-Sun-Transfers-%3E1000ETH-Transactions-Daily-Value-fp-34938](https://www.footprint.network/chart/Jastin-Sun-Transfers->1000ETH-Transactions-Daily-Value-fp-34938)

Syntax Description

- Subquery ( with as )

- - With as, you can build a subquery to turn a SQL result into a 'virtual table' (a view or subquery), and the next SQL can take data directly from this 'virtual table/view'.
  - Function: with as can improve the readability of SQL logic and avoid multiple nesting
  - Syntax: with [view name] as ([SQL logic]), multiple views separated by ','

#### 6. Union-Table 

- Case 6: Calculating Sun's daily TUSD stablecoin transfers in and out in the last 90 days

  ``` sql
  with out_tusd_amount as ( -- create a subquery with as and name it out_usdc_amount
      select
          date_trunc('day',block_timestamp) as block_date
          ,sum(amount_raw*power(0.1,18)) as amount -- precision conversion of TUSD tokens
          ,'out_amount' as transfer_type -- add a new column and name it transfer_type, the value is out_amount
      from ethereum_token_transfers 
      where 
      block_timestamp >= date_add('day',-90,current_date) -- Get the last 90 days of data
      and token_address = lower('0x0000000000085d4780B73119b644AE5ecd22b376') -- Filter the data of the address of the TUSD tokens, Decimals of TUSD : 18,
      and from_address = lower('0x3DdfA8eC3052539b6C9549F12cEA2C295cfF5296') -- filter the amount transferred from justin sun's address 
      group by 1 
  )
  ,in_tusd_amount as ( -- create a subquery and name it in_TUSD_amount
     select
          date_trunc('day',block_timestamp) as block_date
          ,sum(amount_raw*power(0.1,18)) as amount -- the precision conversion of TUSD tokens
          ,'in_amount' as transfer_type -- add a new column and name it transfer_type, the value is in_amount
  
      from ethereum_token_transfers 
      where 
      block_timestamp >= date_add('day',-90,current_date) -- filter the last 90 days of data
      and token_address = lower('0x0000000000085d4780B73119b644AE5ecd22b376') -- filter the data for the address of the TUSD token, USDC Decimals : 18,
      and to_address = lower('0x3DdfA8eC3052539b6C9549F12cEA2C295cfF5296') -- filter the amount transferred from justin sun's address 
      group by 1 
  )
  select 
  block_date
  ,transfer_type
  ,sum(amount) as amount
  from (
      select * from out_tusd_amount
      union all 
      select * from in_tusd_amount
      ) as un
  group by 1,2 -- group by the first and second fields, i.e. block_date and transfer_type
  order by 1
  
  ```


![img](https://lh6.googleusercontent.com/TUd-18rJn9_48dvgATq5e2T7fj0Blc7WSqOtlM_sEgllLgAN6d331x_ByZeilm1ZWebC4TsA2A09iyQUTet6Md6L-6y7lBFg1UkzTtGZcMtUOytJ0cEoJTDqyzhDLC-HaT4wSCSFSijSQACdHqGIz-c)

- Footprint Query URL[https://www.footprint.network/chart/Justin-Sun%27s-TUSD-Token-in-and-out-amount-fp-34948](https://www.footprint.network/chart/Justin-Sun's-TUSD-Token-in-and-out-amount-fp-34948)

Syntax Description

- Merge tables (union, union all)

- - The UNION operator selects different values. If duplicate values are allowed, use UNION ALL.

- Usage: The UNION operator is used to combine the result sets of two or more SELECT statements

- Note : SELECT statements within UNION must have the same number of columns. The columns must also have similar data types. Also, the order of the columns in each SELECT statement must be the same.

- Syntax

```sql
SELECT column_name(s) FROM table_name1
UNION ALL*
SELECT column_name(s) FROM table_name2
```