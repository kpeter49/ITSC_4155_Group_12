# ITSC_4155_Group_12

## Setup

Create a file in the root directory called 'config.json' with the following data:

`{
    "mysqlname" : "SQL_USERNAME",
    "mysqlpass" : "SQL_PASSWORD"
}`

Replace the text, SQL_USERNAME and SQL_PASSWORD, with the login credentials for your local mysql instance

The directory called DatabaseDump contains a backup of all of the tables in the database used for testing and demos for this project. They can be imported using the data import/restore tool in MySQL Workbench.


## Running the app

Use 'pip install -r requirements.txt' to install the necessary packages. If new packages are added, run 'pip freeze > requirements.txt' to update the requirements file.

To run the django project, run the command 'python manage.py runserver' from the './recipeapp' directory

To run unit tests, run the command 'python manage.py test'

If there is an error with migrations, use the command 'python manage.py migrate' to resolve them.