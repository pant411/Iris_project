<!DOCTYPE html>
<html lang="en">
<head>
  <title>OCR Project</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  
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
    <h1>เรียงตามไฟล์</h1>

    <table class="table table-striped table-hover lastesttable">
    <thead>
        <tr>
        <th scope="col">ไฟล์</th>
        <th scope="col">หัวข้อ</th>
        <th scope="col">ส่งโดย</th>
        <th scope="col">ส่งโดยสังกัด</th>
        <th scope="col">วันที่</th>
        </tr>
    </thead>
    <?php
        $monthconvert = array(
        1 => "มกราคม",
        2 => "กุมภาพันธ์",
        3 => "มีนาคม",
        4 => "เมษายน",
        5 => "พฤษภาคม",
        6 => "มิถุนายน",
        7 => "กรกฎาคม",
        8 => "สิงหาคม",
        9 => "กันยายน",
        10 => "ตุลาคม",
        11 => "พฤศจิกายน",
        12 => "ธันวาคม",
        );
        //echo $lastest_number;
        //$lastest_number = strval($lastest_number);
        $got_trans = "
        SELECT Document.filename AS doc_file, Document.ID AS doc_id, Document.name AS doc_name, Document.day, Document.month, Document.year, Unit.Name AS unit_name, Person.Name AS p_name
        FROM (((Transaction
        INNER JOIN Document ON Transaction.Document_ID = Document.ID)
        INNER JOIN Unit ON Transaction.SenderUnit_ID = Unit.ID)
        INNER JOIN Person ON Transaction.Sender_ID = Person.ID)
        ORDER BY Document.filename
        ";
        //echo $got_trans;
        $result = $conn->query($got_trans);
        if ($result->num_rows > 0) {
            // output data of each row
            echo "<tbody>";
            while($row = $result->fetch_assoc()) {
                $filename = end(explode("/", $row["doc_file"]));
            $id = $row["doc_id"];
            if($row["year"] == 0){
                $year = " ไม่ปรากฏปี";
                }
            else{
                $year = " พ.ศ.".($row["year"] + 543);
            }
            if($row["doc_name"] == NULL){
                $topicname = "ไม่ปรากฏชื่อเรื่อง";
            }
            else{
                $topicname = $row["doc_name"];
            }
            if($row["p_name"] == NULL){
                $sendername = "ไม่พบชื่อผู้ส่ง";
            }
            else{
                $sendername = $row["p_name"];
            }
            if($row["unit_name"] == NULL){
                $senderunitname = "ไม่พบหน่วยงานที่ส่ง";
            }
            else{
                $senderunitname = $row["unit_name"];
            }
            echo "<tr><td>$filename</td><td><a class='doc-topic' href='opendocument.php?id=$id'>". $topicname."</a></td><td>". $sendername."</td><td>". $senderunitname. "</td><td>". $row["day"]." ". $monthconvert[$row["month"]] . $year."</td></tr>";

            //echo "<tr><td>". $row["doc_name"]."</td><td>". $row["p_name"]."</td><td>". $row["unit_name"]. "</td><td>". $row["day"]." ". $monthconvert[$row["month"]] ." พ.ศ.". ($row["year"]+543) ."</td></tr>";
            }
            echo "</tbody>";
        } 
        else {
            echo "<tbody>";
            echo "<tr><td>0 results</td><td></td><td></td><td></td></tr>";
            echo "</tbody>";
        }

        
    ?>
</body>
