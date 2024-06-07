import sqlite3
from flask import Flask, render_template

import models
from config import Config

app = Flask(__name__)

def testPull():
    sql = "SELECT * FROM Content"
    con = sqlite3.connect(Config.dbPath)
    cur = con.cursor()
    cur.execute(sql)
    queryResult = cur.fetchall()
    print(queryResult)
    print(type(queryResult))
    con.close()
    return queryResult


tables = [models.sqlTable("Content",["id","nickname","html"],["INTEGER PRIMARY KEY","TEXT","BLOB"])]
models.init_db(Config.dbPath,tables)

@app.route("/")
def index():
    return render_template("base.html", content = models.Content.loadResults(testPull()))