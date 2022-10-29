# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime
from hashlib import sha256

from flask_app import secret_key
from models.models import Characters, Users
from models.db_setting import db_session

# Flaskオブジェクトの生成
app = Flask(__name__)

app.secret_key = secret_key.SECRET_KEY


# modelオブジェクトに入っているクエリを全て取得し
# 格納されたデータとhtmlをレンダリングする
@app.route("/")
@app.route("/index")
def index():
    if "user_name" in session:
        name = session["user_name"]
        all_character = Characters.query.all()
        return render_template("index.html", name=name, all_character=all_character)
    else:
        return redirect(url_for("top", status="logout"))


# フォームに値を入力しnameを変更する
@ app.route("/index", methods=["post"])
def submit():
    name = request.form["name"]
    # family = ["ドンキー", "ディディー", "クリッター", "キングクルール"]
    all_character = Characters.query.all()
    return render_template("index.html", name=name, all_character=all_character)


# フロントのフォームで値を受け取りDBに格納しindex()を返す
@ app.route("/add", methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    char = Characters(title, body, datetime.now())
    db_session.add(char)
    db_session.commit()
    return redirect(url_for("index"))


@ app.route("/update", methods=["post"])
def update():
    char = Characters.query.filter_by(id=request.form["update"]).first()
    char.title = request.form["title"]
    char.body = request.form["body"]
    db_session.commit()
    return redirect(url_for("index"))


@ app.route("/delete", methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        char = Characters.query.filter_by(id=id).first()
        db_session.delete(char)
    db_session.commit()
    return redirect(url_for("index"))


@ app.route("/login", methods=["post"])
def login():
    user_name = request.form["user_name"]
    user = Users.query.filter_by(user_name=user_name).first()
    if user:
        password = request.form["password"]
        hashed_password = sha256(
            (user_name + password + secret_key.SALT).encode("utf-8")).hexdigest()
        if user.hashed_password == hashed_password:
            session["user_name"] = user_name
            return redirect(url_for("index"))
        else:
            return redirect(url_for("top", status="wrong_password"))
    else:
        return redirect(url_for("top", status="user_notfound"))


@ app.route("/register", methods=["post"])
def register():
    user_name = request.form["user_name"]
    user = Users.query.filter_by(user_name=user_name).first()
    if user:
        return redirect(url_for("newcomer", status="exist_user"))
    else:
        password = request.form["password"]
        hashed_password = sha256(
            (user_name + password + secret_key.SALT).encode("utf-8")).hexdigest()
        user = Users(user_name, hashed_password)
        db_session.add(user)
        db_session.commit()
        session["user_name"] = user_name
        return redirect(url_for("index"))


@ app.route("/logout")
def logout():
    session.pop("user_name", None)
    return redirect(url_for("top", status="logout"))


@ app.route("/top")
def top():
    status = request.args.get("status")
    return render_template("top.html", status=status)


@ app.route("/newcomer")
def newcomer():
    status = request.args.get("status")
    return render_template("newcomer.html", status=status)


if __name__ == "__main__":
    app.run(debug=True)
