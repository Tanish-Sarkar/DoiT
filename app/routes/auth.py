from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

## MAKE IT FULL FLEGHED LOGIN

USER_CRENDENTIALS = {
    'username' : 'admin',
    'password' : '1234'
}

@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CRENDENTIALS['username'] and password == USER_CRENDENTIALS['password']:
            session['user'] = username
            flash(f"Login Successfull! {username}", 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash("Invalid username or password", 'danger')
            

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logout Done", "info")
    return redirect(url_for('auth.login'))