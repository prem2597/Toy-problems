Task 1 PostgreSQL - Reflection
1. What is the need for Add Ons in Heroku?
Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps. Our platform is elegant, flexible, and easy to use, offering developers the simplest path to getting their apps to market. Heroku add-ons are components that support your application, such as data storage, monitoring, analytics, data processing, and more. These are fully maintained for you by either a third-party provider or by Heroku.

2. What exactly happens when you click on provision while configuring the Postgres addon?
Heroku Connect provides bidirectional synchronization between data and Heroku Postgres, allowing you to unify and share the data in a Heroku Postgres SQL database with contacts, accounts, and other custom objects in a database. Generally, it will connect the data.

3. What is the use of Adminer? How does it work?
Adminer is a tool for managing contents of MySQL databases, formerly known as phpMinAdmin. It's a single tiny PHP file.
 
Task 2 Python and Flask - Reflection

1. How do I manage to use python 3.6 if I already have python 2.7?
As I am a Ubuntu user my system already consists of python 3.7 as I just made python3.6 as the mainstream python language by certain commands.

2. What is the role of pip and how does it work?
Pip stands for “Pip Installs Packages”. Pip is a command-line based package management system. It's used to install and manage software written in the Python language. You can use pip to install packages listed in the Python Package Index (PyPI). The --user flag to pip install tells Pip to install packages in some specific directories within your home directory. This is a good way to have your own default Python environment that adds to the packages within your system directories, and therefore, does not affect the system Python installation.

3. What is the role of requirements.txt and how does it work with pip?
The requirements.txt file contains all the data management instructions setups within and the pip is used to install those setups within the directory for that project. Requirement files give you a way to create an environment: a set of packages that work together. 
pip install -r requirements

4. Which packages are installed and why are they required?
Flask - for dynamic programming
Flask-Session - The session object of the flask package is used to set and get session data. The session object works like a dictionary but it can also keep track modifications. When we use sessions the data is stored in the browser as a cookie. The cookie used to store session data is a known session cookie.
Psycopg2-binary - It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make many concurrent “INSERT” s or “UPDATE” s. Psycopg 2 is mostly implemented in C as a libpq wrapper, resulting in being both efficient and secure.
SQLAlchemy - A benefit many developers enjoy with SQLAlchemy is that it allows them to write Python code in their project to map from the database schema to the applications' Python objects. No SQL is required to create, maintain and query the database. SQLAlchemy is an implementation of the object-relational mapping (ORM) concept.

5. Which environment variables set for Flask to work? What is the purpose of each variable?
    export FLASK_ENV=development - to set the debugger on.
    export FLASK_APP=application.py - to run application.py instead of app.py.

6. What happens when the Flask run command is issued on the terminal?
The flask executable is a simple command-line runner for Flask apps. It simply checks for application.py and executes it.

7. On which port is Flask running and can it be changed?
    In default, it works on 5000
    export FLASK_RUN_PORT=8000
    flask run --port=2000
    

8. How is Flask different from the tiny webserver?
Flask  is not a web server. It is a micro web application framework. That means it is basically a set of tools and libraries that make it easier to build web applications in Python. Flask will include a web server that can be used for testing and development.

Task 3 Goodreads API - Reflection

1. What are the various categories of web APIs available on good reads?
    Authentication, authorization, and browsing.

2. Is there a limit on the use of the web API? What are the limits?
    The actual number of requests made per connection is 6000.
