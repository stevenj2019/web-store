from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application.models import Admin
from application.forms import AdminLoginForm, AdminForm, ResetPasswordForm
from application import app

@app.route('/admin', methods=['GET', 'POST'])
def adm_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
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
    return render_template('adminhome.html', title = "Dashboard", month = month_revenue, annual = annual_revenue)

#@login_required
@app.route('/new-admin')
def adm_new_admin():
    form = AdminForm()
    roles = (['admin', 'admin'])
    #if Admin.query.filter_by(user_id = current_user.user_id).first().level == 'owner':
        #roles.append(['owner', 'owner'])
    if form.validate_on_submit():
        Data = Admin(first_name = form.first_name.data, last_name = form.last_name.data, email = form.email.data, password = bcrypt.generate_password_has(form.password.data), level = form.level.data)
        #db.session.add(Data)
        #db.session.commit()
        return redirect(url_for('adm_home'))
    else:
        print(form.errors)
    return render_template('adminform.html', form = form, title = "New Admin", form_title ="Create a New Admin User")

@app.route('reset-password')
def adm_password_reset():
    form = ResetPasswordForm()
    admin = Admin.query.filter_by(id=current_user.id).first()
    if form.validate_on_submit():
        if admin and bcrypt.check_password_hash(admin.password, form.old_password.data):
            admin.password = bcrypt.generate_password_hash(form.new_password.data)
            db.session.commit()
        else:
            form.errors.append('incorrect password supplied')
    else:
        print(form.errors)
    return render_template('resetpassword.html', form = form, title="Reset Password")

#@login_required
@app.route('/logout')
def adm_logout():
    logout_user()
    return redirect(url_for('adm_login'))