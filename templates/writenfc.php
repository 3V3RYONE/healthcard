<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Write into NFC</title>
    <link rel="stylesheet" href="../static/css/style_sheet.css">
</head>
<body>
		<div class="header">
			<center><img style="margin: 0px 0px 0px 0px;" src="../static/images/logo.png" width="100"></center>
		</div>
		
		<div class="topnav">
		</div>


    <br>
    <center>
    <div class="column">
        <h2 style="color:#273478">NFC Writer</h2>
          <form method="post" action="writenfc.php" enctype="multipart/form-data">
          
              <label for="firstname">First Name: &nbsp;&nbsp;</label>
              <input type="text" id="firstname" name="firstname" required></br><br><br>

              <label for="lastname">Last Name: &nbsp;&nbsp;</label> 
              <input type="text" id="lastname" name="lastname" required></br><br><br>

               <label for="username">Username :</label>
              <input type="text" id="username" name="username" required><br><br><br>

              <label for="password">Password :</label>
              <input type="text" id="password" name="password" required><br><br><br>

              <label for="email">email :</label>
              <input type="text" id="email" name="email" required><br><br><br>

              <label for="mobno">Mobile Number :</label>
              <input type="text" id="mobno" name="mobno" required><br><br><br>
               
              <label for="address">Address :</label>
              <input type="text" id="address" name="address" required><br><br><br>

              <label for="emergencyContact">Emergency Contact</label>
              <input type="text" id="emergencyContact" name="emergencyContact" required><br><br><br>

              <label for="medicalHistory">Medical History: </label>
              <input type="text" id="medicalHistory" name="medicalHistory" required><br><br><br>

              <label for="age">Age :</label>
              <input type="text" id="age" name="age" required><br><br><br>

              <label for="gender">Gender :</label>
              <input type="text" id="gender" name="gender" required><br><br><br>

              <label for="aadharNo">Aadhar Number :</label>
              <input type="text" id="aadharNo" name="aadharNo" required><br><br><br>

              <input type="submit" name="submit" id="submit" value="Update HealthCard">
              </form>   
    </div>
</center>

</body>
</html>
