import pymysql

# database information
user_db = 'jsms'
pass_db = 'JSMSpass'
host_db = '149.129.233.76'
port_db = 3307
name_db = 'mydepojavapjn'

# connecting server database Jakarta to pythons
db = pymysql.connect(user=user_db,password=pass_db,host=host_db,port=port_db,database=name_db)