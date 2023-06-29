# Product
### product description
1. Footprint Analytics is a data platform blending web2 and web3 data with abstractions. We help analysts, builders, and investors turn blockchain data into insights with accessible visualization tools and a powerful multi-chain API across 20+ chains for NFTs, GameFi, and DeFi. We also provide Footprint Growth Analytics to help with effective growth in GameFi and any web3 projects.
Disclaimer: All data and articles on Footprint Analytics are for informational purposes only, and do not constitute any investment advice.

### Documentation link
### The following is the basic documentation of footprint,
- This document can help you use footprint analytics, link: [footprint analytics docs](https://docs.footprint.network/docs) 
- This document can clearly see the areas, chains, platforms, and contracts covered by the footprint in this link: [Footprint-Data-Overview](https://www.footprint.network/@Footprint/Footprint-Data-Overview) 
-  Data API entry link : [footprint analytics Data API](https://www.footprint.network/data-api) 
-  history published article link: [Footprint analytics article](https://www.footprint.network/news/articles)
-  This document can help you better understand the role of each table in footprint analytics link: [Footprint-Datasets-Data-Dictionary](https://www.footprint.network/@Footprint/Footprint-Datasets-Data-Dictionary) 
-  Footprint website link: [Website](https://www.footprint.network)
-  Footprint analytics Pricing page link: [Pricing](https://www.footprint.network/pricing)
-  Footprint analytics Discord link: [Discord](https://discord.com/invite/3HYaR6USM7)
-  Footprint analytics telegram link: [Telegram](https://t.me/joinchat/4-ocuURAr2thODFh)
-  Footprint analytics twitter link: [Twitter](https://twitter.com/Footprint_Data)
-  Footprint analytics can be contacted at partners@footprint.network
-  @lesley8964 is a colleague in charge of the market. For market-related cooperation, you can contact DM@lesley8964. @jimmytf is in charge of business cooperation. For related cooperation, you can DM @jimmytf. @Hige#3602 is technical support. For data-related issues, you can directly contact him


### Home page
### This is the new page link of Footprint Analytics https://www.footprint.network/news/all, on this page you can see the articles and reports published by Footprint Analytics history and some usage tutorials
1. Here are some video tutorials on Footprint Analytics link :[Footprint Analytics video tutorials](https://www.footprint.network/news/academy?category=academy&subMenu=Footprint%20Analytics%20Tutorials) 
2. This link is a common statement for querying Trino sql and some common index examples,link: [Common Trino SQL examples ](https://www.footprint.network/news/academy?category=academy&subMenu=Footprint%20for%20SQL)
3. Footprint analytics historical article display page link : [Footprint analytics article](https://www.footprint.network/news/articles) 
4. Footprint analytics historical report display page link :  [Footprint analytics historical report](https://www.footprint.network/news/reports) 

## Data frame history
### The data lake is introduced, which is a new type of structured and unstructured data storage. The data lake is very suitable for the storage of data on the chain, because the data on the chain has a wide range of formats, from unstructured raw data to Structured abstract data are the highlights of Footprint Analytics.The footprint uses Trino as the underlying database
Iceberg can be very well integrated with calculation engines such as Spark, Flink, Trino, etc. We can choose the most suitable calculation method for each of our indicators, and choose Spark;
For real-time computing, choose Flink;
StarRocks - Simple ETL tasks that can be done using SQL, choose Trino.
The current footprint analytics platform has iterated three versions, from Bigquery to OLAP to the current Iceberg + Trino, and now uses the syntax of trino
The underlying database for footprint analysis uses trino + Iceberge. If you need to write sql, you need trino's [Trino Docs](https://trino.io/docs/current/functions.html) syntax to query data

