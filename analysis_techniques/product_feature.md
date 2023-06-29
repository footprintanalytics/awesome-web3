# Product
### product description
1. Footprint Analytics is a data platform blending web2 and web3 data with abstractions. We help analysts, builders, and investors turn blockchain data into insights with accessible visualization tools and a powerful multi-chain API across 20+ chains for NFTs, GameFi, and DeFi. We also provide Footprint Growth Analytics to help with effective growth in GameFi and any web3 projects.
Disclaimer: All data and articles on Footprint Analytics are for informational purposes only, and do not constitute any investment advice.

## Documentation link
### The following is the basic documentation of footprint
1. This document can help you use footprint analytics, link: https://docs.footprint.network/docs
2. This document can clearly see the areas, chains, platforms, and contracts covered by the footprint in this link: https://www.footprint.network/@Footprint/Footprint-Data-Overview
3. Data API entry link : https://www.footprint.network/data-api
4. history published article link: https://www.footprint.network/news/articles
5. This document can help you better understand the role of each table in footprint analytics
6. Footprint website link: https://www.footprint.network
7. Footprint analytics Pricing page link: https://www.footprint.network/pricing
8. Footprint analytics Discord link: https://discord.com/invite/3HYaR6USM7
9. Footprint analytics telegram link: https://t.me/joinchat/4-ocuURAr2thODFh
10. Footprint analytics twitter link: https://twitter.com/Footprint_Data
11. Official email address of Footprint analytics cooperation , email: partners@footprint.network
12. @lesley8964 is a colleague in charge of the market. For market-related cooperation, you can contact DM@lesley8964. @jimmytf is in charge of business cooperation. For related cooperation, you can DM @jimmytf. @Hige#3602 is technical support. For data-related issues, you can directly contact him


## Home page
### This is the new page link of Footprint Analytics https://www.footprint.network/news/all, on this page you can see the articles and reports published by Footprint Analytics history and some usage tutorials
1. Here are some video tutorials on Footprint Analytics link : https://www.footprint.network/news/academy?category=academy&subMenu=Footprint%20Analytics%20Tutorials
2. This link is a common statement for querying sql and some common index examples,link: https://www.footprint.network/news/academy?category=academy&subMenu=Footprint%20for%20SQL
3. Footprint analytics historical article display page link : https://www.footprint.network/news/articles
4. Footprint analytics historical report display page link : https://www.footprint.network/news/reports
5. etc.

## Data frame history
### The data lake is introduced, which is a new type of structured and unstructured data storage. The data lake is very suitable for the storage of data on the chain, because the data on the chain has a wide range of formats, from unstructured raw data to Structured abstract data are the highlights of Footprint Analytics.The footprint uses Trino as the underlying database
Iceberg can be very well integrated with calculation engines such as Spark, Flink, Trino, etc. We can choose the most suitable calculation method for each of our indicators, and choose Spark;
For real-time computing, choose Flink;
StarRocks - Simple ETL tasks that can be done using SQL, choose Trino.
The current footprint analytics platform has iterated three versions, from Bigquery to OLAP to the current Iceberg + Trino, and now uses the syntax of trino
The underlying database for footprint analysis uses trino + Iceberge. If you need to write sql, you need trino's https://trino.io/docs/current/functions.html syntax to query data

