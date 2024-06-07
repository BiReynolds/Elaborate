from flask import Flask, render_template

import models
from config import Config

app = Flask(__name__)

testContent = models.Content("test","<p>here's my item</p>")

tables = [models.sqlTable("Content",["id","nickname","html"],["INTEGER PRIMARY KEY","TEXT","BLOB"])]
models.init_db(Config.dbPath,tables)

@app.route("/")
def index():
    return render_template("base.html", content = [testContent,testContent,testContent])