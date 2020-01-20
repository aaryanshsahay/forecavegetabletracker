# forecavegetabletracker
This is a code which pulls the mrp from bigbasket.com and compares it to the price of the csv file and displays which is charging more/less.

The csv file contains 3 columns, vegetable , rates and URL
vegetable contains the list of the vegetables,rates contains the prices of the vegetables and URL contains the url of the vegetables extracted from bigbasket.com.

You can create a similiar type of csv file,modify the names and the code according to your needs.

This code contains 2 main parts, the first is accepting only the mrp from the url(using beautiful soup) and the other is comparing the values and creating a dataframe with an index(using pandas).

