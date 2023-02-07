import mysql.connector
import json

configfile = open('config.json')

config = json.load(configfile)

cnx = mysql.connector.connect(user=config['mysqlname'], password=config['mysqlpass'],
                              host='localhost',
                              database='recipeapp')

cursor = cnx.cursor()

cursor.execute('SELECT * FROM recipeapp.testdata;')

for (id, value) in cursor:
  print("{}, {}".format(
    id, value))

cnx.close()
configfile.close()