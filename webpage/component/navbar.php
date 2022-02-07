
<?php
  include 'component/sqlconnectuser.php';
  $navuserid = $_COOKIE["userid"];
  //echo $navuserid;
  $navsqlname = "SELECT Name FROM user_data WHERE ID = '$navuserid'";
  $navresult = $conn->query($navsqlname);
  if($navresult->num_rows == 1){
    while($row = $navresult->fetch_assoc()) {
        //echo $row;
        $navusername = $row["Name"];
    }
  }
  else{
    //echo "not found";
  }
  $conn->close();
?>
<nav class="navbar fixed-top navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="index.php">OCR Project</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav w-100">
            <li class="nav-item">
              <a class="nav-link" href="index.php">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="allsortbyname.php">ENG Debug</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="adduser.php">เพิ่มผู้ใช้ในระบบ</a>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled" href="#">แก้ไขข้อมูลบุคคลในระบบเอกสาร</a>
            </li>
            <li class="nav-item">
              <a class="nav-link disabled" href="#">แก้ไขข้อมูลองค์กรในระบบเอกสาร</a>
            </li>
            <li class="nav-item dropdown ml-auto">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> <?php echo "สวัสดี ". $navusername;?> </a>
                <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownMenuLink">
                    <a class="dropdown-item" href="editprofile.php">แก้ไขบัญชี</a>
                    <a class="dropdown-item" href="logout.php">ออกจากระบบ</a>
                </div>
            </li>
        </ul>
    </div>
</nav>