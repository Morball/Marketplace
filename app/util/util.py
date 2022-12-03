from functools import wraps
from flask import session,redirect,url_for,flash
from app import breadcrumbs_alias

#create a username_validation function
def validate_username(username):
    if username.contains(' ') or username.contains('/') or username.contains('?') or username.contains('=')  or username.contains(' ') or username.contains('#') or username.contains('$') or username.contains('%') or username.contains('&') or username.contains('*') or username.contains('(') or username.contains(')') or username.contains('+') or username.contains('-') or username.endswith('.') or username.contains('@') or username.contains('[') or username.contains(']') or username.contains('^') or username.contains('`') or username.contains('{') or username.contains('|') or username.contains('}') or username.contains('~'):
        return False
    else:
        return True
        
#create a login_required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'username' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.', 'danger')
            return redirect(url_for('login'))
    return wrap


#create a admin_required decorator
@login_required
def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['role'] == 'admin':
            return f(*args, **kwargs)
        else:
            flash('You need to be an admin to access this page.', 'danger')
            return redirect(url_for('home'))
    return wrap

#create a moderator_required decorator
@login_required
def moderator_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['role'] == 'moderator':
            return f(*args, **kwargs)
        else:
            flash('You need to be a moderator to access this page.', 'danger')
            return redirect(url_for('home'))
    return wrap



#create a vendor_required decorator
@login_required
def vendor_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['role'] == 'vendor':
            return f(*args, **kwargs)
        else:
            flash('You need to be a vendor to access this page.', 'danger')
            return redirect(url_for('home'))
    return wrap

 
 
 
def create_breadcrumb(requestRoute):
    breadcrumbs_array=requestRoute.split('/')[1:]
    breadcrumbs_final_list=[]
    if breadcrumbs_array is not None:
        for elem in breadcrumbs_array:
            if elem in breadcrumbs_alias and elem!='':
                breadcrumbs_final_list.append(breadcrumbs_alias[elem])
            else:
                breadcrumbs_final_list.append(elem)
        return breadcrumbs_final_list
  