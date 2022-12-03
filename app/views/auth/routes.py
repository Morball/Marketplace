from flask import render_template, request, redirect, url_for, flash, session, jsonify
from app import app
from werkzeug.security import generate_password_hash
from app.models.models import User,db
from datetime import datetime
from app.util.util import validate_username,login_required, create_breadcrumb
#create a login view
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html", breadcrumb=create_breadcrumb(request.path))
    elif request.method=='POST':
        if "username" not in session:
            username=request.form['username']
            password=request.form['password']
            if username and password:
                user=User.query.filter_by(username=username, password=generate_password_hash(password)).first()
                if user:
                    session['username']=username
                    session["role"]=user.role
                    user.last_login=datetime.now()
                    db.session.commit()
                    return redirect(url_for('home'))
                else:
                    flash('Invalid username or password', 'danger')
                    return redirect(url_for('login'))
            else:
                flash('Please enter a username and password', 'danger')
                return redirect(url_for('login'))
        else:
            flash('You are already logged in.', 'danger')
            return redirect(url_for('home'))

#create a logout view
@login_required
@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        flash('You have been logged out.', 'success')
        return redirect(url_for('login'))
    else:
        flash('You are not logged in.', 'danger')
        return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html", breadcrumb=create_breadcrumb(request.path))
    elif request.method=='POST':
        if "username" not in session:
            username=request.form['username']
            if username:
                if username.length<=3 or username.length>=20:
                    if validate_username(username):
                        if password and password_confirm:
                            password=request.form['password']
                            password_confirm=request.form['password_confirm']
                            if password==password_confirm:
                                user=User.query.filter_by(username=username).first()
                                if user:
                                    flash('Username already exists.', 'danger')
                                    return redirect(url_for('register'))
                                else:
                                    user=User(username=username, password=generate_password_hash(password), role=request.form['role'])
                                    db.session.add(user)
                                    db.session.commit()
                                    session['username']=username
                                    session['role']='user'
                                    return redirect(url_for('home'))
                            else:
                                flash('Passwords do not match.', 'danger')
                                return redirect(url_for('register'))
                        else:
                            flash('Please enter a password.', 'danger')
                            return redirect(url_for('register'))
                    else:
                        flash('Invalid username.', 'danger')
                        return redirect(url_for('register'))
                else:
                    flash('Username must be between 3 and 20 characters.', 'danger')
                    return redirect(url_for('register'))
            else:
                flash('Please enter a username.', 'danger')
                return redirect(url_for('register'))
        else:
            flash('You are already logged in.', 'danger')
            return redirect(url_for('home'))
