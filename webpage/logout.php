<?php
    if(isset($_COOKIE["userid"])) {
        setcookie("userid", "", time() - 3600, '/');  
        unset($_COOKIE['userid']);
        
    } 

    if(isset($_COOKIE["username"])) {
        setcookie("username", "", time() - 3600, '/');  
        unset($_COOKIE['username']);
        
    } 

    header( "refresh: 2; url=login.php" );
    exit(0);
?>