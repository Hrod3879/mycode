from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

# Setting up the path to the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))
# Path for where the database is located: project directory
database_file = "sqlite:///{}".format(os.path.join(project_dir, "myDB.db"))

app = Flask(__name__)
# Force the app to use the path created
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

# This isnt a regular class but a data base model
class Expense(db.Model):
    # Define Table
    id = db.Column(db.Integer, primary_key=True) # Create a primary key
    date = db.Column(db.String(50), nullable=False) # Variable string with up to 50 chars and no empty field accepted null
    expensename = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Integer, nullable=False) # Use INT
    category = db.Column(db.String(50), nullable=False)
       
@app.route('/')
def add():
    return render_template('add.html')

# Route for deleting an expense uses both the post and delete methods; first we query and use the class to identify ID
@app.route('/delete/<int:id>', methods=['POST', 'DELETE'])
def delete(id):
    expense = Expense.query.filter_by(id=id).first()
    db.session.delete(expense)
    db.session.commit()
    return redirect('/expenses')

# route for updating entries, use the line from above to query by id and create a new html page
@app.route('/updateexpense/<int:id>')
def updateexpense(id):
    expense = Expense.query.filter_by(id=id).first()
    return render_template('updateexpense.html', expense=expense)

# retrive the id and variables from the hidden id in updateexpense in order to update data base with new values
@app.route('/edit', methods=['POST'])
def edit():
    id = request.form['id']
    date = request.form['date']
    expensename = request.form['expensename']
    amount = request.form['amount']
    category = request.form['category']
    
    expense = Expense.query.filter_by(id=id).first()
    expense.date = date
    expense.expensename = expensename
    expense.amount = amount
    expense.category = category
    db.session.commit()
    return redirect('/expenses')
    

# Route to expenses or Home Page
@app.route('/expenses')
def expenses():
    # retrieves all of the objects store in DB table, mapping data store in DB tables to app code
    expenses = Expense.query.all()
    return render_template('expenses.html', expenses=expenses)

# Build a route to /addexpense, then grabs the data from the 'add.html' form and assigns it to variables
@app.route('/addexpense',methods=['POST'])
def addexpense():
    date = request.form['date']
    expensename = request.form['expensename']
    amount = request.form['amount']
    category = request.form['category']
    print(date +' '+ expensename +' '+ amount +' '+ category)
    
    # How i explained it: First date(in class Expense) = date(in functon addexpense) and so on. New Expense object and populate it with form data
    expense = Expense(date=date, expensename=expensename, amount=amount, category=category)
    
    # Add the new expense object to the sessionsqmycode/Week 2/Week 2 Project/env
    
    db.session.add(expense)
    
    # Commit the changes to the database
    db.session.commit()
    
    # Redirect to the 'expenses' route to display the updated list of expenses
    return redirect('/expenses')

if __name__ == '__main__':
    # Use to create a table from class Expense(db.Model) one time use
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)