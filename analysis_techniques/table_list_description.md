### The following table data records the field, level, and description of each table.For example, the domain of the table named token_daily_stats is token, the level is gold level, and the description of the table is This table can be used to analyze the daily indicators (include price, trade volume in 24 hour, current market capitalization, etc.
| table_name                             | domain            | level  | description                                                  |
| -------------------------------------- | ----------------- | ------ | ------------------------------------------------------------ |
| token_daily_stats                      | token             | gold   | This table can be used to  analyze the daily indicators (include price,trade volume in 24 hour,current market capitalization,etc ) of the token. |
| token_info                             | token             | silver | This table contains the basic information of the token, which can be used to identify the token using the token_address. |
| protocol_address_retention_weekly      | protocol          | gold   | This table can be used to analyze metrics related to the number of users for different protocols. |
| protocol_active_address                | protocol          | gold   | This table records the protocol active address data.         |
| protocol_transactions                  | protocol          | silver | This table displays the transactions recorded by Footprint for the GameFi protocols. The table contains transactions that are not include method approve, transfer, and transferFrom |
| protocol_daily_stats                   | protocol          | gold   | This table can be used to analyze metrics related to the number of users for different GameFi protocols. |
| protocol_address_retention_monthly     | protocol          | gold   | This table can be used to analyze metrics related to the number of users for different protocols. |
| protocol_info                          | protocol          | silver | This table shows information of protocol.                    |
| contract_info                          | protocol          | silver | This table shows information for contract                    |
| gamefi_contract_info                   | protocol          | silver | This table shows information for contract                    |
| gamefi_protocol_info                   | protocol          | silver | This table shows information of gamefi protocol.             |
| protocol_token_transfers               | protocol          | silver | This table displays the contracts and tokens corresponding to GameFi protocols collected by Footprint. It filters transfer records in chain_token_transfer that interact with the contracts. |
| nft_collection_latest_floor_price      | nft               | gold   | This table is collection of the latest data statistics       |
| nft_transactions                   | nft               | silver | This table contains the information of the NFT sales transactions traded only on marketplaces included in FP (90% marketplace has included). It includes: ERC1155 , ERC721 included in the nft_contract_info table, some ERC20. |
| nft_collection_latest_stats            | nft               | gold   | This table is collection of the latest data statistics       |
| nft_mint_transactions                  | nft               | silver |                                                              |
| nft_collection_transfers_daily_stats   | nft               | gold   | This table is based on nft_transfers aggregating the rows by day. Table includes: collection dimension of holders , transactions, mint and burn as of each day. |
| nft_aggregator_info                    | nft               | silver | This table shows the nft aggregator static data, which includes the aggregators like gem, genie, blur in Ethereum. Use this table for JOINing aggregator_slug. |
| nft_latest_stats_dev                   | nft               | gold   | This table shows trading statistics of nft collections       |
| transaction_entity_tag                 | nft               | silver | This table shows tags for nft transactions.                  |
| nft_transfers                          | nft               | silver | This table contains the token transfers event information of ERC1155, ERC721 included in the nft_contract_info table and some ERC20 NFTs (including Ethereum, Solana, BNB Chain, Polygon,etc.). Mainly includes the flow direction of the token, and covers mint, burn, and transfer transactions. |
| nft_token_attributes                   | nft               | sliver | This table shows the traits of top collections, containing 56K+ collection contracts. The table allows to analyze the rarity of NFT by the percentage of attribute_value in attribute_key, which can be associated with nft_info by combining collection_contract_address and nft_token_id. |
| nft_info                               | nft               | silver | This table shows information about each nft item of top collections, containing 40M+ items of 19K+ collection contracts. Table includes metadata and mint information. Tip. Use contract_address and nft_token_id to join other tables. |
| nft_collection_info                    | nft               | silver | This table contains information for each indexed NFT collection. It includes 130K+ collections from multiple chains. Tip: Use collection_slug column to quickly identify the collection. |
| marketplace_nft_collection_daily_stats | nft               | gold   | This table shows statistics of nft collections in top marketplaces. It contains daily summary, data after filtering suspecious wash trade by marketplace, including price, volume, fee, royalty, number of traders. |
| nft_collection_daily_stats             | nft               | gold   | This table shows notable statistics of NFT collections (including top 6000+ collections in Ethereum, Solana and BNB Chain). The table contains daily summary data after filtering suspicious wash trades grouped by collection. Metrics include price, volume, fee, market cap, etc. |
| nft_transactions                       | nft               | silver | This table contains the information of the NFT sales transactions traded only on marketplaces included in FP (90% marketplace has included). It includes: ERC1155 , ERC721 included in the nft_contract_info table, some ERC20. |
| address_tag                            | label             | sliver | This table shows tags of the transparent addresses.          |
| entity_tag                             | label             | silver | This table shows tag for entity.                             |
| gamefi_protocol_daily_stats            | gamefi            | gold   | This table can be used to analyze the daily indicators (e.g. transaction volume, transaction number, transaction user number) of the GameFi. |
| token_price_5min                       | export_chain_data | silver |                                                              |
| token_transfers                        | export_chain_data | bronze |                                                              |
| dfk_token_transfers                    | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| harmony_token_transfers                | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| moonriver_token_transfers              | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| thunder_core_token_transfers           | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| heco_token_transfers                   | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| polygon_logs                           | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| optimism_logs                          | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| iotex_logs                             | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| ethereum_logs                          | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| fantom_logs                            | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| bsc_logs                               | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| arbitrum_logs                          | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| iotex_transaction_logs                 | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| dfk_logs                               | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| moonbeam_logs                          | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| moonriver_logs                         | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| boba_logs                              | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| avalanche_logs                         | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| celo_logs                              | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| thunder_core_logs                      | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| heco_logs                              | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| harmony_logs                           | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| eos_transactions                       | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| heco_transactions                      | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| moonbeam_token_transfers               | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| bsc_token_transfers                    | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| arbitrum_token_transfers               | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| fantom_token_transfers                 | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| eos_token_transfers                    | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| celo_token_transfers                   | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| iotex_actions                          | chain_data        | bronze | This table contains a set of all actions.                    |
| optimism_token_transfers               | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| polygon_transactions                   | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| moonriver_transactions                 | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| bsc_transactions                       | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| thunder_core_transactions              | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| avalanche_transactions                 | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| celo_transactions                      | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| oasys_token_transfers                  | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| oasys_transactions                     | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| oasys_logs                             | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| ethereum_blocks                        | chain_data        | bronze | This table contains a set of all blocks in the blockchain and their attributes. |
| ethereum_traces                        | chain_data        | bronze | This table contains a set of all traces in blocks, Represents the function call path that can track the transaction, More detail https://openethereum.github.io/JSONRPC-trace-module. User can use traces table to calc Ethereum Total Supply, Ethereum Reward and Ethereum Transfers,get the Parameters and Outputs of contract function calls. |
| bitcoin_transactions                   | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| doge_transactions                      | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| wax_transactions                       | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| bsc_blocks                             | chain_data        | bronze | This table contains a set of all blocks in the blockchain and their attributes. |
| boba_transactions                      | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| ethereum_decoded_events                | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| harmony_transactions                   | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| dfk_transactions                       | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| iotex_transactions                     | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| ethereum_transactions                  | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| fantom_transactions                    | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| moonbeam_transactions                  | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| fantom_blocks                          | chain_data        | bronze | This table contains a set of all blocks in the blockchain and their attributes. |
| boba_token_transfers                   | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| wax_actions                            | chain_data        | bronze | This table contains a set of all actions.                    |
| eos_actions                            | chain_data        | bronze | This table contains a set of all actions.                    |
| polygon_token_transfers                | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| solana_token_transfers                 | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| ethereum_token_transfers               | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| optimism_community_decoded_events      | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| arbitrum_community_decoded_events      | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| bsc_community_decoded_events           | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| polygon_community_decoded_events       | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| avalanche_community_decoded_events     | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| ethereum_community_decoded_events      | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| optimism_decoded_events                | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| arbitrum_decoded_events                | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| polygon_decoded_events                 | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| bsc_decoded_events                     | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| avalanche_decoded_events               | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| comm_optimism_decoded_events           | chain_data        | silver | This table holds the data parsed from the logs table into readable event (contract address provided by the community). |
| comm_arbitrum_decoded_events           | chain_data        | silver | This table holds the data parsed from the logs table into readable event (contract address provided by the community). |
| comm_polygon_decoded_events            | chain_data        | silver | This table holds the data parsed from the logs table into readable event (contract address provided by the community). |
| comm_bsc_decoded_events                | chain_data        | silver | This table holds the data parsed from the logs table into readable event (contract address provided by the community). |
| comm_avalanche_decoded_events          | chain_data        | silver | This table holds the data parsed from the logs table into readable event (contract address provided by the community). |
| comm_ethereum_decoded_events           | chain_data        | silver | This table holds the data parsed from the logs table into readable event (contract address provided by the community). |
| polygon_blocks                         | chain_data        | bronze | This table contains a set of all blocks in the blockchain and their attributes. |
| arbitrum_blocks                        | chain_data        | bronze | This table contains a set of all blocks in the blockchain and their attributes. |
| optimism_blocks                        | chain_data        | bronze | This table contains a set of all blocks in the blockchain and their attributes. |
| ronin_blocks                           | chain_data        | bronze | This table contains a set of all blocks in the blockchain and their attributes. |
| ronin_logs                             | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| bitcoin_transaction_inputs             | chain_data        | bronze | This table contains bitcoin inputs transactions.             |
| bitcoin_transaction_outputs            | chain_data        | bronze | This table contains bitcoin outputs transactions.            |
| arbitrum_transactions                  | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| hive_transactions                      | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| optimism_transactions                  | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| solana_transactions                    | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| comm_harmony_decoded_events            | chain_data        | silver | This table holds the data parsed from the logs table into readable event (contract address provided by the community). |
| harmony_decoded_events                 | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| cronos_decoded_events                  | chain_data        | silver | This table holds the data parsed from the logs table into readable event. |
| polygon_contract                       | chain_data        | silver |                                                              |
| bnb_chain_contract                     | chain_data        | silver |                                                              |
| ethereum_contract                      | chain_data        | silver |                                                              |
| mch_verse_blocks                       | chain_data        | bronze | This table contains a set of all blocks in the blockchain and their attributes. |
| mch_verse_token_transfers              | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| mch_verse_transactions                 | chain_data        | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| mch_verse_logs                         | chain_data        | bronze | This table is generally useful for reporting on any logged event type on the blockchain. |
| optimism_contract                      | chain_data        | silver |                                                              |
| arbitrum_contract                      | chain_data        | silver |                                                              |
| avalanche_token_transfers              | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
| portfolio_token_latest_stats           | address           | gold   | This table shows the difference and rate of change between the current latest balance and the balance at different times by token address |
| portfolio_latest_stats                 | address           | gold   | This table shows the difference and rate of change between the current latest balance and the balance at different times by portfolio |
| address_token_transfers_deprecated     | address           | silver | This table shows inflow and outflow token transfers of wallets in entity_address_info. |
| ens_latest_resolver                    | address           | silver | This table shows the latest resolver of ens.                 |
| solana_account_mapping                 | address           | silver | This table contains the mapping of token account with wallet at Solana |
| address_latest_balance                 | address           | gold   | This table shows ERC20 & ERC721 & ERC1155 token & native token balance of partial wallets. |


