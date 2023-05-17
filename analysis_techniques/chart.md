# About how to make a chart in Footprint


1.  ***How to make a field filter in a chart***
 To make a field filter in a chart, follow these steps:

  - Open the SQL editor page in your chart.
  - In the SQL query, use the syntax `[[ and {{field_name}}]]` to create a filter for a specific field in your data. For example, if you wanted to filter on a field called "country", you would add `[[ and {{country}}]]` to your WHERE clause.
  - Save the changes to your SQL query and run the chart.
  - On the chart page, you should now see a filter for the field you specified in step 2. Click on the filter to open the filter box.
  - In the filter box, you can select one or more values for the field. The chart will be automatically updated to display only the data that matches your filter selection.
  - To make the filter optional, use `[[ ]]` instead of `[[ and {{field_name}}]]` in your SQL query. This will display the filter box but allow the user to select "All" to show all data.
  - [footprint link](https://www.footprint.network/chart/39952?editingOnLoad=true)
  
  ![field filter](https://user-images.githubusercontent.com/44665855/236614620-d1f647a2-7592-425c-8221-d2eb71c0e7d1.gif)
  
2. ***How to set a chart link***

 - **Save the chart.**
 - **Choose the field that you want to add a clickable link to.**
 - **Select "Link" as the display type.**
 - **Paste the link you want to redirect to into the "Link URL" text box {{variable}}.**
 [footprint link](https://www.footprint.network/@0xAlina/Game-Ranking)
 
![set link](https://github.com/footprintanalytics/awesome-web3/assets/44665855/5e4ba597-665d-43a2-9437-56d6ebb38e17)

3. ***How to do dashboard association filtering***
 - Click created
 - Select New Dashboard
 - Click Add chart, paste the completed chart id into the search box and click the corresponding chart
 - Click Add a filter and select Text or Category, and select Dropdown
 - Select the chart that needs to be associated
 - [footprint link](https://www.footprint.network/@Higi/zkSync-Airdrop-Checker?address=0x38c5e0f95b08b663602ec23223e7c0695d30410e)
 ![2023-05-17 18 44 10](https://github.com/footprintanalytics/awesome-web3/assets/44665855/66295e18-adf5-49eb-ba9a-d5448c917330)
