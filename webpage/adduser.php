<?php
    include 'component/auth.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <title>เพิ่มผู้ใช้ในระบบ</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="component/css/index.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>

<body>
    <?php
            include 'component/navbar.php';
            
    ?>
    <div class="lastestbox">
        <h2>เพิ่มผู้ใช้ในระบบ</h2>
        <form action="<?php echo $_SERVER["PHP_SELF"]; ?>" method="post">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" class="form-control" id="name" placeholder="Enter Name" name="name">
            </div>
            <div class="form-group">
                <label for="email">E-mail:</label>
                <input type="email" class="form-control" id="email" placeholder="Enter email" name="email">
            </div>
            <div class="form-group">
                <label for="pwd">Password: </label>
                <input type="password" class="form-control" id="pwd" placeholder="Enter password" name="pwd">
            </div>
            <button type="submit" name="submit" class="btn btn-block btn-primary">เพิ่มผู้ใช้ในระบบ</button>
        </form>
    </div>
</body>

<?php

    include 'component/sqlconnectuser.php';
    if(isset($_POST["submit"])){
        //echo "hi";
        //echo md5($_POST["pwd"]);
        //echo $_POST["name"];
        //echo $_POST["email"];
        $name = $_POST["name"];
        $email = $_POST["email"];
        $pass = md5($_POST["pwd"]);
        $userid = $_COOKIE["userid"];
        $sql = "INSERT INTO user_data (Email, Name, Add_by)
                VALUES ('$email', '$name', $userid)";

        if ($conn->query($sql) === TRUE) {
            $last_id = $conn->insert_id;
            //echo "New record created successfully. Last inserted ID is: " . $last_id;
            $sqlp = "INSERT INTO user_auth (User_ID, Password)
                    VALUES ($last_id, '$pass')";
            if ($conn->query($sqlp) === TRUE) {
                echo "success";
            }
            else{
                $sqld = "DELETE FROM user_data WHERE id=$last_id";

                if ($conn->query($sqld) === TRUE) {
                    echo "Error End";
                } 
                else {
                    echo "Error deleting record: " . $conn->error;
                }
            }

        } 
        else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }

    $conn->close();
        
    }
?>