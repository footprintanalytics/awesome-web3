# analysis techniques for specific chain and cross chain
### Query the transaction amount , active users gas fee of the ethereum chain in the last 24 hours
```
     select
          count(*) as transactions,
          count(distinct from_address) as users,
          sum(value*power(0.1,18)) as Transaction_Token_Amount, 
          count(*)/ count(distinct from_address) as txsuser_ratio,
           'Ethereum' as chain
        from "ethereum_transactions"
        where receipt_status=1 and  block_timestamp >= (date_add('hour', -24,NOW())) 
```
