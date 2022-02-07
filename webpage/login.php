<?php
    $gets = "";
    $getc = 0;
    $link = "";
    foreach($_GET as $key => $value)
    {
      if($key!="from"){
        
        if($getc > 0){
          $gets = "$gets&$key=$value";
        }
        else{
          $gets = "?$key=$value";
        }
        $link = "$link&$key=$value";
        $getc++;
      } 
      else{
        $link = "?$key=$value";
      }
    }
    $from = $_GET["from"];
    if($from==NULL){
      $from = "index.php";
    }
    else{
      $from = $from.$gets;
    }
    //echo $from;
    if(isset($_COOKIE["userid"])) {
        header( "refresh: 2; url=$from" );
        exit(0);
    } 
    else {
        //echo "hello: " . $_COOKIE["userid"];
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <title>Login</title>
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
<div class="loginbox">
  <div class="container">
    <h2 class="loginlabel">เข้าสู่ระบบ</h2>
    <form action="<?php echo $_SERVER["PHP_SELF"].$link; ?>" method="post">
      <input type="hidden" id="link" value="<?php echo $from;?>"/> 
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" class="form-control" id="email" placeholder="Enter email" name="email">
      </div>
      <div class="form-group">
        <label for="pwd">Password:</label>
        <input type="password" class="form-control" id="pwd" placeholder="Enter password" name="pswd">
      </div>
      <?php /*<div class="form-group form-check">
        <label class="form-check-label">
          <input class="form-check-input" type="checkbox" name="remember"> Remember me
        </label>
      </div>*/?>
      <button type="submit" name="submit" class="lbutton btn btn-block btn-primary">Submit</button>
    </form>
  </div>

</div>


</body>
</html>

<?php
    include 'component/sqlconnectuser.php';
    if(isset($_POST["submit"])){
        $email = $_POST["email"];
        //$link = $_POST["link"];
        $pass = md5($_POST["pswd"]);
        $sql = "SELECT ID, Name FROM user_data WHERE Email = '$email'";
        $result = $conn->query($sql);
        if($result->num_rows == 1){
            while($row = $result->fetch_assoc()) {
                $name = $row["Name"];
                $id = $row["ID"];
            }
            $sqli = "SELECT ID FROM user_auth WHERE User_ID = $id AND Password = '$pass'";
            $resulti = $conn->query($sqli);
            if($resulti->num_rows == 1){
                //echo "สวัสดี" . $name ;
                //setcookie("username", $name, time() + (86400 * 7), "/");
                setcookie("userid", $id, time() + (86400 * 7), "/");
                header( "refresh: 2; url=$from" );
                exit(0);  
            }
            else{
                echo "รหัสผ่านผิดกรุณาลองใหม่";
            }
        }   
        else{
            echo "ไม่พบอีเมลดังกล่าว";
        }
    }
?>