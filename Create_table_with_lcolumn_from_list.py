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