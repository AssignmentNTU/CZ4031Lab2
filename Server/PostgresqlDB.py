import psycopg2
#option 2 using PyGreSql

class DatabasePostgresql:


    def __init__(self,dbName,dbUser,dbPassword):
        try:
            self.conn = psycopg2.connect(database=dbName,user=dbUser,password=dbPassword,host="localhost",port=5432)
        except:
            print "I am unable to connect to the database"

    def processListOfName(self,listName):
        listNameReturn = []
        for name in listName:
            nameChanges = name.replace("'","''")
            listNameReturn.append(nameChanges)
        return listNameReturn

    #listName is all the author name that you want to search the relation on
    def execute(self,listName):
        savedDictionary = {}
        returnDictionary = {}
        for name in listName:
            savedDictionary[name] = self.getListTitleForParticularAuthor(name,test=False)

        for i in range(2,len(listName)+1):
            self.fillTheDictionary(i,listName,savedDictionary)

        #then need to create dictionary with title as it's key
        for key in savedDictionary.keys():
            listName = key.split("|")
            listTitleNow = set(savedDictionary[key])
            for title in listTitleNow:
                listNameToBeSaved = set()
                if(returnDictionary.get(title) != None ):
                    listNameToBeSaved = returnDictionary.get(title)
                for name in listName:
                    listNameToBeSaved.add(name)
                returnDictionary[title] = listNameToBeSaved
        return returnDictionary



    def fillTheDictionary(self,r,listName,savedDictionary):
        n = len(listName)
        listNameAdded = [None]*n
        startIndex = 0
        current = 0
        arraySaved = []
        self.searchCombination(n, r, listName, listNameAdded, startIndex, current, arraySaved)
        for i in range(len(arraySaved)):
            key = ""
            for j in range(len(arraySaved[i])):
                key += arraySaved[i][j] + "|"
            key = key[0:len(key) - 1]
            listName = self.getKeyName(key)
            first = listName[0]
            second = listName[1]
            savedDictionary[key] = set(savedDictionary[first]).intersection(set(savedDictionary[second]))


    def getKeyName(self,nameCombi):
        #edward.sujono
        listCombination = nameCombi.split("|")
        first = ""
        second = ""
        if(len(listCombination) <= 2):
            first = listCombination[0]
            second = listCombination[1]
            answer = [first, second]
            return answer
        for i in range(len(listCombination)-1):
            name = listCombination[i]
            first += (name+"|")
        first = first[0:len(first)-1]
        second = listCombination[len(listCombination)-2]+"|"+listCombination[len(listCombination)-1]

        answer = [first,second]
        return answer;


    def getListTitleForParticularAuthor(self,name,test):
        listToBeSaved = []
        cur = self.conn.cursor()
        query = "SELECT title FROM PUBLICATION_COMPLETE_VIEW where author_name ="+"\'"+name+"\'"
        try:
            cur.execute(query)
        except:
            print("There has something error during execution")
        #put it into array of string
        rows = cur.fetchall()
        for i in rows:
            listToBeSaved.append(i[0])
            if(test):
                print("data: "+i[0])
        return listToBeSaved


    def searchCombination(self,n,r,listName,listNameAdded,startIndex,current,arraySaved):
        if(current == r):
            list = []
            for i in range(0,r):
                data = listNameAdded[i]
                list.append(data)
            arraySaved.append(list)
            return;

        for i in range(startIndex,n):
            listNameAdded[current] = listName[i]
            self.searchCombination(n,r,listName,listNameAdded,i+1,current+1,arraySaved)