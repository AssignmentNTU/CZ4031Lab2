from Server import PostgresqlDB
#listName is the inserted name that you want to search the relation in between
listName = ["A'-Young Cho","A Lun","A.-Ning Bai"]
db = PostgresqlDB.DatabasePostgresql("db","postgres","1234567890")
#process list name first
listNameReturn = db.processListOfName(listName)
db.execute(listNameReturn)
# db.getListTitleForParticularAuthor(name="''Maseka Lesaoana",test=True)