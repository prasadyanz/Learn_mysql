import Database

# get_sectors = Database.get_sectors
# for x in get_sectors:
#     sql = "DROP TABLE "+"sector"+str(x)
#     Database.mycursor.execute(sql)
#     table_name = "sector_"+str(x)
#     sql = "CREATE TABLE "+ table_name + " (subsector varchar(30), type varchar(30))"
#     sql = "ALTER TABLE "+table_name+ " ADD (min_PE int , nominal_PE int, max_PE int)"
#     Database.mycursor.execute(sql)
# Database.mycursor.execute("ALTER TABLE MOAT MODIFY moat VARCHAR(30)")
# Database.db.commit()
#
# get_sectors_with_sub = Database.get_sectors_with_sub
# for y in range(0, len(get_sectors_with_sub)):
#     for x in range(0, len(get_sectors_with_sub[y])):
#         # sql = "delete from {table} where (min_PE) in (10) ".format(table = "sector_"+str(get_sectors_with_sub[y][0]))
#         # sql = "INSERT INTO {table} (subsector, type) VALUE (%s, %s)"
#         # sql = "UPDATE {table} SET (min_PE = 10, nominal_PE = 20, max_PE = 30)".format(table = "sector_"+str(get_sectors_with_sub[y][0]))
#         sql = "UPDATE sector_misc SET min_PE = 10, nominal_PE = 15, max_PE = 20;"
#         print(sql)
#         Database.mycursor.execute(sql)
#         # Database.mycursor.execute(sql, (vals,))
#         Database.db.commit()

"""  Create one table with columns from a list of items """
import Database
get_sectors = Database.get_sectors

table_name = "SECTOR_DATA"
create_stement='create table '+table_name + '('
i=0
while i< len(get_sectors)-1 :
    create_stement =create_stement +get_sectors[i] +' VARCHAR(30),'
    i=i+1

create_stement =create_stement +get_sectors[i] +' VARCHAR(30)'+ ')'

print(create_stement)
Database.mycursor.execute(create_stement)
print('Done')

get_sectors_with_sub = Database.get_sectors_with_sub
max_rows = []
for x in get_sectors_with_sub:
    max_rows.append(len(x))
max_row = max(max_rows)
for x in range(0, max_row):
    print(x)
    for y in range(0, len(get_sectors)):
        if get_sectors_with_sub[y][0] == get_sectors[y]:
            try:
                vals = get_sectors_with_sub[y][x]
            except:
                vals = 'None'
            sql = "INSERT INTO SECTOR_DATA ({}) VALUES (%s) ".format(get_sectors[y])
            print(sql,(vals,))
            Database.mycursor.execute(sql,(vals,))
    Database.db.commit()