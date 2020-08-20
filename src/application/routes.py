from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application.models import Admin
from application.forms import AdminLoginForm
from application import app

@app.route('/admin', methods=['GET', 'POST'])
def adm_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('adm-home'))
        else:
            print(form.errors)
    return render_template('adminlogin.html', form=form)
#@login_required
@app.route('/adm-home')
def adm_home():
    month_revenue = 0
    annual_revenue = 0
    return render_template('adminhome.html', month = month_revenue, annual = annual_revenue)
#@login_required
@app.route('/new-item')
def adm_new_item():
    return render_template('')
