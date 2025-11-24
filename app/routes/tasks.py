from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app import db
from app.models import Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    tasks = Task.query.all()
    return render_template('tasks.html', tasks = tasks)

@tasks_bp.route('/add', methods = ['POST'])
def add_task():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status='Pending')
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully", "success")

    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status == 'Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear/<int:task_id>', methods = ['POST'])
def clear_tasks(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash("Task removed", 'info')
    return redirect(url_for('tasks.view_tasks'))


@tasks_bp.route('/clear_all', methods=['POST'])
def clear_all():
    Task.query.delete()
    db.session.commit()
    flash("All tasks cleared", 'info')
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/update/<int:task_id>', methods=['POST', 'GET'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if request.method == 'POST':
        new_task = request.form.get('task')
        task.title = new_task
        db.session.commit() 
        flash("Task updated successfully", "success")
        return redirect(url_for('tasks.view_tasks'))
    return render_template('update_task.html', task=task)
