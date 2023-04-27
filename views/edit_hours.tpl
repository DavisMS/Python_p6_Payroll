% rebase('layout.tpl', title='edit hours')

<h2> WXYZ Corp.</h2>

<h3>Please enter eid and hours worked</h3><br>

<form action="/editHours" method="post">

    <p><input type="text" name="eid" placeholder="eid" style="margin-right:1%">Employee ID</p><br>

    <p><input type="text" name="hrs" placeholder="hours" style="margin-right:1%">Enter Hours Worked</p><br>

    <input type="submit" value="Submit">

</form>
