<?php
    include 'component/auth.php';
?>
<?php
    include 'component/sqlconnectuser.php';  
    if(isset($_POST["submit"])){
        //echo "hi";
        //echo md5($_POST["pwd"]);
        //echo $_POST["name"];
        //echo $_POST["email"];
        $name = $_POST["name"];
        $newpass = $_POST["newpwd"];
        $errword = '';
        //$oldname = $_COOKIE["username"];
        $oldpass = md5($_POST["oldpwd"]);
        $userid = $_COOKIE["userid"];
        $sqli = "SELECT ID FROM user_auth WHERE User_ID = $userid AND Password = '$oldpass'";
        $resulti = $conn->query($sqli);
        if($resulti->num_rows == 1){
            //echo "update newname";
            $sqlup = "UPDATE user_data SET Name='$name' WHERE ID=$userid";
            if ($conn->query($sqlup) === TRUE) {
                echo "เปลี่ยนชื่อสำเร็จ";
                /*if(isset($_COOKIE["userid"])) {
                    setcookie("userid", "", time() - 3600, '/');  
                    unset($_COOKIE['userid']);
                    //setcookie("username", $name, time() + (86400 * 7), "/");
                } 
            
                if(isset($_COOKIE["username"])) {
                    setcookie("username", "", time() - 3600, '/');  
                    unset($_COOKIE['username']);
                    //setcookie("userid", $userid, time() + (86400 * 7), "/");
                } */
                //echo $name;
                //setcookie("username", $name, time() + (86400 * 7), "/");
                //setcookie("username", $name);
                //echo $_COOKIE["username"];
                //setcookie("userid", $userid, time() + (86400 * 7), "/");
                //setcookie("userid", $userid);
                if($newpass != ""){
                    $mdnewpass = md5($newpass);
                    $sqlp = "UPDATE user_auth SET Password='$mdnewpass' WHERE User_ID=$userid";
                    if ($conn->query($sqlp) === TRUE) {
                        $errword = "เปลี่ยนรหัสผ่านสำเร็จ";
                        header('Location: ./editprofile.php');
                    } 
                    else {
                        $errword = "เกิดข้อผิดพลาดในการเปลี่ยนรหัส";
                        //$sqlupr = "UPDATE user_data SET Name='$oldname' WHERE ID=$userid";
                        //if ($conn->query($sqlup) === TRUE) {
                            //setcookie("username", $oldname, time() + (86400 * 7), "/");
                            //setcookie("userid", $userid, time() + (86400 * 7), "/");
                        //}
                    }
                }
                else{
                    //echo "notchange password";
                    header('Location: ./editprofile.php');
                }
                
            } 
            else {
                $errword = "เกิดข้อผิดพลาดในการเปลี่ยนชื่อ";
            }
        }
        else{
            $errword = "รหัสผ่านผิดกรุณาลองใหม่";
        }
    }
    
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
<?php
    
          
    $userid = $_COOKIE["userid"];
    //$username = $_COOKIE["username"];
?>
<body>
    <?php
        include 'component/navbar.php';
    ?>
    <div class="lastestbox">
        <h2>แก้ไขบัญชี</h2>
        <form action="<?php echo $_SERVER["PHP_SELF"]; ?>" method="post">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" class="form-control" id="name" placeholder="Enter Name" name="name" value="<?php echo $navusername; ?>">
            </div>
            <div class="form-group">
                <label for="pwd">New Password (หากไม่ต้องการเปลี่ยนรหัสให้เว้นช่องไว้): </label>
                <input type="password" class="form-control" id="pwd" placeholder="Enter new password" name="newpwd">
            </div>
            <div class="form-group">
                <label for="pwd">Old Password: </label>
                <input type="password" class="form-control" id="pwd" placeholder="Enter old password" name="oldpwd">
            </div>
            <p class="errmsg"><?php echo $errword; ?></p>
            <button type="submit" name="submit" class="btn btn-block btn-primary">แก้ไขบัญชี</button>
        </form>
    </div>
</body>

