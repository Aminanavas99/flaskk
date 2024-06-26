# -----------------------------ORM-----------------------------------
#  pip install  flask_sqlalchemy
 
# flask_sqlalchemy-ORM TOOL establishes the relationship between the objects and the tables of the
#  realational db. 

# SQLAlchemy provides an ORM (Object-Relational Mapping) tool that allows you to interact with the
# database using Python objects instead of writing raw SQL queries.



from flask import *
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///emp1.sqlite3'

# universal resource identifier(URI)
# sets the database URI for SQLAlchemy. The database URI tells SQLAlchemy where to find the database.
# In this case,  specified a SQLite database named emp.sqlite3

app.config['SECRET_KEY']='abc'

# The secret key is used to secure session cookies and other cryptographic operations in Flask. 
# It's essential for security purposes, such as preventing cross-site request forgery (CSRF) attacks.
db=SQLAlchemy(app)



class Employee(db.Model):
    id=db.Column('employee_id',db.Integer, primary_key=True)
    name=db.Column(db.String(20))
    address=db.Column(db.String(20))

    def __init__(self,name,address):
        self.name=name
        self.address=address

@app.route('/',methods=['GET','POST'])
def add_emp():
    # when the form is submitted
    if request.method=="POST":
        em=Employee(request.form['name'],request.form['address'])
        db.session.add(em)
        # When you create a new SQLAlchemy session (db.session in your code),
        # you can perform various operations on database objects within that session, 
        # such as adding new objects, updating existing objects, or deleting objects.
        db.session.commit()
        return redirect(url_for('display'))

    else:
        return render_template('add.html')


@app.route('/view')
def display():
    return render_template('listemp.html',emp=Employee.query.all())
#  represents a query object associated with the Employee model, and .all() 
# executes the query and returns all the results.
#  for Object-oriented querying:




if __name__ =="__main__":

    #  This condition checks if the script is being executed directly by the Python interpreter.
    #  When you run your Flask application using python your_script.py,
    #  __name__ is set to "__main__". This condition ensures that the code inside 
    #  the block is only executed when the script is run directly

    with app.app_context():
 # This creates a Flask application context. It's required to access certain Flask features
        # within the "with" block, such as the database.

        db.create_all()

  # This line creates all the database tables defined in the models. It's used to create
        # the database schema based on  model classes.
        
        app.run(debug=True)

#  starts the Flask development server with debugging enabled.





# db.session in SQLAlchemy:
# In SQLAlchemy, db.session refers to the database session. It's a concept used to manage 
# interactions with the database, including transactions, querying, and data manipulation.
# This db.session is not related to server-side sessions for storing user data between requests.
# When you use db.session in SQLAlchemy, you're working with a unit of work that represents 
# a set of database operations, such as adding, updating, or deleting records.
# Server-side Sessions in Flask:
# Flask provides a mechanism for managing user sessions, called server-side sessions.
# Server-side sessions are used to store user-specific data between HTTP requests.
# For example, you can use sessions to keep a user logged in across multiple requests.
# Flask manages server-side sessions using a session management interface, typically provided 
# by a Flask extension such as Flask-Session or Flask-Login.
# Server-side sessions are distinct from database sessions used in SQLAlchemy.