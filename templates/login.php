<!DOCTYPE html>
<html>

<head>
   <title>registration page</title>
   <link rel="stylesheet" type="text/css" href="../static/css/signupcss.css">
   <link rel="stylesheet" href="../static/css/style_sheet.css">
<style>
* {box-sizing: border-box;}
</style>

</head>

<body>
<div class="header">
        <center><img style="margin: 0px 0px 0px 0px;" src="../static/images/logo.png" width="100"></center>
    </div>
    <div class="topnav">
            <a href="home.php">Home</a>
            <a href="about.php">About Us</a>
            <a href="sellogin.php">Seller login</a>
            <a href="signupcust.php">Customer signup</a>&nbsp;&nbsp;
   </div>
<br>
<br>
<div class="al">
            <image src="../static/images/gi2.gif" style="float: center; margin: 0px 50px 150px 90px;" width=500px></image>
        </div>
   <form class="box" action="login.php" method="post">
      <br>
      <br>
      <h1>Login for Customers</h1>

      <input type="text" placeholder="Enter Username" name="username" required>

      <input type="password" name="password" placeholder="Enter Password" class="password" required>

      <input type="submit" name="Login" value="Submit">

   </form>
<div class="footer">
		<p style="color:black; text-align: center;">&#169; HealthCard</p>
	</div>
   </body>

</html>
