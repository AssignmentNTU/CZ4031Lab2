from Server import SQLRely
# from GUI import MainGUI


#listName is the inserted name that you want to search the relation in between
listName = ["B. O. Fagginger Auer","Rob H. Bisseling"]
# db = PostgresqlDB.DatabasePostgresql("db","postgres","1234567890")
# db.createPublicationCompleteView()
# #process list name first
# listNameReturn = db.processListOfName(listName)
# result = db.execute(listNameReturn)
# print (result)
# db.closeDatabase()
#run the GUI
# MainGUI.MainApp.run()
db = SQLRely.DatabasePostgresql("db","postgres","1234567890")
listReturn = db.processListOfName(listName)
db.createViewOfTitleFromAllAuthor(listReturn)
db.execute()