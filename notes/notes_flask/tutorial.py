#RV Flask Notes

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")

@app.route("/contact")
def contact():
    return "<p>Don't contact me. I don't like you man.</p>"

@app.route("/<name>")
def user (name):
    return f"<h1>Hello {name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)

#What does Flask do?
#access the library that allows multi page website
#What are the steps to setting up a Flask project?
#set up a folder in python
#How can you reference subpages on your Flask project? (Meaning the difference between the home page and a personal profile)

#What are templates?
#outside html can impport int the webpage