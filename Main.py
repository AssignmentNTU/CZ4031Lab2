from Server import PostgresqlDB
#listName is the inserted name that you want to search the relation in between
listName = ["B. O. Fagginger Auer","Rob H. Bisseling"]
db = PostgresqlDB.DatabasePostgresql("db","postgres","1234567890")
#process list name first
listNameReturn = db.processListOfName(listName)
result = db.execute(listNameReturn)
print(result)
# db.getListTitleForParticularAuthor(name="''Maseka Lesaoana",test=True)
# dataMock = {"title1":["edward","sujono"],"title2":["sujono"]}