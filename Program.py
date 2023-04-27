import sqlite3
from bottle import route, run, request, template

@route('/', method='GET') # Default Route
def index():
    return template('welcome')


@route('/getDepartment', method = ['GET', 'POST'] ) # Employees by Department
def department():
    if request.method=='GET':
        return template('dept_form')
    else:
        dept = request.forms.get("dept")
        con = sqlite3.connect("payroll.db")
        cur = con.cursor()

        sql = '''SELECT pay_data.emp_id, emp_name, wage, hrs_worked 
                    FROM employees
                        JOIN pay_data
                            WHERE pay_data.emp_id = employees.emp_id 
                                AND employees.department = ?'''
        cur.execute(sql, (dept,))

        rows = cur.fetchall()
        cur.close()
        hrs = 0
        wage = 0

        if rows:

            dataList = []
            for row in rows:
                eid, name, wage, hrs = row
                if hrs <= 40:
                    payout = wage * hrs
                else:
                    ot_pay = (hrs - 40) * 1.5 * wage
                    payout = (wage * 40) + ot_pay

                emp = (eid, name, wage, hrs, payout)
                dataList.append(emp)

            data = {'rows': dataList, 'dept': dept}
            return template('show_department', data)
        
        else:
            msg = 'no such username'



@route('/editHours', method = ['GET', 'POST'] ) # Edit/Update Employee Hours
def edit_hours():
    if request.method == 'GET':
        return template('edit_hours')
    else:
        hrs = request.forms.get('hrs')
        eid = request.forms.get('eid')

        try:
            con = sqlite3.connect("payroll.db")
            cur = con.cursor()

            sql = '''SELECT employees.emp_id, emp_name, department FROM employees WHERE emp_id = ?'''
            cur.execute(sql, (eid,))
            result = cur.fetchone()

            emp_id = result[0]
            emp_name = result[1]
            dept = result[2]

            updateSQL = '''UPDATE pay_data SET hrs_worked = ? WHERE emp_id = ?'''
            cur.execute(updateSQL, (hrs, eid))
            if result:
                con.commit()  # Commit updated Information
                cur.close()
                return template('get_employee', {'emp_id': emp_id, 'emp_name': emp_name, 'dept': dept, 'hrs': hrs}) # Verify Update Occured
        except:
            msg = 'Employee does not exist'
        finally:
            cur.close()


 
run(host='localhost', port=8081) # Run application on localhost:8081