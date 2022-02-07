<?php
    $gets = "";
    foreach($_GET as $gkey => $value)
    {
       $gets = "$gets&$gkey=$value";
    }
    $myself = $_SERVER["PHP_SELF"];
    if(!isset($_COOKIE["userid"])) {
        header( "refresh: 2; url=login.php?from=$myself$gets" );
        exit(0);
    } 
    else {
        //echo "hello: " . $_COOKIE["userid"];
    }
?>