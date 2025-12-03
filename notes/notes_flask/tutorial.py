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
    return render_template("contact.html")

@app.route("/<name>")
def user (name):
    return f"<h1>Hello {name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)

#1. What does Flask do?
#access the library that allows multi page website
#2. What are the steps to setting up a Flask project?
#from flask import Flask
#app = Flask(__name__)
#@app.route("/")
#def home():
#    return "<h1>Flask web</h1>"
    #if __name__ == "__main__":
 #       app.run(debug=True)
#set up a folder in python
#3. How can you reference subpages on your Flask project? (Meaning the difference between the home page and a personal profile)
#if __name__ == "__main__":
#        app.run(debug=True)

#4. What are templates?
#Allows you to make a full web page with html tags
