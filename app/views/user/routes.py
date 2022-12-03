from app import app
from app.models.models import User,db
from flask import Flask,request,render_template,redirect,url_for,flash,session



@app.route("/user/<username>", methods=['GET', 'POST'])
def user(username):
    if not username:
        flash("Invalid username", "danger")
        return redirect(url_for('home'))
    user=User.query.filter_by(username=username).first()
    if not user:
        flash("User not found",'danger')
        return redirect(url_for('home'))
    if request.method == 'GET':
            return render_template("user.html", user=user)