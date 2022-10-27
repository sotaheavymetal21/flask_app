# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template, request
from datetime import datetime

from models.models import Characters
from models.db_setting import db_session

# Flaskオブジェクトの生成
app = Flask(__name__)


# modelオブジェクトに入っているクエリを全て取得し
# 格納されたデータとhtmlをレンダリングする
@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    all_character = Characters.query.all()
    # family = ["ドンキー", "ディディー", "クリッター", "キングクルール"]
    return render_template("index.html", name=name, all_character=all_character)


# フォームに値を入力しnameを変更する
@app.route("/index", methods=["post"])
def submit():
    name = request.form["name"]
    # family = ["ドンキー", "ディディー", "クリッター", "キングクルール"]
    all_character = Characters.query.all()
    return render_template("index.html", name=name, all_character=all_character)


# フロントのフォームで値を受け取りDBに格納しindex()を返す
@app.route("/add", methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    char = Characters(title, body, datetime.now())
    db_session.add(char)
    db_session.commit()
    return index()


if __name__ == "__main__":
    app.run(debug=True)
