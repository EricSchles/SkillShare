from app import app, db
from flask import request, render_template,redirect, url_for
import json
from app.models import Users

#This is going to be the splash page
@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index2.html")


# Sign Up Route
@app.route("/sign-up",methods=["GET","POST"])
def sign_up():
    """
    Takes in username and password and creates new user in the database

    # Inputs:
    #     - @param username: string field
    #     - @param password: string field, currently no validations (12.3.2016)
    # Outputs:
    #     - None
    """
    if request.method=="POST":
        
        print(type(request.form))
        username = request.form.get("username")
        password = request.form.get("password_field")
        if len(Users.query.filter_by(username=username).all()) == 0:
            user = Users(username=username,password=password)
            db.session.add(user)
            db.session.commit()
            print(username,password)
            return redirect(url_for("sign_in"))
        else:
            return render_template("sign_up.html",error="username already exists, please choose another")
    return render_template("sign_up.html")

@app.route("/sign-in",methods=["GET","POST"])
def sign_in():
    """
    Takes in username and password and checks to see in the database

    # Inputs:
    #     - @param username: string field
    #     - @param password: string field, currently no validations (12.3.2016)
    # Outputs:
    #     - None
    """
    if request.method=="POST":
        
        print(type(request.form))
        username = request.form.get("username")
        password = request.form.get("password_field")
        result = Users.query.filter_by(username=username).all()
        if len(result) == 0:
            return render_template("sign_in.html",error="does not exist")
        elif result[0].password != password:
            return render_template("sign_in.html",error="wrong password")
        else:
            return redirect(url_for("review_an_article"))
    return render_template("sign_in.html")

@app.route("/review_an_article",methods=["GET","POST"])
def review_an_article():
    #form template: https://v4-alpha.getbootstrap.com/components/forms/
    if request.method == "POST":
        #put stuff here to save to DB
        #should be in status ready for review after submitted
        return redirect(url_for("thanks"))
    return render_template("review_an_article.html")



# Postgres documentation for Python: https://github.com/EricSchles/postgres_flask_macosx
