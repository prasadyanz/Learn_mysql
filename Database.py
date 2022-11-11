

# import SQL_Connect_PI as SQ
import SQL_Connect_PC as SQ
db = SQ.connection
mycursor = SQ.mycursor
#####################     Table   STOCK_DATA      ########################################################
mycursor.execute("SELECT * FROM STOCK_DATA")
myresult = mycursor.fetchall()
get_status = []
get_watch_list = []
get_stocks_in_watchlist =[]

for x in myresult:
    get_status.append(x[9])
    get_watch_list.append(x[10])
    if x[10] == 'Yes':
        get_stocks_in_watchlist.append(x[0])
    else:
        pass

get_status = sorted(list(set(get_status)))
get_watch_list = list(set(get_watch_list))
get_stocks_in_watchlist = sorted((list(get_stocks_in_watchlist)))

##############################     Table  for SECTOR    ########################
get_sectors = []
mycursor.execute("SELECT * FROM SECTOR")
myresult = mycursor.fetchall()
for x in myresult:
    get_sectors.append(x[0])
get_sectors = sorted(list(set(get_sectors)))

get_sectors_with_sub=[]
get_subsector = []
mycursor.execute("SELECT * FROM STOCK_DATA")
myresult = mycursor.fetchall()
for y in get_sectors:
    temp = [y]
    for x in myresult:
        if x[2] == y:
            get_subsector.append(x[3])
            temp.append(x[3])
        else:
            pass
    temp_2 =[]
    [temp_2.append(w) for w in temp if w not in temp_2]
    get_sectors_with_sub.append(temp_2)

# for z in get_sectors_with_sub:
#     print(z)


get_moat = []
mycursor.execute("SELECT * FROM MOAT")
myresult = mycursor.fetchall()
for x in myresult:
    get_moat.append(x[0])
get_moat = sorted(list(set(get_moat)))

get_risk = []
mycursor.execute("SELECT * FROM RISK")
myresult = mycursor.fetchall()
for x in myresult:
    get_risk.append(x[0])
get_risk = sorted(list(set(get_risk)))
# for x in get_risk:
#     print(x)

###########################        Table for Current_PF     ##########################
get_pf = []
mycursor.execute("SELECT * FROM Current_PF")
myresult = mycursor.fetchall()
for x in myresult:
    get_pf.append(x)
get_pf = list(set(get_pf))

