import sqlite3,os

class sqlTable():
    def __init__(self,name,colNames,colParams):
        self.name = name 
        self.colNames = colNames
        self.colParams = colParams

class Content():
    def __init__(self,nickname,html):
        self.id = 0
        self.nickname = nickname 
        self.html = html

    def loadResults(queryResult):
        result = []
        for row in queryResult:
            newContent = Content(row[1],row[2])
            newContent.id = row[0]
            result.append(newContent)
        return result


def init_db(dbPath,tables):
    if os.path.isfile(dbPath):
        return
    con = sqlite3.connect(dbPath)
    cur = con.cursor()
    
    for table in tables:
        sql = "CREATE TABLE "+table.name+"("
        for i,col in enumerate(table.colNames):
            sql+=col+" "+table.colParams[i]+", "
        sql = sql[:-2]+")"
        print(sql)
        cur.execute(sql)
    con.commit()
    con.close()