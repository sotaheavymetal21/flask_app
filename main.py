from flask_app.app import app

from flask import Flask, render_template, request  # Flaskの操作に必要なモジュールをインポート
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String  # DBのテーブルの型をインポート
from sqlalchemy import Column, Integer, String, Text, DateTime
from models.db_setting import Base
from datetime import datetime
if __name__ == "__main__":
    app.run()


# Flaskの立ち上げ

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.sqlite'  # DBへのパス

# SQLAlchemyでデータベース定義

db = SQLAlchemy(app)

# SQLiteのDBテーブル情報


class FLASK_DB(db.Model):
    __tablename__ = 'flask_table'

    ID = db.Column(Integer, primary_key=True)
    YOUR_NAME = db.Column(String(32))
    AGE = db.Column(Integer)


# DBの作成


db.create_all()

# 127.0.0.1:5000に遷移したときの処理


@app.route('/')
def route():
    return render_template('index.html')

# 127.0.0.1/DB_INFO:5000に遷移したときの処理


@app.route('/DB_INFO', methods=['POST', 'GET'])
def book_in_box():
    if request.method == 'POST':
        your_name = request.form['your_name']
        age = request.form['age']
        flask = FLASK_DB(YOUR_NAME=your_name, AGE=age)
        db.session.add(flask)
        db.session.commit()
        db.session.close()
        FLASK_DB_infos = db.session.query(
            FLASK_DB.ID, FLASK_DB.YOUR_NAME, FLASK_DB.AGE).all()
        return render_template('db_info.html', FLASK_DB_infos=FLASKDB_infos)

# python app立ち上げ


if __name__ == '__main__':
    app.run()
