TodoApp
  TodoApp is a web application built with Flask, a Python backend framework, and Bootstrap for the frontend. It utilizes a MySQL database to store tasks and implements CRUD (Create, Read, Update, Delete) 
  operations to manage tasks effectively.

Features
  CRUD Operations: Users can easily create, read, update, and delete tasks.
  Bootstrap Frontend: The frontend is designed using Bootstrap, providing a responsive and user-friendly interface.
  MySQL Database: Tasks are stored in a MySQL database, ensuring data persistence and reliability.
  Automatic Deletion: Utilizes database events to automatically delete completed tasks when users mark them as completed.

Requirements.txt
  Falsk
  flask_mysqldb
  schedule


To use TodoApp, follow these steps:
  Clone the repository to your local machine.
  Install the necessary dependencies by running pip install -r requirements.txt.
  Set up a MySQL database and update the configuration in config.py.
  Run python app.py to start the application.
  Access the application in your web browser at http://localhost:5000.
  
  Future Improvements
    Add user authentication and authorization.
    Implement task categorization and prioritization features.
    Improve UI/UX for a more polished user experience.
