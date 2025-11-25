from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import User
from sqlalchemy import or_

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user'] = username
            flash(f"Login successful! {username}", 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash("Invalid username or password", 'danger')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logout Done", "info")
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm', '')

        if not username or not password:
            flash('Username and password are required.', 'danger')
            return render_template('register.html')

        if password != confirm:
            flash('Passwords do not match.', 'danger')
            return render_template('register.html')

        # check for existing username or email
        existing = User.query.filter(or_(User.username == username, User.email == email)).first()
        if existing:
            flash('A user with that username or email already exists.', 'danger')
            return render_template('register.html')

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')