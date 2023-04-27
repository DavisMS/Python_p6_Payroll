<h2> Payroll Application </h2><br>

<h3> Program Description: </h3><br>
<p>The Payroll Application is the final programming assignment for my Python II course. It requires using Python, a web framework called Bottle, and the CSS framework Bootstrap to create a web application that connects to and queries a local SQLite database (payroll). The program then allows the user to view employee information in the database according to department choice and update an employee's working hours given the employee's ID.</p><br>

<h3>Program Walkthrough:</h3><br>

<p>When the web application is executed, it will run on the designated localhost and assumes the user is already validated 
by logging in and takes you to the welcome page. Here navigation for the rest of the application is possible:</p>

![Welcome](https://user-images.githubusercontent.com/124637405/234785321-11ae31dc-79e4-4bdc-8ac9-1230f549c9cc.png) <br>

<p> I can access employee payroll information by By clicking <i>"View by Department,"</i> choosing an option from the drop-down 
menu, and clicking submit to query the database:</p>

![ViewByDept](https://user-images.githubusercontent.com/124637405/234789041-861aee09-ef22-47dd-a03e-fb0c9729b19f.png) <br>

<p>After the query is submitted and processed, a new page is returned with the relevant information, in this case, 
the employee payroll for the advertising department:</p>

![DeptView](https://user-images.githubusercontent.com/124637405/234786368-6ee4d422-32af-41e3-9eef-46c9c43f2bc6.png) <br>

<p>Now if I want to change or update the hours worked by an employee, I will click <i>"Edit Employee Data"</i> and provide the 
ID of an employee along with a new set of hours worked to replace or update the current set, which should also change their pay:</p>

![UpdateDataEntry](https://user-images.githubusercontent.com/124637405/234787357-825b1a74-c707-4692-b4b2-5a72d27904c4.png) <br>

<p>If successful, the application will return who has been updated, their ID, name, and department:</p>

![UpdateSuccess](https://user-images.githubusercontent.com/124637405/234787651-b913da0c-81a5-4a6b-84e0-e6a9b8f55c67.png) <br>

<p>Finally, I will return to the <i>"View by Department"</i> section to verify the hours worked and pay for Hanna in advertising were changed from 40 to 32:</p>

![UpdatedDeptView](https://user-images.githubusercontent.com/124637405/234787960-e9eb8f26-1bab-4639-a1b7-645bbccc7518.png) <br>

