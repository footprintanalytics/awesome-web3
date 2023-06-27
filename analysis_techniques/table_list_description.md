### The following table data records the field, level, and description of each table
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
| nft_transactions_v1                    | nft               | silver | This table contains the information of the NFT sales transactions traded only on marketplaces included in FP (90% marketplace has included). It includes: ERC1155 , ERC721 included in the nft_contract_info table, some ERC20. |
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
| ethereum_dune_address_label            | label             | sliver |                                                              |
| entity_tag                             | label             | silver | This table shows tag for entity.                             |
| ethereum_flipside_address_label        | label             | sliver |                                                              |
| gamefi_protocol_daily_stats            | gamefi            | gold   | This table can be used to analyze the daily indicators (e.g. transaction volume, transaction number, transaction user number) of the GameFi. |
| token_price_5min                       | export_chain_data | silver |                                                              |
| logs                                   | export_chain_data | bronze |                                                              |
| transactions                           | export_chain_data | bronze | This table contains a set of all transactions from all blocks, and contains a block identifier to get associated block-specific information associated with each transaction. |
| blocks                                 | export_chain_data | bronze | This table contains a set of all blocks in the blockchain and their attributes. |
| token_transfers                        | export_chain_data | bronze |                                                              |
| traces                                 | export_chain_data | bronze | This table contains a set of all traces in blocks, Represents the function call path that can track the transaction, More detail https://openethereum.github.io/JSONRPC-trace-module. |
| contract_abi_info                      | export_chain_data | silver |                                                              |
| wax_token_transfers                    | chain_data        | bronze | Contains the subset of token_transfer event's transactions and has further processed and denormalized the data to make it easier to consume for analysis of token transfer events. |
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

