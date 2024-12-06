from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Liste pour stocker les tâches
tasks = []

@app.route('/')
def index():
    """Page principale affichant les tâches."""
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Ajouter une tâche à la liste."""
    task = request.form.get('task')
    if task:  # Ajouter seulement si la tâche n'est pas vide
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Supprimer une tâche de la liste."""
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
