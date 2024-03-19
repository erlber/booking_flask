from flask import Flask, render_template, request

app = Flask(__name__)

bruker = {"userName": "erlber", "password": "qwerty"}

@app.route("/")
def start():
    return render_template("index.html")


@app.route("/login_page")
def login_page():
    return render_template("login_page.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["pw"]
        if name == bruker["userName"] and password == bruker["password"]:
            return render_template("start.html")
        else:
            return render_template("index.html")
        

if __name__ == "__main__":
    app.run(debug=True)