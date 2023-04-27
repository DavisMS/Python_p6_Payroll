% rebase('layout.tpl', title='edit hours')

<h2>WXYZ Corp.</h2>

<h3>Find Payroll by Dept.</h3><br>
<p>
<form action='/getDepartment' method='post'>
<label for='department'>Select Department:</label>
<select name='dept'>
    <option value='advertising'>Advertising</option>
    <option value='environment'>Environment</option>
    <option value='maintenance'>Maintenance</option>
    <option value='shipping'>Shipping</option>
</select>
</p>
<p><input type='submit' value='Submit'></p>
