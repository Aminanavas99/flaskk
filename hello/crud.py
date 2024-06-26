

from flask import *
import sqlite3

app=Flask(__name__)


# @app.route('/reg/')
# def index():
#     return render_template('emp_reg.html')


@app.route('/',methods=['POST','GET'])
def emp_save():
    if request.method=="POST":
        # pass
        name=request.form['fname']
        email=request.form['email']
        ph=request.form['phone']
        with sqlite3.connect("emp.db") as con: #represent the connection object returned by sqlite3.connect().



            mycursor=con.cursor()
            mycursor.execute('''
                  insert into Employee(name,email,phone) values(?,?,?)
                             ''',(name,email,ph))
            con.commit()
            return "<script>window.alert('successfully added!....');window.location.href='/'</script>"

    else:
        return render_template('emp_reg.html')
    


#execute() method, you provide the values for these placeholders as a tuple. 
# This tuple contains the actual values you want to insert into the database
# The purpose of placeholders is to separate the SQL code from the data being provided.
# When you use placeholders,
# you need to provide the values separately when executing the query.

# Parameter Binding: When you execute the SQL query with placeholders,
# you provide the values for those placeholders separately. the values (name, email, ph) 
# are substituted for the placeholders (?,?,?) in the execute() method call. 
# This is done by passing the values as a tuple as the second argument to the execute() method

@app.route('/list/')
def emp_list():
    con=sqlite3.connect('emp.db')
    con.row_factory=sqlite3.Row
    # , it returns rows as dictionary-like objects. 
    # can access column values by their names rather than by index.
    print(con)
    cur=con.cursor()
    cur.execute("select * from Employee")
    rows=cur.fetchall()
    print(rows)

    return render_template('emp_list.html',data=rows)





@app.route('/emp_del/<int:id>')
def emp_del(id):
    con=sqlite3.connect('emp.db')
    cur=con.cursor()
    cur.execute("delete  from Employee where id=?",(id,))
    con.commit()
    print(id)
    # return 'deleted'
    return "<script>window.alert('successfully deleted!....');window.location.href='/list/'</script>"




@app.route('/emp_edit/<int:id>')
def emp_edit(id):
    con = sqlite3.connect('emp.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Employee WHERE id=?", (id,))
    em = cur.fetchone()
    con.commit()  # Don't forget to close the connection after using it

    print(em)  # Debug print statement
    print(id)  # Debug print statement

    return render_template('emp_edit.html', data=em)


    
    
    
    
    
# return 'successfully edited'


@app.route('/emp_update/<int:id>',methods=['POST'])
def emp_update(id):
    if request.method=="POST":
        name=request.form['fname']
        email=request.form['email']
        ph=request.form['phone']
        con=sqlite3.connect('emp.db')
        cur=con.cursor()
       
        cur.execute("UPDATE Employee SET name=?, email=?, phone=? WHERE id=?", (name, email, ph, id))
        con.commit()
        return redirect(url_for('emp_list'))


if __name__ =="__main__":

    app.run(debug=True)
