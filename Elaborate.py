import sqlite3
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm,CSRFProtect

import models
from forms import ContentForm
from config import Config

## Various setups
app = Flask(__name__)
app.secret_key = Config.secretKey
csrf = CSRFProtect(app)

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

@app.route("/admin")
def admin():
    pass

@app.route("/admin/add", methods = ['GET','POST'])
def adminAdd():
    form = ContentForm()
    message = ""
    if form.validate_on_submit():
        name = form.nickname.data
        html = form.html.data
        sql = "INSERT INTO Content(nickname,html) VALUES ('"+name+"', '"+html+"');"
        print(sql)
        con = sqlite3.connect(Config.dbPath)
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
        con.close()
        return redirect( url_for('index') )
    return render_template("addContent.html",form=form)