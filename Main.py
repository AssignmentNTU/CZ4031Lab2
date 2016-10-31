from Server import PostgresqlDB

#listName is the inserted name that you want to search the relation in between
listName = ["A-Young Cho","A Lun"]
db = PostgresqlDB.DatabasePostgresql("db","postgres","1234567890")
db.execute(listName)