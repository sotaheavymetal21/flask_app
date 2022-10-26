# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from flask import Flask, render_template, request

# Flaskオブジェクトの生成
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    family = ["ドンキー", "ディディー", "クリッター", "キングクルール"]
    return render_template("index.html", name=name, family=family)


@app.route("/index", methods=["post"])
def submit():
    name = request.form["name"]
    family = ["ドンキー", "ディディー", "クリッター", "キングクルール"]
    return render_template("index.html", name=name, family=family)


if __name__ == "__main__":
    app.run(debug=True)
