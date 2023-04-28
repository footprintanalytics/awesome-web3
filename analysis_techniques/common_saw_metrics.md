## analysis techniques for common saw metrics
### here's a tutorial on how to track daily deposits, withdrawals, and remaining locked funds in a PancakeSwap pool, using the `bsc_token_transfers` table to record all transfer information. We will assume that the pool address is `0x45c54210128a065de780C4B0Df3d16664f7f859e`.

#### Tracking Daily Deposits and Withdrawals

1. Use an SQL query to find all transfers to the pool address from the past 24 hours:

   ```
   SELECT SUM(value)
   FROM bsc_token_transfers
   WHERE to_address = '0x45c54210128a065de780C4B0Df3d16664f7f859e' AND block_timeatmp >= NOW() - INTERVAL 1 DAY
   ```

   This query will return the sum of all transfers to the PancakeSwap pool address `0x45c54210128a065de780C4B0Df3d16664f7f859e` from the past 24 hours.

2. Use another SQL query to find all transfers from the pool address to external addresses from the same period:

   ```
   SELECT SUM(value)
   FROM bsc_token_transfers
   WHERE from_address = '0x45c54210128a065de780C4B0Df3d16664f7f859e' AND block_timeatmp >= NOW() - INTERVAL 1 DAY
   ```

   This query will return the sum of all transfers from the PancakeSwap pool address `0x45c54210128a065de780C4B0Df3d16664f7f859e` to external addresses from the past 24 hours.

3. Subtract the result of step 2 from the result of step 1 to get the net inflow of funds to the pool for the past 24 hours.

#### Tracking Remaining Locked Funds
1. Use the following SQL query to calculate the total amount of tokens transferred in and out from the specified address in the PancakeSwap pool. Add the two results to get the total amount of tokens transferred:

   ```
   select sum(amount) as total_amount from (
        SELECT -SUM(amount_raw*power(0.1,18)) as amount FROM bsc_token_transfers WHERE from_address = '0x45c54210128a065de780C4B0Df3d16664f7f859e' 
        union all
        SELECT SUM(amount_raw*power(0.1,18))as amount FROM bsc_token_transfers WHERE to_address = '0x45c54210128a065de780C4B0Df3d16664f7f859e'
   )
   ```

2. Replace 'from_address' or 'to_address' in the above SQL query with the address you want to query.

3. Multiply the amounts in the query result with 'power(0.1,18)' to convert the token units from wei to Cake.

4. Check the 'total_amount' field in the query result. This is the total amount of tokens transferred in and out from the specified address in the PancakeSwap pool.




