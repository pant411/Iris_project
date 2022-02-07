<?php
  $servername = "localhost:3306";
  $username = "ppunn";
  $password = "ppunn-password";
  $dbname = "ppunn_ocr_database"; //"ppunn_Document";
  $conn = new mysqli($servername, $username, $password, $dbname);
  // Check connection
  if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
  }
?>