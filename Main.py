from Server import SQLRely
from datetime import datetime

no_author = 2
author_list_full = ["George Giakkoupis", "Maryam Helmi", "Lisa Higham", "Philipp Woelfel", "Jalal Kawash", "Abhijeet Pareek Pareek", "Dan Alistarh", "James Aspnes"]
author_list = author_list_full[:no_author]

database = SQLRely.DatabasePostgresql("dblp_half", "postgres", "postgres",host="localhost",port=5432)
#Mark starting time
start_time = datetime.now()
#need to create view first
database.createPublicationCompleteView()
print(author_list)
author_list_returned = database.processListOfName(author_list)
database.createViewOfTitleFromAllAuthor(author_list_returned)
result_dict = database.execute()
end_time = datetime.now()
execution_time = end_time - start_time
print("Execution time took " + str(execution_time.total_seconds()) + " seconds.")