import pymysql

# database information
user_db = ''
pass_db = ''
host_db = ''
port_db = 3306
name_db = ''

# connecting server database Jakarta to pythons
db = pymysql.connect(user=user_db,password=pass_db,host=host_db,port=port_db,database=name_db)