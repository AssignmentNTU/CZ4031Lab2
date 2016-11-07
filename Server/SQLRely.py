import psycopg2



class DatabasePostgresql:


    def __init__(self,dbName,dbUser,dbPassword):
        try:
            self.conn = psycopg2.connect(database=dbName,user=dbUser,password=dbPassword,host="localhost",port=5432)
        except:
            self.conn = None
            print "I am unable to connect to the database"

    def processListOfName(self,listName):
        listNameReturn = []
        for name in listName:
            nameChanges = name.replace("'","''")
            listNameReturn.append(nameChanges)
        return listNameReturn

    def createViewOfTitleFromAllAuthor(self,listAuthorName):
        cur = self.conn.cursor()
        self.listOfAllAuthor = listAuthorName
        author_requirement = ''
        query = ''
        for author_name in listAuthorName:
            author_requirement += 'author_name = '+'\''+author_name+'\''+' OR '
        author_requirement = author_requirement[:-3]
        query = "CREATE OR REPLACE VIEW PUBKEY_FROM_ALL_AUTHOR AS SELECT pubkey,author_name from pubauthor WHERE "+author_requirement+";"
        cur.execute(query)
        self.conn.commit()
        #then query again to get the result and buffer it to the global dictionary to be referred later
        self.checkingDictionary =  {}
        queryFromNewView = "SELECT * FROM PUBKEY_FROM_ALL_AUTHOR"
        try:
            cur.execute(queryFromNewView)
        except:
            print("There has something error during execution")
        self.checkingDictionary = cur.fetchall()


    def createPublicationCompleteView(self):
        cur = self.conn.cursor()
        cur.execute('''CREATE OR REPLACE VIEW PUBLICATION_COMPLETE_VIEW AS SELECT * FROM publication NATURAL JOIN pubauthor;''')
        print "View created successfully"
        self.conn.commit()


    def execute(self):
        cur = self.conn.cursor()
        dictionaryReturn = {}
        queryToGetAllTitle = "select pubkey,a2 from ( select pubkey,author_name as a1 from pubkey_from_all_author ) as p NATURAL JOIN  (select pubkey, author_name as a2 from pubkey_from_all_author) as p2";
        try:
            cur.execute(queryToGetAllTitle)
        except:
            print("There has something error during execution")
        rows = cur.fetchall()
        #will get list of title from here
        for i in rows:
            title = i[0]
            author = i[1]
            if(dictionaryReturn.get(title) == None):
                set_new = set()
                set_new.add(author)
                dictionaryReturn[title] = set_new
            else :
                set_return = dictionaryReturn.get(title)
                set_return.add(author)
                dictionaryReturn[title] = set_return

        dictionary_real_return = {}
        for key in  dictionaryReturn.keys():
            list_added = list(dictionaryReturn.get(key))
            dictionary_real_return[key] = list_added

        return dictionary_real_return


    def closeDatabase(self):
        self.conn.close();
