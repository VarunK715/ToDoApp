from flask import Flask, render_template, request ,redirect ,url_for
from flask_mysqldb import MySQL
import time
import schedule
from datetime import datetime, timedelta


app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todoapp'

# Create MySQL instance
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        task = request.form['task']
        # Insert data into the database
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO tododocs(task) VALUES(%s)", (task,))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('home_page'))  # Redirect to the index page after adding task
    
    # Fetch data from the database
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tododocs")
    data = cursor.fetchall()
    count = len(data)

    #  # Count completed tasks
    cursor.execute("SELECT COUNT(*) FROM tododocs WHERE completed=1")
    completed_count = cursor.fetchone()[0]
    cursor.close()
    
    return render_template('index.html', count=count,completed_count=completed_count, data=data)


@app.route('/checkbox', methods=['POST'])
def checkbox():
    if request.method == 'POST':
        # Get the list of completed tasks from the form
        completed_tasks = request.form.getlist('completed')
        
        # Update the completed field in the database for each completed task
        cursor = mysql.connection.cursor()
        current_time = int(time.time())
        for task_id in completed_tasks:
            cursor.execute("UPDATE tododocs SET completed = 1 WHERE id = %s", (task_id,))
        mysql.connection.commit()  # Commit the transaction
        cursor.close()

        # Redirect the user to the home page after the update
        return redirect(url_for('home_page'))

    # If the request method is not POST, redirect to the home page
    return redirect(url_for('home_page'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    try:
        # Fetch the existing task name from the database
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT task FROM tododocs WHERE id = %s", (id,))
        data = cursor.fetchone()
        cursor.close()

        if not data:
            return "Task not found", 404

        if request.method == 'POST':
            taskName = request.form['taskname']
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE tododocs SET task = %s WHERE id = %s", (taskName,  id))
            mysql.connection.commit()
            cursor.close()

            return redirect(url_for('home_page'))

        # Render the update form with the existing task name
        return render_template('update.html', taskId=id, taskName=data[0])

    except Exception as e:
        return str(e), 500

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM tododocs WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('home_page'))  # Redirect to the index page after deleting task



if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)