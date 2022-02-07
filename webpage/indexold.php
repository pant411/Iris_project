<!DOCTYPE html>
<html lang="en">
<head>
  <title>OCR Project</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <link rel="stylesheet" href="component/css/index.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
    <?php
        include 'component/navbar.php';
        include 'component/sqlconnect.php';
    ?>
    <div class="indexsearchbox">
      <?php
          include 'component/searchbox.php';
      ?>
    </div>
    <div class="lastestbox">
      <?php
          $lastest_number = 5;
          include 'component/lastest.php';
          
      ?>
      <a class="moredoc" href="alldocument.php">ดูเอกสารทั้งหมด</a>
    </div>


</body>