#### The table below is the meaning of each field in each table of footprint analytics,For example, the number_of_holders field in the nft_collection_daily_stats table, the number of holders per collection per day
|table_name|field|description|field_type|
|----------|-----|-----------|----------|
|address_latest_balance|amount|Wallet address hold amount|double|
|address_latest_balance|asset_name|Name of the asset|string|
|address_latest_balance|chain|Chain name|string|
|address_latest_balance|contract_address|The contract address|string|
|address_latest_balance|holding_time|Wallet address hold time(unit:day)|integer|
|address_latest_balance|standard|The standard of the contract|string|
|address_latest_balance|updated_at|Last update time|timestamp|
|address_latest_balance|value|Wallet address hold usd value|double|
|address_latest_balance|wallet_address|The address of wallet|string|
|address_tag|address|Address|string|
|address_tag|chain|chain|string|
|address_tag|created_at|the time when this record was created|timestamp|
|address_tag|entity_id|wallet address or contract address|STRING|
|address_tag|entity_ns_name|entity type name|string|
|address_tag|op_id|users who create tag|string|
|address_tag|source|source of the tag|string|
|address_tag|tag|Tag name|string|
|address_tag|tag_name|tag name|string|
|address_tag|updated_at|the time when this record was last modified|timestamp|
|address_token_transfers_deprecated|amount|Token amount of the last transfer|double|
|address_token_transfers_deprecated|block_number|Block number where this transaction was in|int|
|address_token_transfers_deprecated|block_timestamp|Transaction timestamp|timestamp|
|address_token_transfers_deprecated|chain|Chain name|string|
|address_token_transfers_deprecated|counterparty_address|The address of counterparty|string|
|address_token_transfers_deprecated|index|Index of the record in this transaction|string|
|address_token_transfers_deprecated|token_address|The contract_address of token|string|
|address_token_transfers_deprecated|token_symbol|Transaction token symbol name|string|
|address_token_transfers_deprecated|transaction_hash|Transaction hash|string|
|address_token_transfers_deprecated|type|Transaction transfer type, in or out|string|
|address_token_transfers_deprecated|value|The usd value of this transfer|double|
|address_token_transfers_deprecated|wallet_address|Transaction wallet address|string|
|arbitrum_blocks|base_fee_per_gas|Protocol base fee per gas, which can move up or down|integer|
|arbitrum_blocks|difficulty|Integer of the difficulty for this block|integer|
|arbitrum_blocks|extra_data|The extra data field of this block|string|
|arbitrum_blocks|gas_limit|The maximum gas allowed in this block|integer|
|arbitrum_blocks|gas_used|The total used gas by all transactions in this block|integer|
|arbitrum_blocks|hash|Hash of the block|string|
|arbitrum_blocks|logs_bloom|The bloom filter for the logs of the block|string|
|arbitrum_blocks|miner|The address of the beneficiary to whom the mining rewards were given|string|
|arbitrum_blocks|nonce|Hash of the generated proof-of-work|string|
|arbitrum_blocks|number|The block number|integer|
|arbitrum_blocks|parent_hash|Hash of the parent block|string|
|arbitrum_blocks|receipts_root|The root of the receipts trie of the block|string|
|arbitrum_blocks|sha3_uncles|SHA3 of the uncles data in the block|string|
|arbitrum_blocks|size|The size of this block in bytes|integer|
|arbitrum_blocks|state_root|The root of the final state trie of the block|string|
|arbitrum_blocks|timestamp|The unix timestamp for when the block was collated|timestamp|
|arbitrum_blocks|total_difficulty|Integer of the total difficulty of the chain until this block|integer|
|arbitrum_blocks|transaction_count|The number of transactions in the block|integer|
|arbitrum_blocks|transactions_root|The root of the transaction trie of the block|string|
|arbitrum_community_decoded_events|block_number|The block number where this event was in|integer|
|arbitrum_community_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|arbitrum_community_decoded_events|contract_address|Contract address from which this log originated|string|
|arbitrum_community_decoded_events|contract_name|The contract name of the event|string|
|arbitrum_community_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|arbitrum_community_decoded_events|event_name|The name of event|string|
|arbitrum_community_decoded_events|log_index|Integer of the event index position in the block|integer|
|arbitrum_community_decoded_events|protocol_slug|The protocol which the contract belongs, associate protocol_info for details|string|
|arbitrum_community_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|arbitrum_contract|bytecode||string|
|arbitrum_contract|contract_address||string|
|arbitrum_contract|deploy_block_number||integer|
|arbitrum_contract|deploy_block_timestamp||timestamp|
|arbitrum_contract|deploy_deployer_address||string|
|arbitrum_contract|deploy_transaction_hash||string|
|arbitrum_decoded_events|block_number|The block number where this event was in|integer|
|arbitrum_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|arbitrum_decoded_events|contract_address|Contract address from which this log originated|string|
|arbitrum_decoded_events|contract_name|The contract name of the event|string|
|arbitrum_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|arbitrum_decoded_events|event_name|The name of event|string|
|arbitrum_decoded_events|log_index|Integer of the event index position in the block|integer|
|arbitrum_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|arbitrum_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|arbitrum_logs|address|Address from which this log originated|string|
|arbitrum_logs|block_hash|Hash of the block where this log was in|string|
|arbitrum_logs|block_number|The block number where this log was in|integer|
|arbitrum_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|arbitrum_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|arbitrum_logs|log_index|Integer of the log index position in the block|integer|
|arbitrum_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|arbitrum_logs|transaction_hash|Hash of the transactions this log was created from|string|
|arbitrum_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|arbitrum_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). |integer|
|arbitrum_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|arbitrum_token_transfers|block_number|Block number where this transfer was in|integer|
|arbitrum_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|arbitrum_token_transfers|from_address|Address of the sender|string|
|arbitrum_token_transfers|log_index|Log index in the transaction receipt|integer|
|arbitrum_token_transfers|to_address|Address of the receiver|string|
|arbitrum_token_transfers|token_address|ERC20 token address|string|
|arbitrum_token_transfers|transaction_hash|Transaction hash|string|
|arbitrum_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|arbitrum_transactions|block_hash|Hash of the block where this transaction was in|string|
|arbitrum_transactions|block_number|Block number where this transaction was in|integer|
|arbitrum_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|arbitrum_transactions|from_address|Address of the sender|string|
|arbitrum_transactions|gas|Gas provided by the sender|integer|
|arbitrum_transactions|gas_price|Gas price provided by the sender |float|
|arbitrum_transactions|hash|Hash of the transaction|string|
|arbitrum_transactions|input|The data sent along with the transaction|string|
|arbitrum_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|arbitrum_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|arbitrum_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|arbitrum_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|arbitrum_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|arbitrum_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|arbitrum_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|arbitrum_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|arbitrum_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|arbitrum_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|arbitrum_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|arbitrum_transactions|transaction_type|Transaction type|integer|
|arbitrum_transactions|value|Value transferred |float|
|avalanche_community_decoded_events|block_number|The block number where this event was in|integer|
|avalanche_community_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|avalanche_community_decoded_events|contract_address|Contract address from which this log originated|string|
|avalanche_community_decoded_events|contract_name|The contract name of the event|string|
|avalanche_community_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|avalanche_community_decoded_events|event_name|The name of event|string|
|avalanche_community_decoded_events|log_index|Integer of the event index position in the block|integer|
|avalanche_community_decoded_events|protocol_slug|The protocol which the contract belongs, associate protocol_info for details|string|
|avalanche_community_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|avalanche_decoded_events|block_number|The block number where this event was in|integer|
|avalanche_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|avalanche_decoded_events|contract_address|Contract address from which this log originated|string|
|avalanche_decoded_events|contract_name|The contract name of the event|string|
|avalanche_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|avalanche_decoded_events|event_name|The name of event|string|
|avalanche_decoded_events|log_index|Integer of the event index position in the block|integer|
|avalanche_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|avalanche_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|avalanche_logs|address|Address from which this log originated|string|
|avalanche_logs|block_hash|Hash of the block where this log was in|string|
|avalanche_logs|block_number|The block number where this log was in|integer|
|avalanche_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|avalanche_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|avalanche_logs|log_index|Integer of the log index position in the block|integer|
|avalanche_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|avalanche_logs|transaction_hash|Hash of the transactions this log was created from|string|
|avalanche_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|avalanche_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|avalanche_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|avalanche_token_transfers|block_number|Block number where this transfer was in|integer|
|avalanche_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|avalanche_token_transfers|from_address|Address of the sender|string|
|avalanche_token_transfers|log_index|Log index in the transaction receipt|integer|
|avalanche_token_transfers|to_address|Address of the receiver|string|
|avalanche_token_transfers|token_address|ERC20 token address|string|
|avalanche_token_transfers|transaction_hash|Transaction hash|string|
|avalanche_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|avalanche_transactions|block_hash|Hash of the block where this transaction was in|string|
|avalanche_transactions|block_number|Block number where this transaction was in|integer|
|avalanche_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|avalanche_transactions|from_address|Address of the sender|string|
|avalanche_transactions|gas|Gas provided by the sender|integer|
|avalanche_transactions|gas_price|Gas price provided by the sender |float|
|avalanche_transactions|hash|Hash of the transaction|string|
|avalanche_transactions|input|The data sent along with the transaction|string|
|avalanche_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|avalanche_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|avalanche_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|avalanche_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|avalanche_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|avalanche_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|avalanche_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|avalanche_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|avalanche_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|avalanche_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|avalanche_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|avalanche_transactions|transaction_type|Transaction type|integer|
|avalanche_transactions|value|Value transferred |float|
|bitcoin_transaction_inputs|addresses|The address of the current flow direction |string|
|bitcoin_transaction_inputs|block_hash|The block hash of the transaction in|string|
|bitcoin_transaction_inputs|block_number|Number of the block which contains this transaction|integer|
|bitcoin_transaction_inputs|block_timestamp|Timestamp of the block which contains this transaction|timestamp|
|bitcoin_transaction_inputs|index|Sort number of the current input/output sub transaction|integer|
|bitcoin_transaction_inputs|required_signatures|The hash of required signatures|integer|
|bitcoin_transaction_inputs|script_asm|The symbolic representation of the Bitcoin's Script language op-codes|string|
|bitcoin_transaction_inputs|script_hex|The serialised form of the script in hex encoding.|string|
|bitcoin_transaction_inputs|sequence|The sequence of this transactions|integer|
|bitcoin_transaction_inputs|spent_output_index|The index of spent output transactions|integer|
|bitcoin_transaction_inputs|spent_transaction_hash|The hash of spent transaction.|string|
|bitcoin_transaction_inputs|transaction_hash|The hash of this transaction|string|
|bitcoin_transaction_inputs|type|The type of this sub transactions generate by.|string|
|bitcoin_transaction_inputs|value|The amount of current transaction.|double|
|bitcoin_transaction_outputs|addresses|The address of the current flow direction |string|
|bitcoin_transaction_outputs|block_hash|The block hash of the transaction in|string|
|bitcoin_transaction_outputs|block_number|Number of the block which contains this transaction|integer|
|bitcoin_transaction_outputs|block_timestamp|Timestamp of the block which contains this transaction|timestamp|
|bitcoin_transaction_outputs|index|Sort number of the current input/output sub transaction|integer|
|bitcoin_transaction_outputs|required_signatures|The hash of required signatures||
|bitcoin_transaction_outputs|script_asm|The symbolic representation of the Bitcoin's Script language op-codes|string|
|bitcoin_transaction_outputs|script_hex|The serialised form of the script in hex encoding.|string|
|bitcoin_transaction_outputs|transaction_hash|The hash of this transaction|string|
|bitcoin_transaction_outputs|type|The type of this sub transactions generate by.|string|
|bitcoin_transaction_outputs|value|The amount of current transaction.|double|
|bitcoin_transactions|block_hash|Hash of the block which contains this transaction|string|
|bitcoin_transactions|block_number|Number of the block which contains this transaction|integer|
|bitcoin_transactions|block_timestamp|Timestamp of the block which contains this transaction|timestamp|
|bitcoin_transactions|block_timestamp_month|Month of the block which contains this transaction|date|
|bitcoin_transactions|fee|The fee paid by this transaction|double|
|bitcoin_transactions|hash|The hash of this transaction|string|
|bitcoin_transactions|input_count|The number of inputs in the transaction|integer|
|bitcoin_transactions|input_value|Total value of inputs in the transaction|double|
|bitcoin_transactions|inputs|Transaction inputs|structural|
|bitcoin_transactions|is_coinbase|true if this transaction is a coinbase transaction|boolean|
|bitcoin_transactions|lock_time|Earliest time that miners can include the transaction in their hashing of the Merkle root to attach it in the latest block of the blockchain|integer|
|bitcoin_transactions|output_count|The number of outputs in the transaction|integer|
|bitcoin_transactions|output_value|Total value of outputs in the transaction|double|
|bitcoin_transactions|outputs|Transaction outputs|structural|
|bitcoin_transactions|size|The size of this transaction in bytes|integer|
|bitcoin_transactions|version|Protocol version specified in block which contained this transaction|integer|
|bitcoin_transactions|virtual_size|The virtual transaction size (differs from size for witness transactions)|integer|
|blocks|base_fee_per_gas|Protocol base fee per gas, which can move up or down|integer|
|blocks|difficulty|Integer of the difficulty for this block|integer|
|blocks|extra_data|The extra data field of this block|string|
|blocks|gas_limit|The maximum gas allowed in this block|integer|
|blocks|gas_used|The total used gas by all transactions in this block|integer|
|blocks|hash|Hash of the block|string|
|blocks|logs_bloom|The bloom filter for the logs of the block|string|
|blocks|miner|The address of the beneficiary to whom the mining rewards were given|string|
|blocks|nonce|Hash of the generated proof-of-work|string|
|blocks|number|The block number|integer|
|blocks|parent_hash|Hash of the parent block|string|
|blocks|receipts_root|The root of the receipts trie of the block|string|
|blocks|sha3_uncles|SHA3 of the uncles data in the block|string|
|blocks|size|The size of this block in bytes|integer|
|blocks|state_root|The root of the final state trie of the block|string|
|blocks|timestamp|The unix timestamp for when the block was collated|timestamp|
|blocks|total_difficulty|Integer of the total difficulty of the chain until this block|integer|
|blocks|transaction_count|The number of transactions in the block|integer|
|blocks|transactions_root|The root of the transaction trie of the block|string|
|bnb_chain_contract|bytecode||string|
|bnb_chain_contract|contract_address||string|
|bnb_chain_contract|deploy_block_number||integer|
|bnb_chain_contract|deploy_block_timestamp||timestamp|
|bnb_chain_contract|deploy_deployer_address||string|
|bnb_chain_contract|deploy_transaction_hash||string|
|boba_logs|address|Address from which this log originated|string|
|boba_logs|block_hash|Hash of the block where this log was in|string|
|boba_logs|block_number|The block number where this log was in|integer|
|boba_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|boba_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|boba_logs|log_index|Integer of the log index position in the block|integer|
|boba_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|boba_logs|transaction_hash|Hash of the transactions this log was created from|string|
|boba_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|boba_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|boba_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|boba_token_transfers|block_number|Block number where this transfer was in|integer|
|boba_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|boba_token_transfers|from_address|Address of the sender|string|
|boba_token_transfers|log_index|Log index in the transaction receipt|integer|
|boba_token_transfers|to_address|Address of the receiver|string|
|boba_token_transfers|token_address|ERC20 token address|string|
|boba_token_transfers|transaction_hash|Transaction hash|string|
|boba_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|boba_transactions|block_hash|Hash of the block where this transaction was in|string|
|boba_transactions|block_number|Block number where this transaction was in|integer|
|boba_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|boba_transactions|from_address|Address of the sender|string|
|boba_transactions|gas|Gas provided by the sender|integer|
|boba_transactions|gas_price|Gas price provided by the sender |float|
|boba_transactions|hash|Hash of the transaction|string|
|boba_transactions|input|The data sent along with the transaction|string|
|boba_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|boba_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|boba_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|boba_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|boba_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|boba_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|boba_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|boba_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|boba_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|boba_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|boba_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|boba_transactions|transaction_type|Transaction type|integer|
|boba_transactions|value|Value transferred |float|
|bsc_blocks|base_fee_per_gas|Protocol base fee per gas, which can move up or down|integer|
|bsc_blocks|difficulty|Integer of the difficulty for this block|integer|
|bsc_blocks|extra_data|The extra data field of this block|string|
|bsc_blocks|gas_limit|The maximum gas allowed in this block|integer|
|bsc_blocks|gas_used|The total used gas by all transactions in this block|integer|
|bsc_blocks|hash|Hash of the block|string|
|bsc_blocks|logs_bloom|The bloom filter for the logs of the block|string|
|bsc_blocks|miner|The address of the beneficiary to whom the mining rewards were given|string|
|bsc_blocks|nonce|Hash of the generated proof-of-work|string|
|bsc_blocks|number|The block number|integer|
|bsc_blocks|parent_hash|Hash of the parent block|string|
|bsc_blocks|receipts_root|The root of the receipts trie of the block|string|
|bsc_blocks|sha3_uncles|SHA3 of the uncles data in the block|string|
|bsc_blocks|size|The size of this block in bytes|integer|
|bsc_blocks|state_root|The root of the final state trie of the block|string|
|bsc_blocks|timestamp|The unix timestamp for when the block was collated|timestamp|
|bsc_blocks|total_difficulty|Integer of the total difficulty of the chain until this block|integer|
|bsc_blocks|transaction_count|The number of transactions in the block|integer|
|bsc_blocks|transactions_root|The root of the transaction trie of the block|string|
|bsc_community_decoded_events|block_number|The block number where this event was in|integer|
|bsc_community_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|bsc_community_decoded_events|contract_address|Contract address from which this log originated|string|
|bsc_community_decoded_events|contract_name|The contract name of the event|string|
|bsc_community_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|bsc_community_decoded_events|event_name|The name of event|string|
|bsc_community_decoded_events|log_index|Integer of the event index position in the block|integer|
|bsc_community_decoded_events|protocol_slug|The protocol which the contract belongs, associate protocol_info for details|string|
|bsc_community_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|bsc_decoded_events|block_number|The block number where this event was in|integer|
|bsc_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|bsc_decoded_events|contract_address|Contract address from which this log originated|string|
|bsc_decoded_events|contract_name|The contract name of the event|string|
|bsc_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|bsc_decoded_events|event_name|The name of event|string|
|bsc_decoded_events|log_index|Integer of the event index position in the block|integer|
|bsc_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|bsc_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|bsc_logs|address|Address from which this log originated|string|
|bsc_logs|block_hash|Hash of the block where this log was in|string|
|bsc_logs|block_number|The block number where this log was in|integer|
|bsc_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|bsc_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|bsc_logs|log_index|Integer of the log index position in the block|integer|
|bsc_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|bsc_logs|transaction_hash|Hash of the transactions this log was created from|string|
|bsc_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|bsc_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|bsc_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|bsc_token_transfers|block_number|Block number where this transfer was in|integer|
|bsc_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|bsc_token_transfers|from_address|Address of the sender|string|
|bsc_token_transfers|log_index|Log index in the transaction receipt|integer|
|bsc_token_transfers|to_address|Address of the receiver|string|
|bsc_token_transfers|token_address|ERC20 token address|string|
|bsc_token_transfers|transaction_hash|Transaction hash|string|
|bsc_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|bsc_transactions|block_hash|Hash of the block where this transaction was in|string|
|bsc_transactions|block_number|Block number where this transaction was in|integer|
|bsc_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|bsc_transactions|from_address|Address of the sender|string|
|bsc_transactions|gas|Gas provided by the sender|integer|
|bsc_transactions|gas_price|Gas price provided by the sender |float|
|bsc_transactions|hash|Hash of the transaction|string|
|bsc_transactions|input|The data sent along with the transaction|string|
|bsc_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|bsc_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|bsc_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|bsc_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|bsc_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|bsc_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|bsc_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|bsc_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|bsc_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|bsc_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|bsc_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|bsc_transactions|transaction_type|Transaction type|integer|
|bsc_transactions|value|Value transferred |float|
|celo_logs|address|Address from which this log originated|string|
|celo_logs|block_hash|Hash of the block where this log was in|string|
|celo_logs|block_number|The block number where this log was in|integer|
|celo_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|celo_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|celo_logs|log_index|Integer of the log index position in the block|integer|
|celo_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|celo_logs|transaction_hash|Hash of the transactions this log was created from|string|
|celo_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|celo_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|celo_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|celo_token_transfers|block_number|Block number where this transfer was in|integer|
|celo_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|celo_token_transfers|from_address|Address of the sender|string|
|celo_token_transfers|log_index|Log index in the transaction receipt|integer|
|celo_token_transfers|to_address|Address of the receiver|string|
|celo_token_transfers|token_address|ERC20 token address|string|
|celo_token_transfers|transaction_hash|Transaction hash|string|
|celo_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|celo_transactions|block_hash|Hash of the block where this transaction was in|string|
|celo_transactions|block_number|Block number where this transaction was in|integer|
|celo_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|celo_transactions|from_address|Address of the sender|string|
|celo_transactions|gas|Gas provided by the sender|integer|
|celo_transactions|gas_price|Gas price provided by the sender |float|
|celo_transactions|hash|Hash of the transaction|string|
|celo_transactions|input|The data sent along with the transaction|string|
|celo_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|celo_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|celo_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|celo_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|celo_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|celo_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|celo_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|celo_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|celo_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|celo_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|celo_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|celo_transactions|transaction_type|Transaction type|integer|
|celo_transactions|value|Value transferred |float|
|comm_arbitrum_decoded_events|block_number|The block number where this event was in|integer|
|comm_arbitrum_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|comm_arbitrum_decoded_events|contract_address|Contract address from which this log originated|string|
|comm_arbitrum_decoded_events|contract_name|The contract name of the event|string|
|comm_arbitrum_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|comm_arbitrum_decoded_events|event_name|The name of event|string|
|comm_arbitrum_decoded_events|log_index|Integer of the event index position in the block|integer|
|comm_arbitrum_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|comm_arbitrum_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|comm_avalanche_decoded_events|block_number|The block number where this event was in|integer|
|comm_avalanche_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|comm_avalanche_decoded_events|contract_address|Contract address from which this log originated|string|
|comm_avalanche_decoded_events|contract_name|The contract name of the event|string|
|comm_avalanche_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|comm_avalanche_decoded_events|event_name|The name of event|string|
|comm_avalanche_decoded_events|log_index|Integer of the event index position in the block|integer|
|comm_avalanche_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|comm_avalanche_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|comm_bsc_decoded_events|block_number|The block number where this event was in|integer|
|comm_bsc_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|comm_bsc_decoded_events|contract_address|Contract address from which this log originated|string|
|comm_bsc_decoded_events|contract_name|The contract name of the event|string|
|comm_bsc_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|comm_bsc_decoded_events|event_name|The name of event|string|
|comm_bsc_decoded_events|log_index|Integer of the event index position in the block|integer|
|comm_bsc_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|comm_bsc_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|comm_ethereum_decoded_events|block_number|The block number where this event was in|integer|
|comm_ethereum_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|comm_ethereum_decoded_events|contract_address|Contract address from which this log originated|string|
|comm_ethereum_decoded_events|contract_name|The contract name of the event|string|
|comm_ethereum_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|comm_ethereum_decoded_events|event_name|The name of event|string|
|comm_ethereum_decoded_events|log_index|Integer of the event index position in the block|integer|
|comm_ethereum_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|comm_ethereum_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|comm_harmony_decoded_events|block_number|The block number where this event was in|integer|
|comm_harmony_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|comm_harmony_decoded_events|contract_address|Contract address from which this log originated|string|
|comm_harmony_decoded_events|contract_name|The contract name of the event|string|
|comm_harmony_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|comm_harmony_decoded_events|event_name|The name of event|string|
|comm_harmony_decoded_events|log_index|Integer of the event index position in the block|integer|
|comm_harmony_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|comm_harmony_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|comm_optimism_decoded_events|block_number|The block number where this event was in|integer|
|comm_optimism_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|comm_optimism_decoded_events|contract_address|Contract address from which this log originated|string|
|comm_optimism_decoded_events|contract_name|The contract name of the event|string|
|comm_optimism_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|comm_optimism_decoded_events|event_name|The name of event|string|
|comm_optimism_decoded_events|log_index|Integer of the event index position in the block|integer|
|comm_optimism_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|comm_optimism_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|comm_polygon_decoded_events|block_number|The block number where this event was in|integer|
|comm_polygon_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|comm_polygon_decoded_events|contract_address|Contract address from which this log originated|string|
|comm_polygon_decoded_events|contract_name|The contract name of the event|string|
|comm_polygon_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|comm_polygon_decoded_events|event_name|The name of event|string|
|comm_polygon_decoded_events|log_index|Integer of the event index position in the block|integer|
|comm_polygon_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|comm_polygon_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|contract_info|chain|the chain to which the contract belongs|string|
|contract_info|contract_address|contract address|string|
|contract_info|contract_name|The name of the contract|string|
|contract_info|created_at|The time when this record was created|timestamp|
|contract_info|created_by|Who created this record|string|
|contract_info|deploy_block_number||integer|
|contract_info|deploy_block_timestamp||timestamp|
|contract_info|deploy_deployer_address||string|
|contract_info|deploy_transaction_hash||string|
|contract_info|protocol_slug|protocol name|string|
|contract_info|updated_at|When this record was last modified|timestamp|
|contract_info|updated_by|The latest person who edited this record|string|
|cronos_decoded_events|block_number|The block number where this event was in|integer|
|cronos_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|cronos_decoded_events|contract_address|Contract address from which this log originated|string|
|cronos_decoded_events|contract_name|The contract name of the event|string|
|cronos_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|cronos_decoded_events|event_name|The name of event|string|
|cronos_decoded_events|log_index|Integer of the event index position in the block|integer|
|cronos_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|cronos_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|dfk_logs|address|Address from which this log originated|string|
|dfk_logs|block_hash|Hash of the block where this log was in|string|
|dfk_logs|block_number|The block number where this log was in|integer|
|dfk_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|dfk_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|dfk_logs|log_index|Integer of the log index position in the block|integer|
|dfk_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|dfk_logs|transaction_hash|Hash of the transactions this log was created from|string|
|dfk_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|dfk_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|dfk_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|dfk_token_transfers|block_number|Block number where this transfer was in|integer|
|dfk_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|dfk_token_transfers|from_address|Address of the sender|string|
|dfk_token_transfers|log_index|Log index in the transaction receipt|integer|
|dfk_token_transfers|to_address|Address of the receiver|string|
|dfk_token_transfers|token_address|ERC20 token address|string|
|dfk_token_transfers|transaction_hash|Transaction hash|string|
|dfk_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|dfk_transactions|block_hash|Hash of the block where this transaction was in|string|
|dfk_transactions|block_number|Block number where this transaction was in|integer|
|dfk_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|dfk_transactions|from_address|Address of the sender|string|
|dfk_transactions|gas|Gas provided by the sender|integer|
|dfk_transactions|gas_price|Gas price provided by the sender |float|
|dfk_transactions|hash|Hash of the transaction|string|
|dfk_transactions|input|The data sent along with the transaction|string|
|dfk_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|dfk_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|dfk_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|dfk_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|dfk_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|dfk_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|dfk_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|dfk_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|dfk_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|dfk_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|dfk_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|dfk_transactions|transaction_type|Transaction type|integer|
|dfk_transactions|value|Value transferred |float|
|doge_transactions|block_hash|Hash of the block which contains this transaction|string|
|doge_transactions|block_number|Number of the block which contains this transaction|integer|
|doge_transactions|block_timestamp|Timestamp of the block which contains this transaction|timestamp|
|doge_transactions|block_timestamp_month|Month of the block which contains this transaction|date|
|doge_transactions|fee|The fee paid by this transaction|double|
|doge_transactions|hash|The hash of this transaction|string|
|doge_transactions|input_count|The number of inputs in the transaction|integer|
|doge_transactions|input_value|Total value of inputs in the transaction|double|
|doge_transactions|inputs|Transaction inputs|structural|
|doge_transactions|is_coinbase|true if this transaction is a coinbase transaction|boolean|
|doge_transactions|lock_time|Earliest time that miners can include the transaction in their hashing of the Merkle root to attach it in the latest block of the blockchain|integer|
|doge_transactions|output_count|The number of outputs in the transaction|integer|
|doge_transactions|output_value|Total value of outputs in the transaction|double|
|doge_transactions|outputs|Transaction outputs|structural|
|doge_transactions|size|The size of this transaction in bytes|integer|
|doge_transactions|version|Protocol version specified in block which contained this transaction|integer|
|doge_transactions|virtual_size|The virtual transaction size (differs from size for witness transactions)|integer|
|ens_latest_resolver|domain_name|The domain name of the ens|string|
|ens_latest_resolver|ens_name|The whole name of the ens|string|
|ens_latest_resolver|last_updated_at|Tast updated time of the ens resolver|timestamp|
|ens_latest_resolver|name|The name of the ens|string|
|ens_latest_resolver|resolver_node|The node of the ens resolver|string|
|ens_latest_resolver|wallet_address|The address of the resolver|string|
|entity_tag|_id|id of data|string|
|entity_tag|created_at|create time of data|timestamp|
|entity_tag|entity_id|entity id|string|
|entity_tag|entity_ns_name|entity type name|string|
|entity_tag|op_id|users who create tag|string|
|entity_tag|tag_name|tag name|string|
|entity_tag|updated_at|update time of data|timestamp|
|eos_actions|account|Account participating in this action|string|
|eos_actions|authorization|The authorization in this action|structural|
|eos_actions|block_hash|Hash of the block|string|
|eos_actions|block_number|Block number where this action was in|integer|
|eos_actions|block_timestamp|Timestamp of the block where this action was in|timestamp|
|eos_actions|data|The data in this action|structural|
|eos_actions|hex_data| Hex of data|string|
|eos_actions|index|Index of action in the same transaction_hash|integer|
|eos_actions|name|The main actor in this action's authorization|string|
|eos_actions|transaction_hash|Hash of the transaction|string|
|eos_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|eos_token_transfers|block_number|Block number where this transfer was in|integer|
|eos_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|eos_token_transfers|from_address|Address of the sender|string|
|eos_token_transfers|log_index|Log index in the transaction receipt|integer|
|eos_token_transfers|to_address|Address of the receiver|string|
|eos_token_transfers|token_address|ERC20 token address|string|
|eos_token_transfers|transaction_hash|Transaction hash|string|
|eos_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|eos_transactions|action_count|Action Count|integer|
|eos_transactions|block_hash|Hash of the block|string|
|eos_transactions|block_number|Block number where this transaction was in|integer|
|eos_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|eos_transactions|compression|Compression|string|
|eos_transactions|context_free_data|Context free data|string|
|eos_transactions|cpu_usage_us|Cpu usages of the transaction|integer|
|eos_transactions|deferred|Deferred|bool|
|eos_transactions|delay_sec|Delay sec|integer|
|eos_transactions|expiration|Expiration|timestamp|
|eos_transactions|hash|Hash of the transaction|string|
|eos_transactions|max_cpu_usage_ms|Max cpu usage ms|integer|
|eos_transactions|max_net_usage_words|Max net usage words|integer|
|eos_transactions|net_usage_words|Net usages of the transaction|integer|
|eos_transactions|packed_context_free_data|Packed context free data|string|
|eos_transactions|packed_trx|Packed trx|string|
|eos_transactions|ref_block_num|Ref block num|string|
|eos_transactions|ref_block_prefix|Ref block prefix|string|
|eos_transactions|signatures|Signatures|string|
|eos_transactions|status|Status of the transaction|string|
|ethereum_blocks|base_fee_per_gas|Protocol base fee per gas, which can move up or down|integer|
|ethereum_blocks|difficulty|Integer of the difficulty for this block|integer|
|ethereum_blocks|extra_data|The extra data field of this block|string|
|ethereum_blocks|gas_limit|The maximum gas allowed in this block|integer|
|ethereum_blocks|gas_used|The total used gas by all transactions in this block|integer|
|ethereum_blocks|hash|Hash of the block|string|
|ethereum_blocks|logs_bloom|The bloom filter for the logs of the block|string|
|ethereum_blocks|miner|The address of the beneficiary to whom the mining rewards were given|string|
|ethereum_blocks|nonce|Hash of the generated proof-of-work|string|
|ethereum_blocks|number|The block number|integer|
|ethereum_blocks|parent_hash|Hash of the parent block|string|
|ethereum_blocks|receipts_root|The root of the receipts trie of the block|string|
|ethereum_blocks|sha3_uncles|SHA3 of the uncles data in the block|string|
|ethereum_blocks|size|The size of this block in bytes|integer|
|ethereum_blocks|state_root|The root of the final state trie of the block|string|
|ethereum_blocks|timestamp|The unix timestamp for when the block was collated|timestamp|
|ethereum_blocks|total_difficulty|Integer of the total difficulty of the chain until this block|integer|
|ethereum_blocks|transaction_count|The number of transactions in the block|integer|
|ethereum_blocks|transactions_root|The root of the transaction trie of the block|string|
|ethereum_community_decoded_events|block_number|The block number where this event was in|integer|
|ethereum_community_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|ethereum_community_decoded_events|contract_address|Contract address from which this log originated|string|
|ethereum_community_decoded_events|contract_name|The contract name of the event|string|
|ethereum_community_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|ethereum_community_decoded_events|event_name|The name of event|string|
|ethereum_community_decoded_events|log_index|Integer of the event index position in the block|integer|
|ethereum_community_decoded_events|protocol_slug|The protocol which the contract belongs, associate protocol_info for details|string|
|ethereum_community_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|ethereum_contract|bytecode||string|
|ethereum_contract|contract_address||string|
|ethereum_contract|deploy_block_number||integer|
|ethereum_contract|deploy_block_timestamp||timestamp|
|ethereum_contract|deploy_deployer_address||string|
|ethereum_contract|deploy_transaction_hash||string|
|ethereum_decoded_events|block_number|The block number where this event was in|integer|
|ethereum_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|ethereum_decoded_events|contract_address|Contract address from which this log originated|string|
|ethereum_decoded_events|contract_name|The contract name of the event|string|
|ethereum_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|ethereum_decoded_events|event_name|The name of event|string|
|ethereum_decoded_events|log_index|Integer of the event index position in the block|integer|
|ethereum_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|ethereum_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|ethereum_logs|address|Address from which this log originated|string|
|ethereum_logs|block_hash|Hash of the block where this log was in|string|
|ethereum_logs|block_number|The block number where this log was in|integer|
|ethereum_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|ethereum_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|ethereum_logs|log_index|Integer of the log index position in the block|integer|
|ethereum_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|ethereum_logs|transaction_hash|Hash of the transactions this log was created from|string|
|ethereum_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|ethereum_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|ethereum_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|ethereum_token_transfers|block_number|Block number where this transfer was in|integer|
|ethereum_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|ethereum_token_transfers|from_address|Address of the sender|string|
|ethereum_token_transfers|log_index|Log index in the transaction receipt|integer|
|ethereum_token_transfers|to_address|Address of the receiver|string|
|ethereum_token_transfers|token_address|ERC20 token address|string|
|ethereum_token_transfers|transaction_hash|Transaction hash|string|
|ethereum_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|ethereum_traces|block_hash|Hash of the block where this trace was in|string|
|ethereum_traces|block_number|Block number where this trace was in|integer|
|ethereum_traces|block_timestamp|Timestamp of the block where this trace was in|timestamp|
|ethereum_traces|call_type|One of call, callcode, delegatecall, staticcall|string|
|ethereum_traces|error|Error if message call failed. This field doesn't contain top-level trace errors.|string|
|ethereum_traces|from_address|Address of the sender, null when trace_type is genesis or reward|string|
|ethereum_traces|gas|Gas provided with the message call|integer|
|ethereum_traces|gas_used|Gas used by the message call|integer|
|ethereum_traces|input|The data sent along with the message call|string|
|ethereum_traces|output|The output of the message call, bytecode of contract when trace_type is create|string|
|ethereum_traces|reward_type|One of block, uncle|string|
|ethereum_traces|status|Either 1 (success) or 0 (failure, due to any operation that can cause the call itself or any top-level call to revert)|integer|
|ethereum_traces|subtraces|Number of subtraces|integer|
|ethereum_traces|to_address|Address of the receiver if trace_type is call, address of new contract or null if trace_type is create, beneficiary address if trace_type is suicide, miner address if trace_type is reward, shareholder address if trace_type is genesis, WithdrawDAO address if trace_type is daofork|string|
|ethereum_traces|trace_address|Comma separated list of trace address in call tree|string|
|ethereum_traces|trace_id|Unique string that identifies the trace. For transaction-scoped traces it is {trace_type}_{transaction_hash}_{trace_address}. For block-scoped traces it is {trace_type}_{block_number}_{index_within_block}|string|
|ethereum_traces|trace_type|One of call, create, suicide, reward, genesis, daofork|string|
|ethereum_traces|transaction_hash|Transaction hash where this trace was in, null if trace_type is reward|string|
|ethereum_traces|transaction_index|Integer of the transactions index position in the block|integer|
|ethereum_traces|value|Value transferred in Wei|float|
|ethereum_transactions|block_hash|Hash of the block where this transaction was in|string|
|ethereum_transactions|block_number|Block number where this transaction was in|integer|
|ethereum_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|ethereum_transactions|from_address|Address of the sender|string|
|ethereum_transactions|gas|Gas provided by the sender|integer|
|ethereum_transactions|gas_price|Gas price provided by the sender in Wei|float|
|ethereum_transactions|hash|Hash of the transaction|string|
|ethereum_transactions|input|The data sent along with the transaction|string|
|ethereum_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|ethereum_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|ethereum_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|ethereum_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|ethereum_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|ethereum_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|ethereum_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|ethereum_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|ethereum_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|ethereum_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|ethereum_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|ethereum_transactions|transaction_type|Transaction type|integer|
|ethereum_transactions|value|Value transferred in Wei|float|
|fantom_blocks|base_fee_per_gas|Protocol base fee per gas, which can move up or down|integer|
|fantom_blocks|difficulty|Integer of the difficulty for this block|integer|
|fantom_blocks|extra_data|The extra data field of this block|string|
|fantom_blocks|gas_limit|The maximum gas allowed in this block|integer|
|fantom_blocks|gas_used|The total used gas by all transactions in this block|integer|
|fantom_blocks|hash|Hash of the block|string|
|fantom_blocks|logs_bloom|The bloom filter for the logs of the block|string|
|fantom_blocks|miner|The address of the beneficiary to whom the mining rewards were given|string|
|fantom_blocks|nonce|Hash of the generated proof-of-work|string|
|fantom_blocks|number|The block number|integer|
|fantom_blocks|parent_hash|Hash of the parent block|string|
|fantom_blocks|receipts_root|The root of the receipts trie of the block|string|
|fantom_blocks|sha3_uncles|SHA3 of the uncles data in the block|string|
|fantom_blocks|size|The size of this block in bytes|integer|
|fantom_blocks|state_root|The root of the final state trie of the block|string|
|fantom_blocks|timestamp|The unix timestamp for when the block was collated|timestamp|
|fantom_blocks|total_difficulty|Integer of the total difficulty of the chain until this block|integer|
|fantom_blocks|transaction_count|The number of transactions in the block|integer|
|fantom_blocks|transactions_root|The root of the transaction trie of the block|string|
|fantom_logs|address|Address from which this log originated|string|
|fantom_logs|block_hash|Hash of the block where this log was in|string|
|fantom_logs|block_number|The block number where this log was in|integer|
|fantom_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|fantom_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|fantom_logs|log_index|Integer of the log index position in the block|integer|
|fantom_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|fantom_logs|transaction_hash|Hash of the transactions this log was created from|string|
|fantom_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|fantom_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|fantom_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|fantom_token_transfers|block_number|Block number where this transfer was in|integer|
|fantom_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|fantom_token_transfers|from_address|Address of the sender|string|
|fantom_token_transfers|log_index|Log index in the transaction receipt|integer|
|fantom_token_transfers|to_address|Address of the receiver|string|
|fantom_token_transfers|token_address|ERC20 token address|string|
|fantom_token_transfers|transaction_hash|Transaction hash|string|
|fantom_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|fantom_transactions|block_hash|Hash of the block where this transaction was in|string|
|fantom_transactions|block_number|Block number where this transaction was in|integer|
|fantom_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|fantom_transactions|from_address|Address of the sender|string|
|fantom_transactions|gas|Gas provided by the sender|integer|
|fantom_transactions|gas_price|Gas price provided by the sender |float|
|fantom_transactions|hash|Hash of the transaction|string|
|fantom_transactions|input|The data sent along with the transaction|string|
|fantom_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|fantom_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|fantom_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|fantom_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|fantom_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|fantom_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|fantom_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|fantom_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|fantom_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|fantom_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|fantom_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|fantom_transactions|transaction_type|Transaction type|integer|
|fantom_transactions|value|Value transferred |float|
|gamefi_contract_info|chain|the chain to which the contract belongs|string|
|gamefi_contract_info|collection_name|The name of nft collection|string|
|gamefi_contract_info|contract_address|contract address|string|
|gamefi_contract_info|contract_name|contract name|string|
|gamefi_contract_info|contract_type|contract type|string|
|gamefi_contract_info|nft_collection_type|The type of nft collection|string|
|gamefi_contract_info|protocol_name|The protocol name |string|
|gamefi_contract_info|protocol_slug|protocol slug|string|
|gamefi_contract_info|token_name||string|
|gamefi_contract_info|token_type|The type of token||
|gamefi_protocol_daily_stats|chain|Chain of the protocol|string|
|gamefi_protocol_daily_stats|logo|Logo link of the protocol|string|
|gamefi_protocol_daily_stats|number_of_active_users|Number of active wallet addresses interacting with dapp's smart contracts|integer|
|gamefi_protocol_daily_stats|number_of_transactions|Transactions made to dapp's smart contracts|integer|
|gamefi_protocol_daily_stats|on_date|Statistical date|date|
|gamefi_protocol_daily_stats|protocol_name|Protocol name|string|
|gamefi_protocol_daily_stats|protocol_slug|Protocol slug|string|
|gamefi_protocol_daily_stats|volume|Total amount of incoming value to dapp's smart contracts|float|
|gamefi_protocol_info|chain|The chain of the protocol|string|
|gamefi_protocol_info|genre|genre|string|
|gamefi_protocol_info|protocol_slug|The abbreviation of the protocol |string|
|harmony_decoded_events|block_number|The block number where this event was in|integer|
|harmony_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|harmony_decoded_events|contract_address|Contract address from which this log originated|string|
|harmony_decoded_events|contract_name|The contract name of the event|string|
|harmony_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|harmony_decoded_events|event_name|The name of event|string|
|harmony_decoded_events|log_index|Integer of the event index position in the block|integer|
|harmony_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|harmony_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|harmony_logs|address|Address from which this log originated|string|
|harmony_logs|block_hash|Hash of the block where this log was in|string|
|harmony_logs|block_number|The block number where this log was in|integer|
|harmony_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|harmony_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|harmony_logs|log_index|Integer of the log index position in the block|integer|
|harmony_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|harmony_logs|transaction_hash|Hash of the transactions this log was created from|string|
|harmony_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|harmony_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|harmony_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|harmony_token_transfers|block_number|Block number where this transfer was in|integer|
|harmony_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|harmony_token_transfers|from_address|Address of the sender|string|
|harmony_token_transfers|log_index|Log index in the transaction receipt|integer|
|harmony_token_transfers|to_address|Address of the receiver|string|
|harmony_token_transfers|token_address|ERC20 token address|string|
|harmony_token_transfers|transaction_hash|Transaction hash|string|
|harmony_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|harmony_transactions|block_hash|Hash of the block where this transaction was in|string|
|harmony_transactions|block_number|Block number where this transaction was in|integer|
|harmony_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|harmony_transactions|from_address|Address of the sender|string|
|harmony_transactions|gas|Gas provided by the sender|integer|
|harmony_transactions|gas_price|Gas price provided by the sender |float|
|harmony_transactions|hash|Hash of the transaction|string|
|harmony_transactions|input|The data sent along with the transaction|string|
|harmony_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|harmony_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|harmony_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|harmony_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|harmony_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|harmony_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|harmony_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|harmony_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|harmony_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|harmony_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|harmony_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|harmony_transactions|transaction_type|Transaction type|integer|
|harmony_transactions|value|Value transferred |float|
|heco_logs|address|Address from which this log originated|string|
|heco_logs|block_hash|Hash of the block where this log was in|string|
|heco_logs|block_number|The block number where this log was in|integer|
|heco_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|heco_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|heco_logs|log_index|Integer of the log index position in the block|integer|
|heco_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|heco_logs|transaction_hash|Hash of the transactions this log was created from|string|
|heco_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|heco_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). |integer|
|heco_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|heco_token_transfers|block_number|Block number where this transfer was in|integer|
|heco_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|heco_token_transfers|from_address|Address of the sender|string|
|heco_token_transfers|log_index|Log index in the transaction receipt|integer|
|heco_token_transfers|to_address|Address of the receiver|string|
|heco_token_transfers|token_address|ERC20 token address|string|
|heco_token_transfers|transaction_hash|Transaction hash|string|
|heco_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|heco_transactions|block_hash|Hash of the block where this transaction was in|string|
|heco_transactions|block_number|Block number where this transaction was in|integer|
|heco_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|heco_transactions|from_address|Address of the sender|string|
|heco_transactions|gas|Gas provided by the sender|integer|
|heco_transactions|gas_price|Gas price provided by the sender |float|
|heco_transactions|hash|Hash of the transaction|string|
|heco_transactions|input|The data sent along with the transaction|string|
|heco_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|heco_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|heco_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|heco_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|heco_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|heco_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|heco_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|heco_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|heco_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|heco_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|heco_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|heco_transactions|transaction_type|Transaction type|integer|
|heco_transactions|value|Value transferred |float|
|hive_transactions|account_witness_vote_operation|Account witness vote operation|structural|
|hive_transactions|block_hash|Hash of the block where this transaction was in|string|
|hive_transactions|block_number|Block number where this transaction was in|integer|
|hive_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|hive_transactions|claim_reward_balance_operation|Claim reward balance operation|structural|
|hive_transactions|comment_operation|Comment operation|structural|
|hive_transactions|create_claimed_account_operation|Create claimed account operation|structural|
|hive_transactions|custom_json_operation|Custom json operation|structural|
|hive_transactions|delegate_vesting_shares_operation|Delegate vesting shares operation|structural|
|hive_transactions|effective_comment_vote_operation|Effective comment vote operation|structural|
|hive_transactions|expiration|Expiration|timestamp|
|hive_transactions|extensions|Extensions|string|
|hive_transactions|operations|Operations|structural|
|hive_transactions|ref_block_num|Ref block num|integer|
|hive_transactions|ref_block_prefix|Ref block prefix|integer|
|hive_transactions|signatures|Signatures|string|
|hive_transactions|transaction_id|Integer of the transactions index position in the block|string|
|hive_transactions|transfer_operation|Transfer operation|structural|
|hive_transactions|type|Type of the transaction |string|
|hive_transactions|vote_operation|Vote operation|structural|
|iotex_actions|action_type|Action type|string|
|iotex_actions|candidate_register|Candidate register|structural|
|iotex_actions|candidate_update|Candidate update|structural|
|iotex_actions|claim_from_rewarding_fund|Claim from rewarding fund|structural|
|iotex_actions|contract_address|Contract address|string|
|iotex_actions|create_deposit|Create deposit|structural|
|iotex_actions|deposit_to_rewarding_fund|Deposit to rewarding fund|structural|
|iotex_actions|execution|Execution|structural|
|iotex_actions|gas_consumed|Gas consumed|float|
|iotex_actions|gas_limit|Gas limit|float|
|iotex_actions|gas_price|Gas price|float|
|iotex_actions|grant_reward|Grant reward|structural|
|iotex_actions|hash|Hash|string|
|iotex_actions|height|Height|integer|
|iotex_actions|nonce|Nonce|integer|
|iotex_actions|plum_challenge_exit|Plum challenge exit|structural|
|iotex_actions|plum_create_deposit|Plum create deposit|structural|
|iotex_actions|plum_finalize_exit|Plum finalize exit|structural|
|iotex_actions|plum_put_block|Plum put block|structural|
|iotex_actions|plum_response_challenge_exit|Plum response challenge exit|structural|
|iotex_actions|plum_settle_deposit|Plum settle deposit|structural|
|iotex_actions|plum_start_exit|Plum start exit|structural|
|iotex_actions|plum_transfer|Plum transfer|structural|
|iotex_actions|put_block|Put block|structural|
|iotex_actions|put_poll_result|Put poll result|structural|
|iotex_actions|sender|Sender|string|
|iotex_actions|settle_deposit|Settle deposit|structural|
|iotex_actions|stake_add_deposit|Stake add deposit|structural|
|iotex_actions|stake_change_candidate|Stake change candidate|structural|
|iotex_actions|stake_create|Stake create|structural|
|iotex_actions|stake_restake|Stake restake|structural|
|iotex_actions|stake_transfer_ownership|Stake transfer ownership|structural|
|iotex_actions|stake_unstake|Stake unstake|structural|
|iotex_actions|stake_withdraw|Stake withdraw|structural|
|iotex_actions|start_sub_chain|Start sub chain|structural|
|iotex_actions|status|Status|integer|
|iotex_actions|stop_sub_chain|Stop sub chain|structural|
|iotex_actions|terminate_plum_chain|Terminate plum chain|structural|
|iotex_actions|timestamp|Timestamp|timestamp|
|iotex_actions|transfer|Transfer|structural|
|iotex_actions|version|Version|integer|
|iotex_logs|action_hash|Action hash|string|
|iotex_logs|contract_address|Contract address|string|
|iotex_logs|data|Data|bytes|
|iotex_logs|height|Height|integer|
|iotex_logs|index|Index|integer|
|iotex_logs|timestamp|Timestamp|timestamp|
|iotex_logs|topics|Topics|bytes|
|iotex_transaction_logs|action_hash|Action hash|string|
|iotex_transaction_logs|amount|Amount|float|
|iotex_transaction_logs|height|Height|integer|
|iotex_transaction_logs|index|Index|integer|
|iotex_transaction_logs|recipient|Recipient|string|
|iotex_transaction_logs|sender|Sender|string|
|iotex_transaction_logs|timestamp|Timestamp|timestamp|
|iotex_transaction_logs|topic|Topic|string|
|iotex_transaction_logs|transaction_log_type|Transaction log type|integer|
|iotex_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|iotex_transactions|chain|Chain of the transactions|string|
|iotex_transactions|data|Data|structural|
|iotex_transactions|from_address|Address of the sender|string|
|iotex_transactions|gas|Gas provided by the sender|float|
|iotex_transactions|gas_price|Gas price provided by the sender|float|
|iotex_transactions|height|Height|integer|
|iotex_transactions|status|Status|string|
|iotex_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|iotex_transactions|transaction_hash|Transaction hash|string|
|iotex_transactions|value|Value transferred|float|
|logs|address|Address from which this log originated|string|
|logs|block_hash|Hash of the block where this log was in|string|
|logs|block_number|The block number where this log was in|integer|
|logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|logs|log_index|Integer of the log index position in the block|integer|
|logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|logs|transaction_hash|Hash of the transactions this log was created from|string|
|logs|transaction_index|Integer of the transactions index position log was created from|integer|
|marketplace_nft_collection_daily_stats|amount_currency|Value of amount denominated in this currency|string|
|marketplace_nft_collection_daily_stats|avg_price|Average price of nft collection denominated in USD|double|
|marketplace_nft_collection_daily_stats|avg_price_amount|Average price of nft collection denominated in amount_currency|double|
|marketplace_nft_collection_daily_stats|chain|Chain name|string|
|marketplace_nft_collection_daily_stats|collection_contract_address|The contract address of collection|string|
|marketplace_nft_collection_daily_stats|collection_name|The name of collection|string|
|marketplace_nft_collection_daily_stats|collection_slug|Abbreviation of the nft collection|string|
|marketplace_nft_collection_daily_stats|floor_price|Floor price of nft collection denominated in USD|double|
|marketplace_nft_collection_daily_stats|floor_price_amount|Floor price of nft collection denominated in amount_currency|double|
|marketplace_nft_collection_daily_stats|marketplace_name|The name of marketplace|string|
|marketplace_nft_collection_daily_stats|marketplace_slug|Abbreviation of the marketplace|string|
|marketplace_nft_collection_daily_stats|max_price|Max price of nft collection denominated in USD|double|
|marketplace_nft_collection_daily_stats|max_price_amount|Max price of nft denominated in amount_currency|double|
|marketplace_nft_collection_daily_stats|min_price|Min price of nft collection denominated in USD|double|
|marketplace_nft_collection_daily_stats|min_price_amount|Min price of nft collection denominated in amount_currency|double|
|marketplace_nft_collection_daily_stats|number_of_buyers|The number of buyers on the date|integer|
|marketplace_nft_collection_daily_stats|number_of_sales_transactions|The number of sales transactions on the date|integer|
|marketplace_nft_collection_daily_stats|number_of_sellers|The number of sellers on the date|integer|
|marketplace_nft_collection_daily_stats|on_date|The date of statistics|date|
|marketplace_nft_collection_daily_stats|volume|Sum up amount of trading volume denominated in USD|double|
|marketplace_nft_collection_daily_stats|volume_amount|Amount of trading volume denominated in amount_currency|double|
|mch_verse_blocks|base_fee_per_gas|Protocol base fee per gas, which can move up or down|integer|
|mch_verse_blocks|difficulty|Integer of the difficulty for this block|integer|
|mch_verse_blocks|extra_data|The extra data field of this block|string|
|mch_verse_blocks|gas_limit|The maximum gas allowed in this block|integer|
|mch_verse_blocks|gas_used|The total used gas by all transactions in this block|integer|
|mch_verse_blocks|hash|Hash of the block|string|
|mch_verse_blocks|logs_bloom|The bloom filter for the logs of the block|string|
|mch_verse_blocks|miner|The address of the beneficiary to whom the mining rewards were given|string|
|mch_verse_blocks|nonce|Hash of the generated proof-of-work|string|
|mch_verse_blocks|number|The block number|integer|
|mch_verse_blocks|parent_hash|Hash of the parent block|string|
|mch_verse_blocks|receipts_root|The root of the receipts trie of the block|string|
|mch_verse_blocks|sha3_uncles|SHA3 of the uncles data in the block|string|
|mch_verse_blocks|size|The size of this block in bytes|integer|
|mch_verse_blocks|state_root|The root of the final state trie of the block|string|
|mch_verse_blocks|timestamp|The unix timestamp for when the block was collated|timestamp|
|mch_verse_blocks|total_difficulty|Integer of the total difficulty of the chain until this block|integer|
|mch_verse_blocks|transaction_count|The number of transactions in the block|integer|
|mch_verse_blocks|transactions_root|The root of the transaction trie of the block|string|
|mch_verse_logs|address|Address from which this log originated|string|
|mch_verse_logs|block_hash|Hash of the block where this log was in|string|
|mch_verse_logs|block_number|The block number where this log was in|integer|
|mch_verse_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|mch_verse_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|mch_verse_logs|log_index|Integer of the log index position in the block|integer|
|mch_verse_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|mch_verse_logs|transaction_hash|Hash of the transactions this log was created from|string|
|mch_verse_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|mch_verse_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|mch_verse_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|mch_verse_token_transfers|block_number|Block number where this transfer was in|integer|
|mch_verse_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|mch_verse_token_transfers|from_address|Address of the sender|string|
|mch_verse_token_transfers|log_index|Log index in the transaction receipt|integer|
|mch_verse_token_transfers|to_address|Address of the receiver|string|
|mch_verse_token_transfers|token_address|ERC20 token address|string|
|mch_verse_token_transfers|transaction_hash|Transaction hash|string|
|mch_verse_transactions|block_hash|Hash of the block where this transaction was in|string|
|mch_verse_transactions|block_number|Block number where this transaction was in|integer|
|mch_verse_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|mch_verse_transactions|from_address|Address of the sender|string|
|mch_verse_transactions|gas|Gas provided by the sender|integer|
|mch_verse_transactions|gas_price|Gas price provided by the sender |float|
|mch_verse_transactions|hash|Hash of the transaction|string|
|mch_verse_transactions|input|The data sent along with the transaction|string|
|mch_verse_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|mch_verse_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|mch_verse_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|mch_verse_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|mch_verse_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|mch_verse_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|mch_verse_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|mch_verse_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|mch_verse_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|mch_verse_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|mch_verse_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|mch_verse_transactions|transaction_type|Transaction type|integer|
|mch_verse_transactions|value|Value transferred |float|
|moonbeam_logs|address|Address from which this log originated|string|
|moonbeam_logs|block_hash|Hash of the block where this log was in|string|
|moonbeam_logs|block_number|The block number where this log was in|integer|
|moonbeam_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|moonbeam_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|moonbeam_logs|log_index|Integer of the log index position in the block|integer|
|moonbeam_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|moonbeam_logs|transaction_hash|Hash of the transactions this log was created from|string|
|moonbeam_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|moonbeam_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|moonbeam_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|moonbeam_token_transfers|block_number|Block number where this transfer was in|integer|
|moonbeam_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|moonbeam_token_transfers|from_address|Address of the sender|string|
|moonbeam_token_transfers|log_index|Log index in the transaction receipt|integer|
|moonbeam_token_transfers|to_address|Address of the receiver|string|
|moonbeam_token_transfers|token_address|ERC20 token address|string|
|moonbeam_token_transfers|transaction_hash|Transaction hash|string|
|moonbeam_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|moonbeam_transactions|block_hash|Hash of the block where this transaction was in|string|
|moonbeam_transactions|block_number|Block number where this transaction was in|integer|
|moonbeam_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|moonbeam_transactions|from_address|Address of the sender|string|
|moonbeam_transactions|gas|Gas provided by the sender|integer|
|moonbeam_transactions|gas_price|Gas price provided by the sender |float|
|moonbeam_transactions|hash|Hash of the transaction|string|
|moonbeam_transactions|input|The data sent along with the transaction|string|
|moonbeam_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|moonbeam_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|moonbeam_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|moonbeam_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|moonbeam_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|moonbeam_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|moonbeam_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|moonbeam_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|moonbeam_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|moonbeam_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|moonbeam_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|moonbeam_transactions|transaction_type|Transaction type|integer|
|moonbeam_transactions|value|Value transferred |float|
|moonriver_logs|address|Address from which this log originated|string|
|moonriver_logs|block_hash|Hash of the block where this log was in|string|
|moonriver_logs|block_number|The block number where this log was in|integer|
|moonriver_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|moonriver_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|moonriver_logs|log_index|Integer of the log index position in the block|integer|
|moonriver_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|moonriver_logs|transaction_hash|Hash of the transactions this log was created from|string|
|moonriver_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|moonriver_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). |integer|
|moonriver_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|moonriver_token_transfers|block_number|Block number where this transfer was in|integer|
|moonriver_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|moonriver_token_transfers|from_address|Address of the sender|string|
|moonriver_token_transfers|log_index|Log index in the transaction receipt|integer|
|moonriver_token_transfers|to_address|Address of the receiver|string|
|moonriver_token_transfers|token_address|ERC20 token address|string|
|moonriver_token_transfers|transaction_hash|Transaction hash|string|
|moonriver_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|moonriver_transactions|block_hash|Hash of the block where this transaction was in|string|
|moonriver_transactions|block_number|Block number where this transaction was in|integer|
|moonriver_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|moonriver_transactions|from_address|Address of the sender|string|
|moonriver_transactions|gas|Gas provided by the sender|integer|
|moonriver_transactions|gas_price|Gas price provided by the sender |float|
|moonriver_transactions|hash|Hash of the transaction|string|
|moonriver_transactions|input|The data sent along with the transaction|string|
|moonriver_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|moonriver_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|moonriver_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|moonriver_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|moonriver_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|moonriver_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|moonriver_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|moonriver_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|moonriver_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|moonriver_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|moonriver_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|moonriver_transactions|transaction_type|Transaction type|integer|
|moonriver_transactions|value|Value transferred |float|
|nft_aggregator_info|aggregator_name|The name of aggregator|string|
|nft_aggregator_info|aggregator_slug|The slug of aggregator|string|
|nft_aggregator_info|chain|The chain to which the contract belongs|string|
|nft_aggregator_info|contract_address|The contract address of aggregator|string|
|nft_aggregator_info|created_at|The time when this record was created|timestamp|
|nft_aggregator_info|created_by|Who created this record|string|
|nft_aggregator_info|updated_at|When this record was last modified|timestamp|
|nft_aggregator_info|updated_by|The latest person who edited this record|string|
|nft_collection_daily_stats|amount_currency|Value of amount denominated in this currency|string|
|nft_collection_daily_stats|avg_price|Average price of nft collection denominated in USD|double|
|nft_collection_daily_stats|avg_price_amount|Average price of nft collection denominated in amount_currency|double|
|nft_collection_daily_stats|chain|Chain name|string|
|nft_collection_daily_stats|collection_contract_address|The contract address of collection|string|
|nft_collection_daily_stats|collection_name|The name of collection|string|
|nft_collection_daily_stats|collection_slug|Abbreviation of the nft collection|string|
|nft_collection_daily_stats|floor_price|Floor price of nft collection denominated in USD|double|
|nft_collection_daily_stats|floor_price_amount|Floor price of nft collection denominated in amount_currency|double|
|nft_collection_daily_stats|liquidity_rate|The liquidity of this collection if sales|double|
|nft_collection_daily_stats|market_cap|The market cap of this collection denominated in USD|double|
|nft_collection_daily_stats|market_cap_amount|The market cap of this collection denominated in amount_currency|double|
|nft_collection_daily_stats|max_price|Max price of nft collection denominated in USD|double|
|nft_collection_daily_stats|max_price_amount|Max price of nft denominated in amount_currency|double|
|nft_collection_daily_stats|min_price|Min price of nft collection denominated in USD|double|
|nft_collection_daily_stats|min_price_amount|Min price of nft collection denominated in amount_currency|double|
|nft_collection_daily_stats|number_of_burn_transactions|The number of burn transactions on the date|integer|
|nft_collection_daily_stats|number_of_buyers|The number of buyers on the date|integer|
|nft_collection_daily_stats|number_of_holders|The number of holders on the date|integer|
|nft_collection_daily_stats|number_of_mint_transactions|The number of mint transactions on the date|integer|
|nft_collection_daily_stats|number_of_sales_transactions|The number of sales transactions on the date|integer|
|nft_collection_daily_stats|number_of_sellers|The number of sellers on the date|integer|
|nft_collection_daily_stats|number_of_transactions|The number of transactions on the date|integer|
|nft_collection_daily_stats|number_of_transfer_transactions|The number of transfer transactions on the date|integer|
|nft_collection_daily_stats|on_date|The date of statistics|date|
|nft_collection_daily_stats|total_minted|Total nft items have been minted in the collection|integer|
|nft_collection_daily_stats|total_supply|The total number of NFT items minted on the specified date minus the total number burned in collections  until that day.|integer|
|nft_collection_daily_stats|volume|Sum up amount of trading volume denominated in USD|double|
|nft_collection_daily_stats|volume_amount|Amount of trading volume denominated in amount_currency|double|
|nft_collection_info|chain|The chain to which the contract belongs|string|
|nft_collection_info|collection_created_at|The contract create time of nft collection or first minted time.|timestamp|
|nft_collection_info|collection_name|The name of nft collection|string|
|nft_collection_info|collection_slug|The unique field of the collection|string|
|nft_collection_info|collection_type|type of collection|array|
|nft_collection_info|contract_address|Address of the contract|string|
|nft_collection_info|created_at|The time when this record was created|timestamp|
|nft_collection_info|created_by|Who created this record|string|
|nft_collection_info|created_date|The contract create time of nft collection or first minted time.|date|
|nft_collection_info|deploy_block_number|The block height when this contract was deployed|integer|
|nft_collection_info|deploy_transaction_hash|The transaction hash when this contract was deployed|string|
|nft_collection_info|description|The description of nft collection|string|
|nft_collection_info|discord_url|The discord invite link of nft collection|string|
|nft_collection_info|instagram_username|The instagram username of nft collection|string|
|nft_collection_info|logo|The logo of nft collection|string|
|nft_collection_info|medium_username|The medium username of nft collection|string|
|nft_collection_info|owner|The owner of nft collection|string|
|nft_collection_info|protocol_slug|The protocol of nft collection|string|
|nft_collection_info|standard|Contract strandard (erc1155/erc721/erc20)|string|
|nft_collection_info|symbol|The symbol of nft collection|string|
|nft_collection_info|telegram_url|The telegram invite link of nft collection|string|
|nft_collection_info|total_supply|The contract create count of nft collection. If undefined then -1|integer|
|nft_collection_info|twitter_username|The twitter username of nft collection|string|
|nft_collection_info|updated_at|When this record was last modified|timestamp|
|nft_collection_info|updated_by|The latest person who edited this record|string|
|nft_collection_info|website_url|Tthe website of nft collection|string|
|nft_collection_latest_floor_price|chain|chain name|string|
|nft_collection_latest_floor_price|collection_contract_address|The contract address of collection|string|
|nft_collection_latest_floor_price|collection_slug|The slug of collection|string|
|nft_collection_latest_floor_price|floor_price_native_amount|Floor price of the collection in native token value like eth/matic|float|
|nft_collection_latest_floor_price|floor_price_usd_value|Floor price of the collection in usd value|float|
|nft_collection_latest_floor_price|updated_at|update timestamp|timestamp|
|nft_collection_latest_stats|chain|chain name|string|
|nft_collection_latest_stats|collection_contract_address|The contract address of collection|string|
|nft_collection_latest_stats|collection_slug|The slug of collection|string|
|nft_collection_latest_stats|floor_price_native_amount|Floor price of the collection in native token value like eth/matic|float|
|nft_collection_latest_stats|floor_price_usd_value|Floor price of the collection in usd value|float|
|nft_collection_latest_stats|market_cap|The market cap of this collection denominated in USD|float|
|nft_collection_latest_stats|market_cap_amount|The market cap of this collection denominated in amount_currency|float|
|nft_collection_latest_stats|sales_24h|Nearly 24 hours, the number of items in the nft collection for the transaction|integer|
|nft_collection_latest_stats|total_supply|The contract create count of nft collection.|integer|
|nft_collection_latest_stats|updated_at|update timestamp|timestamp|
|nft_collection_latest_stats|volume_24h|Nearly 24 hours, sum up amount of trading volume denominated in USD|float|
|nft_collection_latest_stats|volume_24h_amount|Nearly 24 hours, amount of trading volume denominated in amount_currency|float|
|nft_collection_transfers_daily_stats|chain|chain name|string|
|nft_collection_transfers_daily_stats|collection_contract_address|The contract address of collection|string|
|nft_collection_transfers_daily_stats|number_of_burn_transactions|The number of burn transactions on the date|integer|
|nft_collection_transfers_daily_stats|number_of_holders|The number of holders on the date|integer|
|nft_collection_transfers_daily_stats|number_of_mint_transactions|The number of mint transactions on the date|integer|
|nft_collection_transfers_daily_stats|number_of_transactions|The number of transactions on the date|integer|
|nft_collection_transfers_daily_stats|number_of_transfer_transactions|The number of transfer transactions on the date|integer|
|nft_collection_transfers_daily_stats|on_date|The date of statistics|date|
|nft_collection_transfers_daily_stats|total_minted|Total nft items have been minted in the collection|integer|
|nft_collection_transfers_daily_stats|total_supply|The amount of nft items that have already been minted, minus any items that have been burned|integer|
|nft_info|animation_url|animation url|string|
|nft_info|chain|chain|string|
|nft_info|collection_contract_address|collection_contract_address|string|
|nft_info|collection_name|name of collection|string|
|nft_info|collection_slug|abbreviation of the nft collection|string|
|nft_info|created_at|the create time of this record|timestamp|
|nft_info|created_by|the person created this record|string|
|nft_info|description|description of nft|string|
|nft_info|image_mime_type|The format of NFT|string|
|nft_info|image_url|url of image|string|
|nft_info|internet_mime_type|The format of NFT|string|
|nft_info|metadata|off chain metadata|string|
|nft_info|metadata_uri|uri of metadata|string|
|nft_info|mint_address|address of mint nft|string|
|nft_info|mint_block_timestamp|block timestamp of mint nft transaction|timestamp|
|nft_info|mint_transaction_hash|hash of mint nft transaction|string|
|nft_info|nft_token_id|token id of nft or nft mint account in Solana|string|
|nft_info|token_name|name of nft|string|
|nft_info|updated_at|the last update time of this record|timestamp|
|nft_info|updated_by|last update person|string|
|nft_latest_stats_dev|amount_currency|The token used for the transaction|string|
|nft_latest_stats_dev|avg_price|Average price of the nft item denominated in USD|double|
|nft_latest_stats_dev|avg_price_amount|Average price of the nft item denominated in amount_currency|double|
|nft_latest_stats_dev|chain|Chain name|string|
|nft_latest_stats_dev|collection_contract_address|The contract address of collection|string|
|nft_latest_stats_dev|collection_name|The name of collection|string|
|nft_latest_stats_dev|collection_slug|Abbreviation of the nft collection|string|
|nft_latest_stats_dev|current_hold_time|The longest hold time among all the current holders|integer|
|nft_latest_stats_dev|holder|Current holder wallet address|string|
|nft_latest_stats_dev|latest_price|Latest price of the nft item denominated in USD|double|
|nft_latest_stats_dev|latest_price_amount|Latest price of the nft item denominated in amount_currency|double|
|nft_latest_stats_dev|longest_hold_time|The longest hold time among holders in the whole history|integer|
|nft_latest_stats_dev|max_price|Max price of the nft item denominated in USD|double|
|nft_latest_stats_dev|max_price_1y|365 days percentage change of max price denominated in USD|double|
|nft_latest_stats_dev|max_price_30d|30 days percentage change of max price denominated in USD|double|
|nft_latest_stats_dev|max_price_3m|90 days percentage change of max price denominated in USD|double|
|nft_latest_stats_dev|max_price_7d|7 days percentage change of max price denominated in USD|double|
|nft_latest_stats_dev|max_price_amount|Max price of the nft item denominated in amount_currency|double|
|nft_latest_stats_dev|max_price_amount_1y|365 days percentage change of max price denominated in amount_currency|double|
|nft_latest_stats_dev|max_price_amount_30d|30 days percentage change of max price denominated in amount_currency|double|
|nft_latest_stats_dev|max_price_amount_3m|90 days percentage change of max price denominated in amount_currency|double|
|nft_latest_stats_dev|max_price_amount_7d|7 days percentage change of max price denominated in amount_currency|double|
|nft_latest_stats_dev|min_price|Min price of the nft item denominated in USD|double|
|nft_latest_stats_dev|min_price_amount|Min price of the nft item denominated in amount_currency|double|
|nft_latest_stats_dev|mint_block_timestamp|Timestamp when the nft item minted|timestamp|
|nft_latest_stats_dev|nft_token_id|The token if of the nft collection|string|
|nft_latest_stats_dev|number_of_past_owners|The number of holders through whole history|integer|
|nft_latest_stats_dev|number_of_sales_transactions|The number of sales transactions of this nft items|integer|
|nft_latest_stats_dev|number_of_sales_transactions_1y|365 days percentage change of number_of_sales_transaction|integer|
|nft_latest_stats_dev|number_of_sales_transactions_30d|30 days percentage change of number_of_sales_transaction|integer|
|nft_latest_stats_dev|number_of_sales_transactions_3m|90 days percentage change of number_of_sales_transaction|integer|
|nft_latest_stats_dev|number_of_sales_transactions_7d|7 days percentage change of number_of_sales_transaction|integer|
|nft_latest_stats_dev|on_date|The date of statistics|timestamp|
|nft_latest_stats_dev|status|The token status,minted/burned|string|
|nft_token_attributes|attribute_key|the key of attribute|string|
|nft_token_attributes|attribute_type|the type of attribute value|string|
|nft_token_attributes|attribute_value|the value of attribute|string|
|nft_token_attributes|chain|the chain to which the contract belongs|string|
|nft_token_attributes|collection_contract_address|collection contract address|string|
|nft_token_attributes|collection_slug|collection slug|string|
|nft_token_attributes|created_at|the timestamp of this records created|timestamp|
|nft_token_attributes|created_by|the creator of this records|string|
|nft_token_attributes|nft_token_id|the id of this NFT Collection|STRING|
|nft_token_attributes|updated_at|the timestamp of this records updated|timestamp|
|nft_token_attributes|updated_by|the operator of this records updated|string|
|nft_transactions|amount|number of tokens transferred|float|
|nft_transactions|amount_currency|amount currency|string|
|nft_transactions|amount_currency_contract_address|token address of amount currency|string|
|nft_transactions|block_date|DateTime of this transaction was in|date|
|nft_transactions|block_number|Block number where this transaction was in|int|
|nft_transactions|block_timestamp|Timestamp of the block where this transaction was in||
|nft_transactions|block_timestampf_value - latest_time_after_yesterday|Timestamp of the block where this transaction was in||
|nft_transactions|buyer_address|address of buyer|string|
|nft_transactions|chain|the chain to which the contract belongs|string|
|nft_transactions|collection_contract_address|collection contract address|string|
|nft_transactions|collection_slug|collection slug|string|
|nft_transactions|internal_index|log index of transaction hash|string|
|nft_transactions|log_index|Log index in the transaction receipt|string|
|nft_transactions|marketplace_contract_address|marketplace contract address|string|
|nft_transactions|marketplace_slug|marketplace protocol name|string|
|nft_transactions|nft_token_id|the id of this NFT Collection|STRING|
|nft_transactions|number_of_nft_token_id|how many nfts were transacted in this transaction|float|
|nft_transactions|platform_fee_rate|platform fee rate|float|
|nft_transactions|platform_fees_amount|platform fees amount|float|
|nft_transactions|platform_fees_value|platform fees value (USD)|float|
|nft_transactions|royalty_amount|royalty amount|float|
|nft_transactions|royalty_rate|royalty rate|float|
|nft_transactions|royalty_value|royalty value (USD)|float|
|nft_transactions|seller_address|address of seller|string|
|nft_transactions|trade_type|trade type (single/bundle/batch)|string|
|nft_transactions|transaction_hash|Hash of the transaction|string|
|nft_transactions|value|Amount of tokens transferred(USD)|float|
|nft_transactions|value_currency|value currency|string|
|nft_transactions_v1|amount|number of tokens transferred|float|
|nft_transactions_v1|amount_currency|amount currency|string|
|nft_transactions_v1|amount_currency_contract_address|token address of amount currency|string|
|nft_transactions_v1|block_date|DateTime of this transaction was in|date|
|nft_transactions_v1|block_number|Block number where this transaction was in|int|
|nft_transactions_v1|block_timestamp|Timestamp of the block where this transaction was in||
|nft_transactions_v1|buyer_address|address of buyer|string|
|nft_transactions_v1|chain|the chain to which the contract belongs|string|
|nft_transactions_v1|collection_contract_address|collection contract address|string|
|nft_transactions_v1|collection_slug|collection slug|string|
|nft_transactions_v1|internal_index|log index of transaction hash|string|
|nft_transactions_v1|log_index|Log index in the transaction receipt|string|
|nft_transactions_v1|marketplace_contract_address|marketplace contract address|string|
|nft_transactions_v1|marketplace_slug|marketplace protocol name|string|
|nft_transactions_v1|nft_token_id|the id of this NFT Collection|STRING|
|nft_transactions_v1|number_of_nft_token_id|how many nfts were transacted in this transaction|float|
|nft_transactions_v1|platform_fee_rate|platform fee rate|float|
|nft_transactions_v1|platform_fees_amount|platform fees amount|float|
|nft_transactions_v1|platform_fees_value|platform fees value (USD)|float|
|nft_transactions_v1|royalty_amount|royalty amount|float|
|nft_transactions_v1|royalty_rate|royalty rate|float|
|nft_transactions_v1|royalty_value|royalty value (USD)|float|
|nft_transactions_v1|seller_address|address of seller|string|
|nft_transactions_v1|trade_type|trade type (single/bundle/batch)|string|
|nft_transactions_v1|transaction_hash|Hash of the transaction|string|
|nft_transactions_v1|value|Amount of tokens transferred(USD)|float|
|nft_transactions_v1|value_currency|value currency|string|
|nft_transfers|amount_raw|Amount of tokens transferred / id of the token transferred (NFT)|double|
|nft_transfers|block_date|Date of the block|date|
|nft_transfers|block_number|Block number where this transfer was in|integer|
|nft_transfers|block_timestamp|Timestamp of the block|timestamp|
|nft_transfers|chain|The chain to which the contract belongs|string|
|nft_transfers|collection_contract_address|The contract address of the collection|string|
|nft_transfers|from_address|Address of the sender|string|
|nft_transfers|internal_index|Log index of transaction hash|string|
|nft_transfers|log_index|Log index of transaction hash|integer|
|nft_transfers|nft_token_id|Id of the token transferred (NFT)|string|
|nft_transfers|to_address|Address of the receiver|string|
|nft_transfers|token_address|Token address|string|
|nft_transfers|transaction_hash|Transaction hash|string|
|nft_transfers|transfer_type|Type for nft transfers|string|
|oasys_logs|address|Address from which this log originated|string|
|oasys_logs|block_hash|Hash of the block where this log was in|string|
|oasys_logs|block_number|The block number where this log was in|integer|
|oasys_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|oasys_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|oasys_logs|log_index|Integer of the log index position in the block|integer|
|oasys_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|oasys_logs|transaction_hash|Hash of the transactions this log was created from|string|
|oasys_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|oasys_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|oasys_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|oasys_token_transfers|block_number|Block number where this transfer was in|integer|
|oasys_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|oasys_token_transfers|from_address|Address of the sender|string|
|oasys_token_transfers|log_index|Log index in the transaction receipt|integer|
|oasys_token_transfers|to_address|Address of the receiver|string|
|oasys_token_transfers|token_address|ERC20 token address|string|
|oasys_token_transfers|transaction_hash|Transaction hash|string|
|oasys_transactions|block_hash|Hash of the block where this transaction was in|string|
|oasys_transactions|block_number|Block number where this transaction was in|integer|
|oasys_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|oasys_transactions|from_address|Address of the sender|string|
|oasys_transactions|gas|Gas provided by the sender|integer|
|oasys_transactions|gas_price|Gas price provided by the sender|float|
|oasys_transactions|hash|Hash of the transaction|string|
|oasys_transactions|input|The data sent along with the transaction|string|
|oasys_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|oasys_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|oasys_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|oasys_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|oasys_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|oasys_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|oasys_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|oasys_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|oasys_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|oasys_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|oasys_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|oasys_transactions|transaction_type|Transaction type|integer|
|oasys_transactions|value|Value transferred|float|
|optimism_blocks|base_fee_per_gas|Protocol base fee per gas, which can move up or down|integer|
|optimism_blocks|difficulty|Integer of the difficulty for this block|integer|
|optimism_blocks|extra_data|The extra data field of this block|string|
|optimism_blocks|gas_limit|The maximum gas allowed in this block|integer|
|optimism_blocks|gas_used|The total used gas by all transactions in this block|integer|
|optimism_blocks|hash|Hash of the block|string|
|optimism_blocks|logs_bloom|The bloom filter for the logs of the block|string|
|optimism_blocks|miner|The address of the beneficiary to whom the mining rewards were given|string|
|optimism_blocks|nonce|Hash of the generated proof-of-work|string|
|optimism_blocks|number|The block number|integer|
|optimism_blocks|parent_hash|Hash of the parent block|string|
|optimism_blocks|receipts_root|The root of the receipts trie of the block|string|
|optimism_blocks|sha3_uncles|SHA3 of the uncles data in the block|string|
|optimism_blocks|size|The size of this block in bytes|integer|
|optimism_blocks|state_root|The root of the final state trie of the block|string|
|optimism_blocks|timestamp|The unix timestamp for when the block was collated|timestamp|
|optimism_blocks|total_difficulty|Integer of the total difficulty of the chain until this block|integer|
|optimism_blocks|transaction_count|The number of transactions in the block|integer|
|optimism_blocks|transactions_root|The root of the transaction trie of the block|string|
|optimism_community_decoded_events|block_number|The block number where this event was in|integer|
|optimism_community_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|optimism_community_decoded_events|contract_address|Contract address from which this log originated|string|
|optimism_community_decoded_events|contract_name|The contract name of the event|string|
|optimism_community_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|optimism_community_decoded_events|event_name|The name of event|string|
|optimism_community_decoded_events|log_index|Integer of the event index position in the block|integer|
|optimism_community_decoded_events|protocol_slug|The protocol which the contract belongs, associate protocol_info for details|string|
|optimism_community_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|optimism_contract|bytecode||string|
|optimism_contract|contract_address||string|
|optimism_contract|deploy_block_number||integer|
|optimism_contract|deploy_block_timestamp||timestamp|
|optimism_contract|deploy_deployer_address||string|
|optimism_contract|deploy_transaction_hash||string|
|optimism_decoded_events|block_number|The block number where this event was in|integer|
|optimism_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|optimism_decoded_events|contract_address|Contract address from which this log originated|string|
|optimism_decoded_events|contract_name|The contract name of the event|string|
|optimism_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|optimism_decoded_events|event_name|The name of event|string|
|optimism_decoded_events|log_index|Integer of the event index position in the block|integer|
|optimism_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|optimism_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|optimism_logs|address|Address from which this log originated|string|
|optimism_logs|block_hash|Hash of the block where this log was in|string|
|optimism_logs|block_number|The block number where this log was in|integer|
|optimism_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|optimism_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|optimism_logs|log_index|Integer of the log index position in the block|integer|
|optimism_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|optimism_logs|transaction_hash|Hash of the transactions this log was created from|string|
|optimism_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|optimism_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|optimism_token_transfers|block_number|Block number where this transfer was in|integer|
|optimism_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|optimism_token_transfers|from_address|Address of the sender|string|
|optimism_token_transfers|log_index|Log index in the transaction receipt|integer|
|optimism_token_transfers|to_address|Address of the receiver|string|
|optimism_token_transfers|token_address|ERC20 token address|string|
|optimism_token_transfers|transaction_hash|Transaction hash|string|
|optimism_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|string|
|optimism_transactions|block_hash|Hash of the block where this transaction was in|string|
|optimism_transactions|block_number|Block number where this transaction was in|integer|
|optimism_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|optimism_transactions|from_address|Address of the sender|string|
|optimism_transactions|gas|Gas provided by the sender|integer|
|optimism_transactions|gas_price|Gas price provided by the sender |float|
|optimism_transactions|hash|Hash of the transaction|string|
|optimism_transactions|input|The data sent along with the transaction|string|
|optimism_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|optimism_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|optimism_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|optimism_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|optimism_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|optimism_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|optimism_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|optimism_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|optimism_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|optimism_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|optimism_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|optimism_transactions|transaction_type|Transaction type|integer|
|optimism_transactions|value|Value transferred |float|
|polygon_blocks|base_fee_per_gas|Protocol base fee per gas, which can move up or down|integer|
|polygon_blocks|difficulty|Integer of the difficulty for this block|integer|
|polygon_blocks|extra_data|The extra data field of this block|string|
|polygon_blocks|gas_limit|The maximum gas allowed in this block|integer|
|polygon_blocks|gas_used|The total used gas by all transactions in this block|integer|
|polygon_blocks|hash|Hash of the block|string|
|polygon_blocks|logs_bloom|The bloom filter for the logs of the block|string|
|polygon_blocks|miner|The address of the beneficiary to whom the mining rewards were given|string|
|polygon_blocks|nonce|Hash of the generated proof-of-work|string|
|polygon_blocks|number|The block number|integer|
|polygon_blocks|parent_hash|Hash of the parent block|string|
|polygon_blocks|receipts_root|The root of the receipts trie of the block|string|
|polygon_blocks|sha3_uncles|SHA3 of the uncles data in the block|string|
|polygon_blocks|size|The size of this block in bytes|integer|
|polygon_blocks|state_root|The root of the final state trie of the block|string|
|polygon_blocks|timestamp|The unix timestamp for when the block was collated|timestamp|
|polygon_blocks|total_difficulty|Integer of the total difficulty of the chain until this block|integer|
|polygon_blocks|transaction_count|The number of transactions in the block|integer|
|polygon_blocks|transactions_root|The root of the transaction trie of the block|string|
|polygon_community_decoded_events|block_number|The block number where this event was in|integer|
|polygon_community_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|polygon_community_decoded_events|contract_address|Contract address from which this log originated|string|
|polygon_community_decoded_events|contract_name|The contract name of the event|string|
|polygon_community_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|polygon_community_decoded_events|event_name|The name of event|string|
|polygon_community_decoded_events|log_index|Integer of the event index position in the block|integer|
|polygon_community_decoded_events|protocol_slug|The protocol which the contract belongs, associate protocol_info for details|string|
|polygon_community_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|polygon_contract|bytecode||string|
|polygon_contract|contract_address||string|
|polygon_contract|deploy_block_number||integer|
|polygon_contract|deploy_block_timestamp||timestamp|
|polygon_contract|deploy_deployer_address||string|
|polygon_contract|deploy_transaction_hash||string|
|polygon_decoded_events|block_number|The block number where this event was in|integer|
|polygon_decoded_events|block_timestamp|Timestamp of the block where this event was in|timestamp|
|polygon_decoded_events|contract_address|Contract address from which this log originated|string|
|polygon_decoded_events|contract_name|The contract name of the event|string|
|polygon_decoded_events|decoded_data|Data of the event was decoded, usage examples: json_query(decoded_data, 'lax $.{FIELD_NAME}' OMIT QUOTES) |string|
|polygon_decoded_events|event_name|The name of event|string|
|polygon_decoded_events|log_index|Integer of the event index position in the block|integer|
|polygon_decoded_events|protocol_slug|The protocol which the contract belongs|string|
|polygon_decoded_events|transaction_hash|Hash of the transactions this event was created from|string|
|polygon_logs|address|Address from which this log originated|string|
|polygon_logs|block_hash|Hash of the block where this log was in|string|
|polygon_logs|block_number|The block number where this log was in|integer|
|polygon_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|polygon_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|polygon_logs|log_index|Integer of the log index position in the block|integer|
|polygon_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|polygon_logs|transaction_hash|Hash of the transactions this log was created from|string|
|polygon_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|polygon_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|integer|
|polygon_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|polygon_token_transfers|block_number|Block number where this transfer was in|integer|
|polygon_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|polygon_token_transfers|from_address|Address of the sender|string|
|polygon_token_transfers|log_index|Log index in the transaction receipt|integer|
|polygon_token_transfers|to_address|Address of the receiver|string|
|polygon_token_transfers|token_address|ERC20 token address|string|
|polygon_token_transfers|transaction_hash|Transaction hash|string|
|polygon_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|polygon_transactions|block_hash|Hash of the block where this transaction was in|string|
|polygon_transactions|block_number|Block number where this transaction was in|integer|
|polygon_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|polygon_transactions|from_address|Address of the sender|string|
|polygon_transactions|gas|Gas provided by the sender|integer|
|polygon_transactions|gas_price|Gas price provided by the sender |float|
|polygon_transactions|hash|Hash of the transaction|string|
|polygon_transactions|input|The data sent along with the transaction|string|
|polygon_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|polygon_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|polygon_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|polygon_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|polygon_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|polygon_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|polygon_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|polygon_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|polygon_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|polygon_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|polygon_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|polygon_transactions|transaction_type|Transaction type|integer|
|polygon_transactions|value|Value transferred |float|
|portfolio_latest_stats|portfolio_name|The name of portfolio|string|
|portfolio_latest_stats|portfolio_slug|The slug of portfolio|string|
|portfolio_latest_stats|portfolio_type|The category of portfolio|string|
|portfolio_latest_stats|value|Latest balance in USD|double|
|portfolio_latest_stats|value_24h_pct_change|The rate of change between the latest balance and the balance before 24H|double|
|portfolio_latest_stats|value_7d_pct_change|The rate of change between the latest balance and the balance before 7D|double|
|portfolio_latest_stats|value_change_24h|The difference between the latest balance and the balance before 24H|double|
|portfolio_latest_stats|value_change_7d|The difference between the latest balance and the balance before 7D|double|
|portfolio_token_latest_stats|chain|The chain to which the contract belongs|string|
|portfolio_token_latest_stats|portfolio_name|The name of portfolio|string|
|portfolio_token_latest_stats|portfolio_slug|The slug of portfolio|string|
|portfolio_token_latest_stats|portfolio_type|The category of portfolio|string|
|portfolio_token_latest_stats|token_address|The address of the chain|string|
|portfolio_token_latest_stats|token_balance|The balance in USD of the token|string|
|portfolio_token_latest_stats|token_symbol|The symbol of the token|string|
|portfolio_token_latest_stats|value|Latest balance in USD|double|
|portfolio_token_latest_stats|value_24h_pct_change|The rate of change between the latest balance and the balance before 24H|double|
|portfolio_token_latest_stats|value_7d_pct_change|The rate of change between the latest balance and the balance before 7D|double|
|portfolio_token_latest_stats|value_change_24h|The difference between the latest balance and the balance before 24H|double|
|portfolio_token_latest_stats|value_change_7d|The difference between the latest balance and the balance before 7D|double|
|protocol_active_address|chain|The chain of protocol|string|
|protocol_active_address|is_new_address|First transaction address|integer|
|protocol_active_address|on_date|The statistical date|date|
|protocol_active_address|protocol_name|Name of protocol|string|
|protocol_active_address|protocol_slug|Abbreviation of protocol|string|
|protocol_active_address|protocol_type|Type of protocol|string|
|protocol_active_address|wallet_address|Wallet address|string|
|protocol_address_retention_monthly|chain|The chain to which the protocol belongs|string|
|protocol_address_retention_monthly|cohort|Statistical month|string|
|protocol_address_retention_monthly|end_date|End time of the statistical month|date|
|protocol_address_retention_monthly|month_1|Retention rate for the month|float|
|protocol_address_retention_monthly|month_10|Retention rate for the month|float|
|protocol_address_retention_monthly|month_11|Retention rate for the month|float|
|protocol_address_retention_monthly|month_12|Retention rate for the month|float|
|protocol_address_retention_monthly|month_2|Retention rate for the month|float|
|protocol_address_retention_monthly|month_3|Retention rate for the month|float|
|protocol_address_retention_monthly|month_4|Retention rate for the month|float|
|protocol_address_retention_monthly|month_5|Retention rate for the month|float|
|protocol_address_retention_monthly|month_6|Retention rate for the month|float|
|protocol_address_retention_monthly|month_7|Retention rate for the month|float|
|protocol_address_retention_monthly|month_8|Retention rate for the month|float|
|protocol_address_retention_monthly|month_9|Retention rate for the month|float|
|protocol_address_retention_monthly|number_of_new_users|Number of new users at this month|integer|
|protocol_address_retention_monthly|protocol_name|Name of the protocol|string|
|protocol_address_retention_monthly|protocol_slug|Abbreviation of the protocol|string|
|protocol_address_retention_monthly|start_date|Start time of the statistical month|date|
|protocol_address_retention_weekly|chain|The chain to which the protocol belongs|string|
|protocol_address_retention_weekly|cohort|Statistical week|string|
|protocol_address_retention_weekly|end_date|End time of the statistical week|date|
|protocol_address_retention_weekly|number_of_new_users|Number of new users at this week|integer|
|protocol_address_retention_weekly|protocol_name|Name of the protocol|string|
|protocol_address_retention_weekly|protocol_slug|Abbreviation of the protocol|string|
|protocol_address_retention_weekly|start_date|Start time of the statistical week|date|
|protocol_address_retention_weekly|week_1|Retention rate for the week|float|
|protocol_address_retention_weekly|week_10|Retention rate for the week|float|
|protocol_address_retention_weekly|week_11|Retention rate for the week|float|
|protocol_address_retention_weekly|week_12|Retention rate for the week|float|
|protocol_address_retention_weekly|week_2|Retention rate for the week|float|
|protocol_address_retention_weekly|week_3|Retention rate for the week|float|
|protocol_address_retention_weekly|week_4|Retention rate for the week|float|
|protocol_address_retention_weekly|week_5|Retention rate for the week|float|
|protocol_address_retention_weekly|week_6|Retention rate for the week|float|
|protocol_address_retention_weekly|week_7|Retention rate for the week|float|
|protocol_address_retention_weekly|week_8|Retention rate for the week|float|
|protocol_address_retention_weekly|week_9|Retention rate for the week|float|
|protocol_daily_stats|active_users_180d_pct_change|The growth rate of the current number of new users compared to the number of active users 180 days ago|double|
|protocol_daily_stats|active_users_1d_pct_change|The growth rate of the current number of new users compared to the number of active users 1 day ago|double|
|protocol_daily_stats|active_users_30d_pct_change|The growth rate of the current number of new users compared to the number of active users 30 days ago|double|
|protocol_daily_stats|active_users_360d_pct_change|The growth rate of the current number of new users compared to the number of active users 360 days ago|double|
|protocol_daily_stats|active_users_7d_pct_change|The growth rate of the current number of new users compared to the number of active users 7 days ago|double|
|protocol_daily_stats|chain|The chain to which the contract belongs|string|
|protocol_daily_stats|new_users_180d_pct_change|The growth rate of the current number of new users compared to the number of new users 180 days ago|double|
|protocol_daily_stats|new_users_1d_pct_change|The growth rate of the current number of new users compared to the number of new users 1 day ago|double|
|protocol_daily_stats|new_users_30d_pct_change|The growth rate of the current number of new users compared to the number of new users 30 days ago|double|
|protocol_daily_stats|new_users_360d_pct_change|The growth rate of the current number of new users compared to the number of new users 360 days ago|double|
|protocol_daily_stats|new_users_7d_pct_change|The growth rate of the current number of new users compared to the number of new users 7 days ago|double|
|protocol_daily_stats|number_of_active_users|The number of active wallet addresses interacting with dapp's smart contracts|integer|
|protocol_daily_stats|number_of_new_users|The number of new addresses who made the first transaction with the smart contract of this protocol on the statistical day|integer|
|protocol_daily_stats|number_of_total_users|The cumulative number of users who made the first transaction with the smart contract of this protocol on the statistical day|integer|
|protocol_daily_stats|number_of_transactions|the number of transaction between wallet and contract_address|double|
|protocol_daily_stats|on_date|Statistical date|date|
|protocol_daily_stats|protocol_name|Name of the protocol|string|
|protocol_daily_stats|protocol_slug|Abbreviation of the protocol|string|
|protocol_daily_stats|volume|the flat value incoming dapp contract|double|
|protocol_info|categories|The categories of the protocol|array|
|protocol_info|chain|The chain of the protocol|string|
|protocol_info|created_at|The time when this record was created|timestamp|
|protocol_info|created_by|Who created this record|string|
|protocol_info|description|The description of the protocol|string|
|protocol_info|discord|The link of the discord|string|
|protocol_info|github|The link of the github |string|
|protocol_info|logo|The logo link of the protocol|string|
|protocol_info|protocol_name|The protocol name |string|
|protocol_info|protocol_slug|The abbreviation of the protocol |string|
|protocol_info|protocol_sub_type|The sub type of the protocol|string|
|protocol_info|protocol_type|The type ot the protocol(DeFi,NFT or GameFi)|string|
|protocol_info|telegram|The address of telegram|string|
|protocol_info|twitter|The link of the twitter |string|
|protocol_info|updated_at|When this record was last modified|timestamp|
|protocol_info|updated_by|The latest person who edited this record|string|
|protocol_info|web_url|The link of the protocol website|string|
|protocol_token_transfers|amount|Amount of transfer|float|
|protocol_token_transfers|block_timestamp|Time of transactions|timestamp|
|protocol_token_transfers|chain|The chain to which the contract belongs|string|
|protocol_token_transfers|contract_address|Address of contract|string|
|protocol_token_transfers|decimals|Decimals of platform token|integer|
|protocol_token_transfers|from_address|the source address of transfer|string|
|protocol_token_transfers|protocol_slug|Abbreviation of the protocol|string|
|protocol_token_transfers|protocol_type|Type of protocol|string|
|protocol_token_transfers|to_address|the destination address of transfer|string|
|protocol_token_transfers|token_address|Address of platform token|string|
|protocol_token_transfers|token_symbol|Symbol of platform token|string|
|protocol_token_transfers|transaction_hash|Transaction hash|string|
|protocol_token_transfers|type|The flow value in/out contract|string|
|protocol_token_transfers|value|USD value of transfer|float|
|protocol_token_transfers|wallet_address|Address of wallet|string|
|protocol_transactions|amount|Transaction amount|double|
|protocol_transactions|amount_raw|Transaction amount raw|double|
|protocol_transactions|block_timestamp|Time of transactions|timestamp|
|protocol_transactions|chain|The chain to which the contract belongs|string|
|protocol_transactions|contract_address|Address of contract|string|
|protocol_transactions|contract_method_id|Id of method|string|
|protocol_transactions|contract_method_name|Name of method|string|
|protocol_transactions|protocol_name|Name of the protocol|string|
|protocol_transactions|protocol_slug|Abbreviation of the protocol|string|
|protocol_transactions|transaction_hash|Transaction hash|string|
|protocol_transactions|wallet_address|Address of wallat|string|
|ronin_blocks|base_fee_per_gas|Protocol base fee per gas, which can move up or down|integer|
|ronin_blocks|difficulty|Integer of the difficulty for this block|integer|
|ronin_blocks|extra_data|The extra data field of this block|string|
|ronin_blocks|gas_limit|The maximum gas allowed in this block|integer|
|ronin_blocks|gas_used|The total used gas by all transactions in this block|integer|
|ronin_blocks|hash|Hash of the block|string|
|ronin_blocks|logs_bloom|The bloom filter for the logs of the block|string|
|ronin_blocks|miner|The address of the beneficiary to whom the mining rewards were given|string|
|ronin_blocks|nonce|Hash of the generated proof-of-work|string|
|ronin_blocks|number|The block number|integer|
|ronin_blocks|parent_hash|Hash of the parent block|string|
|ronin_blocks|receipts_root|The root of the receipts trie of the block|string|
|ronin_blocks|sha3_uncles|SHA3 of the uncles data in the block|string|
|ronin_blocks|size|The size of this block in bytes|integer|
|ronin_blocks|state_root|The root of the final state trie of the block|string|
|ronin_blocks|timestamp|The unix timestamp for when the block was collated|timestamp|
|ronin_blocks|total_difficulty|Integer of the total difficulty of the chain until this block|integer|
|ronin_blocks|transaction_count|The number of transactions in the block|integer|
|ronin_blocks|transactions_root|The root of the transaction trie of the block|string|
|ronin_logs|address|Address from which this log originated|string|
|ronin_logs|block_hash|Hash of the block where this log was in|string|
|ronin_logs|block_number|The block number where this log was in|integer|
|ronin_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|ronin_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|ronin_logs|log_index|Integer of the log index position in the block|integer|
|ronin_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|ronin_logs|transaction_hash|Hash of the transactions this log was created from|string|
|ronin_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|solana_account_mapping|hold_end_time|End time of holding the token account|timestamp|
|solana_account_mapping|hold_start_time|Start time of holding the token account|timestamp|
|solana_account_mapping|owner|Owner of account|string|
|solana_account_mapping|token_account|Account of token address|string|
|solana_account_mapping|token_address|Address of token|string|
|solana_token_transfers|amount_raw|Amount of tokens transferred / id of the token transferred (NFT) in wei|integer|
|solana_token_transfers|block_hash|Block hash|string|
|solana_token_transfers|block_height|Transfer happens on which block height|integer|
|solana_token_transfers|block_number|Transfer happens on which block number|integer|
|solana_token_transfers|block_timestamp|The time on the block height|timestamp|
|solana_token_transfers|destination|Destination token account of token transfer|string|
|solana_token_transfers|from_post_balance|Token balance of source token account after transfer|float|
|solana_token_transfers|from_pre_balance|Token balance of source token account before transfer|float|
|solana_token_transfers|gen_id|Gen index in the transaction receipt|string|
|solana_token_transfers|main_program|Main program|string|
|solana_token_transfers|main_signer|Main signer|string|
|solana_token_transfers|mint|Token address of mint|string|
|solana_token_transfers|scale|Scale|integer|
|solana_token_transfers|signature|Signature|string|
|solana_token_transfers|source|Source token account of token transfer|string|
|solana_token_transfers|to_post_balance|Token balance of destination token account after transfer|float|
|solana_token_transfers|to_pre_balance|Token balance of destination token account before transfer|float|
|solana_token_transfers|value|Amount of tokens transferred / id of the token transferred (NFT) in wei|string|
|solana_transactions|accounts|Accounts|string|
|solana_transactions|block_hash|Block hash|string|
|solana_transactions|block_height|Block height where this transaction was in|integer|
|solana_transactions|block_number|Block number where this transaction was in|integer|
|solana_transactions|fee|Fee|integer|
|solana_transactions|instructions|Instructions|structural|
|solana_transactions|is_successful|Is successful|boolean|
|solana_transactions|log_messages|Log messages|string|
|solana_transactions|main_signer|Main signer|string|
|solana_transactions|mints|Mints|string|
|solana_transactions|num_accounts|Num accounts|integer|
|solana_transactions|num_instructions|Num instructions|integer|
|solana_transactions|num_mints|Num mints|integer|
|solana_transactions|post_balances|Post balances|structural|
|solana_transactions|post_token_balances|Post token balances|structural|
|solana_transactions|pre_balances|Pre balances|structural|
|solana_transactions|pre_token_balances|Pre token balances|structural|
|solana_transactions|programs|Programs|string|
|solana_transactions|signature|Signature|string|
|solana_transactions|signers|Signers|string|
|solana_transactions|time|Timestamp of the block where this transaction was i|timestamp|
|thunder_core_logs|address|Address from which this log originated|string|
|thunder_core_logs|block_hash|Hash of the block where this log was in|string|
|thunder_core_logs|block_number|The block number where this log was in|integer|
|thunder_core_logs|block_timestamp|Timestamp of the block where this log was in|timestamp|
|thunder_core_logs|data|Contains one or more 32 Bytes non-indexed arguments of the log|string|
|thunder_core_logs|log_index|Integer of the log index position in the block|integer|
|thunder_core_logs|topics|Indexed log arguments (0 to 4 32-byte hex strings). (In solidity: The first topic is the hash of the signature of the event (e.g. Deposit(address,bytes32,uint256)), except you declared the event with the anonymous specifier.)|array|
|thunder_core_logs|transaction_hash|Hash of the transactions this log was created from|string|
|thunder_core_logs|transaction_index|Integer of the transactions index position log was created from|integer|
|thunder_core_token_transfers|amount_raw|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). |integer|
|thunder_core_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|thunder_core_token_transfers|block_number|Block number where this transfer was in|integer|
|thunder_core_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|thunder_core_token_transfers|from_address|Address of the sender|string|
|thunder_core_token_transfers|log_index|Log index in the transaction receipt|integer|
|thunder_core_token_transfers|to_address|Address of the receiver|string|
|thunder_core_token_transfers|token_address|ERC20 token address|string|
|thunder_core_token_transfers|transaction_hash|Transaction hash|string|
|thunder_core_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|thunder_core_transactions|block_hash|Hash of the block where this transaction was in|string|
|thunder_core_transactions|block_number|Block number where this transaction was in|integer|
|thunder_core_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|thunder_core_transactions|from_address|Address of the sender|string|
|thunder_core_transactions|gas|Gas provided by the sender|integer|
|thunder_core_transactions|gas_price|Gas price provided by the sender |float|
|thunder_core_transactions|hash|Hash of the transaction|string|
|thunder_core_transactions|input|The data sent along with the transaction|string|
|thunder_core_transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|thunder_core_transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|thunder_core_transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|thunder_core_transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|thunder_core_transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|thunder_core_transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|thunder_core_transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|thunder_core_transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|thunder_core_transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|thunder_core_transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|thunder_core_transactions|transaction_index|Integer of the transactions index position in the block|integer|
|thunder_core_transactions|transaction_type|Transaction type|integer|
|thunder_core_transactions|value|Value transferred |float|
|token_daily_stats|circulating_supply|The amount of coins that are circulating in the market and are tradeable by the public|float|
|token_daily_stats|fully_diluted_valuation|The total market value of  after  cryptocurrency fully diluted|float|
|token_daily_stats|market_cap|Refers to the total market value of a cryptocurrency’s circulating supply.|float|
|token_daily_stats|max_supply|The maximum number of coins coded to exist in the lifetime of the cryptocurrency.|float|
|token_daily_stats|on_date|The statistical date|date|
|token_daily_stats|price|The price of the end of day|float|
|token_daily_stats|protocol_slug|The slug of the protocol|string|
|token_daily_stats|token_name|The name of the token |string|
|token_daily_stats|token_slug|The abbreviation of the token |string|
|token_daily_stats|token_symbol|The identifier of the token |string|
|token_daily_stats|total_supply|The amount of coins that have already been created, minus any coins that have been burned|float|
|token_daily_stats|trading_vol_24h|A cryptocurrency trading volume across all tracked platforms in the last 24 hours|float|
|token_info|chain|chain|string|
|token_info|created_at|The time when this record was created|timestamp|
|token_info|created_by|Who created this record|string|
|token_info|decimals||integer|
|token_info|logo||string|
|token_info|protocol_slug|The abbreviation of the protocol|string|
|token_info|token_address||string|
|token_info|token_name||string|
|token_info|token_slug||string|
|token_info|token_symbol||string|
|token_info|token_type||array|
|token_info|updated_at|When this record was last modified|timestamp|
|token_info|updated_by|The latest person who edited this record|string|
|token_price_5min|block_timestamp||timestamp|
|token_price_5min|chain|The chain of the token|string|
|token_price_5min|price|The 5min price of the token|double|
|token_price_5min|timestamp|The time of the token|timestamp|
|token_price_5min|token_address|The address of the token|string|
|token_price_5min|token_symbol|The symbol of the token|string|
|token_transfers|block_hash|Hash of the block where this transfer was in|string|
|token_transfers|block_number|Block number where this transfer was in|integer|
|token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|token_transfers|from_address|Address of the sender|string|
|token_transfers|log_index|Log index in the transaction receipt|integer|
|token_transfers|to_address|Address of the receiver|string|
|token_transfers|token_address|ERC20 token address|string|
|token_transfers|transaction_hash|Transaction hash|string|
|token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721).|string|
|traces|block_hash|Hash of the block where this trace was in|string|
|traces|block_number|Block number where this trace was in|integer|
|traces|block_timestamp|Timestamp of the block where this trace was in|timestamp|
|traces|call_type|One of call, callcode, delegatecall, staticcall|string|
|traces|error|Error if message call failed. This field doesn't contain top-level trace errors.|string|
|traces|from_address|Address of the sender, null when trace_type is genesis or reward|string|
|traces|gas|Gas provided with the message call|integer|
|traces|gas_used|Gas used by the message call|integer|
|traces|input|The data sent along with the message call|string|
|traces|output|The output of the message call, bytecode of contract when trace_type is create|string|
|traces|reward_type|One of block, uncle|string|
|traces|status|Either 1 (success) or 0 (failure, due to any operation that can cause the call itself or any top-level call to revert)|integer|
|traces|subtraces|Number of subtraces|integer|
|traces|to_address|Address of the receiver if trace_type is call, address of new contract or null if trace_type is create, beneficiary address if trace_type is suicide, miner address if trace_type is reward, shareholder address if trace_type is genesis, WithdrawDAO address if trace_type is daofork|string|
|traces|trace_address|Comma separated list of trace address in call tree|string|
|traces|trace_id|Unique string that identifies the trace. For transaction-scoped traces it is {trace_type}_{transaction_hash}_{trace_address}. For block-scoped traces it is {trace_type}_{block_number}_{index_within_block}|string|
|traces|trace_type|One of call, create, suicide, reward, genesis, daofork|string|
|traces|transaction_hash|Transaction hash where this trace was in, null if trace_type is reward|string|
|traces|transaction_index|Integer of the transactions index position in the block|integer|
|traces|value|Value transferred in Wei|float|
|transaction_entity_tag|_id|Unique id of this record|string|
|transaction_entity_tag|created_at||timestamp|
|transaction_entity_tag|entity_id|Transaction hash|string|
|transaction_entity_tag|entity_ns_name|The name space name of entity|string|
|transaction_entity_tag|op_id|users who create tag|string|
|transaction_entity_tag|tag_name|The name of label|string|
|transaction_entity_tag|updated_at||timestamp|
|transactions|block_hash|Hash of the block where this transaction was in|string|
|transactions|block_number|Block number where this transaction was in|integer|
|transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|transactions|from_address|Address of the sender|string|
|transactions|gas|Gas provided by the sender|integer|
|transactions|gas_price|Gas price provided by the sender |float|
|transactions|hash|Hash of the transaction|string|
|transactions|input|The data sent along with the transaction|string|
|transactions|max_fee_per_gas|Total fee that covers both base and priority fees|integer|
|transactions|max_priority_fee_per_gas|Fee given to miners to incentivize them to include the transaction|integer|
|transactions|nonce|The number of transactions made by the sender prior to this one|integer|
|transactions|receipt_contract_address|The contract address created, if the transaction was a contract creation, otherwise null|string|
|transactions|receipt_cumulative_gas_used|The total amount of gas used when this transaction was executed in the block|integer|
|transactions|receipt_effective_gas_price|The actual value per gas deducted from the senders account. Replacement of gas_price after EIP-1559|integer|
|transactions|receipt_gas_used|The amount of gas used by this specific transaction alone|integer|
|transactions|receipt_root|32 bytes of post-transaction stateroot (pre Byzantium)|string|
|transactions|receipt_status|Either 1 (success) or 0 (failure) (post Byzantium)|integer|
|transactions|to_address|Address of the receiver. null when its a contract creation transaction|string|
|transactions|transaction_index|Integer of the transactions index position in the block|integer|
|transactions|transaction_type|Transaction type|integer|
|transactions|value|Value transferred |float|
|wax_actions|account|Account participating in this action|string|
|wax_actions|authorization|The authorization in this action|structural|
|wax_actions|block_hash|Hash of the block|string|
|wax_actions|block_number|Block number where this action was in|integer|
|wax_actions|block_timestamp|Timestamp of the block where this action was in|timestamp|
|wax_actions|data|The data in this action|structural|
|wax_actions|hex_data| Hex of data|string|
|wax_actions|index|Index of action in the same transaction_hash|integer|
|wax_actions|name|The main actor in this action's authorization|string|
|wax_actions|transaction_hash|Hash of the transaction|string|
|wax_token_transfers|block_hash|Hash of the block where this transfer was in|string|
|wax_token_transfers|block_number|Block number where this transfer was in|integer|
|wax_token_transfers|block_timestamp|Timestamp of the block where this transfer was in|timestamp|
|wax_token_transfers|from_address|Address of the sender|string|
|wax_token_transfers|log_index|Log index in the transaction receipt|integer|
|wax_token_transfers|to_address|Address of the receiver|string|
|wax_token_transfers|token_address|ERC20 token address|string|
|wax_token_transfers|transaction_hash|Transaction hash|string|
|wax_token_transfers|value|Amount of tokens transferred (ERC20) / id of the token transferred (ERC721). Use safe_cast for casting to NUMERIC or FLOAT64|string|
|wax_transactions|action_count|Action Count|integer|
|wax_transactions|block_hash|Hash of the block|string|
|wax_transactions|block_number|Block number where this transaction was in|integer|
|wax_transactions|block_timestamp|Timestamp of the block where this transaction was in|timestamp|
|wax_transactions|compression|Compression|string|
|wax_transactions|context_free_data|Context free data|string|
|wax_transactions|cpu_usage_us|Cpu usages of the transaction|integer|
|wax_transactions|deferred|Deferred|bool|
|wax_transactions|delay_sec|Delay sec|integer|
|wax_transactions|expiration|Expiration|timestamp|
|wax_transactions|hash|Hash of the transaction|string|
|wax_transactions|max_cpu_usage_ms|Max cpu usage ms|integer|
|wax_transactions|max_net_usage_words|Max net usage words|integer|
|wax_transactions|net_usage_words|Net usages of the transaction|integer|
|wax_transactions|packed_context_free_data|Packed context free data|string|
|wax_transactions|packed_trx|Packed trx|string|
|wax_transactions|ref_block_num|Ref block num|string|
|wax_transactions|ref_block_prefix|Ref block prefix|string|
|wax_transactions|signatures|Signatures|string|
|wax_transactions|status|Status of the transaction|string|

