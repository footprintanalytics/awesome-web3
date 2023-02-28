## analysis techniques of Footprint Analytics


### table mapping between Dune Analytics and Footprint Analytics



|                |Dune                          |Footprint                         |
|----------------|-------------------------------|-----------------------------|
|nft | nft.trades         | nft.transactions          |
|erc20 transfer | erc20_ethereum.evt_Transfer        | ethereum_token_transfers        |
| event | {project}__evt__{event_name}     | ethereum_decoded_events        |
|price          |prices.usd       | token_price_5min    |
|price          |prices.usd_latest| token_price_5min|

