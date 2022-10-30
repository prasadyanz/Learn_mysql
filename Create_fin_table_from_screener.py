""" trying to get the finance data to DB Tables   """
import Get_financial_screener
import time

heading_type = ["profit-loss", "balance-sheet", "cash-flow","ratios"]
stock_name = "LT"
temp = []
for x in heading_type:
    temp_data = Get_financial_screener.get_details(stock_name,x,"Consolidated", "Sales")
    temp.append(temp_data)
    time.sleep(5)
heading_name = []
for x in temp:
    print(stock_name +"_"+x[0][0])
    temp = []
    print(x)
    for y in range(0, len(x)):
        table_name = stock_name +"_"+x[y][0]
        temp.append(x[y][2])
    print(temp)

    # print(table_name, heading_name, x[y][3])

