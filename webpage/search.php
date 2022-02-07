<?php
    include 'component/auth.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <title>OCR Project</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <link rel="stylesheet" href="component/css/search.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.3/css/jquery.dataTables.css">
  <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.js"></script>
  <script src="component/tables.js"></script>
</head>
<body>
    <?php
        include 'component/navbar.php';
        include 'component/sqlconnect.php';
        $typeconvert = array(
            "all" => "ทั้งหมด",
            "topic" => "หัวข้อ",
            "person" => "บุคคล",
            "organize" => "องค์กร",
        );
        $key = $_GET["keyword"];
        $type = $_GET["type"];
    ?>
    <div class="resultlab">
        <?php
            include 'component/searchbox.php';
        ?>
    </div>
    <div class="resultlab">  
        <h2>ผลลัพธ์การค้นหาของ <?php echo $_GET["keyword"];?> ที่เกี่ยวข้องกับ <?php echo $typeconvert[$_GET["type"]]?></h2>  
        <table id="alldocument" class="table table-striped table-hover lastesttable">
        <thead>
            <tr>
            <th scope="col">หัวข้อ</th>
            <th scope="col">ส่งโดย</th>
            <th scope="col">ส่งโดยสังกัด</th>
            <th scope="col">วันที่</th>
            </tr>
        </thead>
        <?php
            
            $monthconvert = array(
                1 => "1/",
                2 => "2/",
                3 => "3/",
                4 => "4/",
                5 => "5/",
                6 => "6/",
                7 => "7/",
                8 => "8/",
                9 => "9/",
                10 => "10/",
                11 => "11/",
                12 => "12/",
            );
            //echo $lastest_number;
            //$lastest_number = strval($lastest_number);
            //$result = [];
            if($_GET["type"]==="all"){
                $got_trans = "
                SELECT DISTINCT Document.ID AS doc_id, Document.name AS doc_name, Document.day, Document.month, Document.year, Unit.Name AS unit_name, Person.Name AS p_name
                FROM ((((Keyword
                INNER JOIN Document ON Keyword.Document_ID = Document.ID)
                INNER JOIN Transaction ON Transaction.Document_ID = Keyword.Document_ID)
                INNER JOIN Unit ON Transaction.SenderUnit_ID = Unit.ID)
                INNER JOIN Person ON Transaction.Sender_ID = Person.ID)
                WHERE Keyword.tag LIKE '%$key%'
                ORDER BY Document.year DESC, Document.month DESC, Document.day DESC";
                
                //echo $got_trans;
                $result = $conn->query($got_trans);
            }
            elseif($_GET["type"]==="topic"){
                $got_trans = "
                SELECT DISTINCT Document.ID AS doc_id, Document.name AS doc_name, Document.day, Document.month, Document.year, Unit.Name AS unit_name, Person.Name AS p_name
                FROM ((((Keyword
                INNER JOIN Document ON Keyword.Document_ID = Document.ID)
                INNER JOIN Transaction ON Transaction.Document_ID = Keyword.Document_ID)
                INNER JOIN Unit ON Transaction.SenderUnit_ID = Unit.ID)
                INNER JOIN Person ON Transaction.Sender_ID = Person.ID)
                WHERE Keyword.tag LIKE '%$key%' AND Keyword.word = 'Topic'
                ORDER BY Document.year DESC, Document.month DESC, Document.day DESC";
                
                //echo $got_trans;
                $result = $conn->query($got_trans);
            }
            elseif($_GET["type"]==="person"){
                $got_trans = "
                SELECT DISTINCT Document.ID AS doc_id, Document.name AS doc_name, Document.day, Document.month, Document.year, Unit.Name AS unit_name, Person.Name AS p_name
                FROM ((((Keyword
                INNER JOIN Document ON Keyword.Document_ID = Document.ID)
                INNER JOIN Transaction ON Transaction.Document_ID = Keyword.Document_ID)
                INNER JOIN Unit ON Transaction.SenderUnit_ID = Unit.ID)
                INNER JOIN Person ON Transaction.Sender_ID = Person.ID)
                WHERE Keyword.tag LIKE '%$key%' AND Keyword.word = 'Person'
                ORDER BY Document.year DESC, Document.month DESC, Document.day DESC";
                
                //echo $got_trans;
                $result = $conn->query($got_trans);
            }
            elseif($_GET["type"]==="organnize"){
                $got_trans = "
                SELECT DISTINCT Document.ID AS doc_id, Document.name AS doc_name, Document.day, Document.month, Document.year, Unit.Name AS unit_name, Person.Name AS p_name
                FROM ((((Keyword
                INNER JOIN Document ON Keyword.Document_ID = Document.ID)
                INNER JOIN Transaction ON Transaction.Document_ID = Keyword.Document_ID)
                INNER JOIN Unit ON Transaction.SenderUnit_ID = Unit.ID)
                INNER JOIN Person ON Transaction.Sender_ID = Person.ID)
                WHERE Keyword.tag LIKE '%$key%' AND Keyword.word = 'Org'
                ORDER BY Document.year DESC, Document.month DESC, Document.day DESC";
                
                //echo $got_trans;
                $result = $conn->query($got_trans);
            }
            if ($result->num_rows > 0) {
                // output data of each row
                
                echo "<tbody>";
                while($row = $result->fetch_assoc()) {
                    $id = $row["doc_id"];
                    if($row["year"] == 0){
                        $year = "ไม่ปรากฏปี";
                      }
                    else{
                        $year = ($row["year"] + 543);
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
                    //echo "<tr><td><a class='doc-topic' href='opendocument.php?id=$id'>". $topicname."</a></td><td>". $sendername."</td><td>". $senderunitname. "</td><td>". $row["day"]." ". $monthconvert[$row["month"]] . $year."</td></tr>";
                    echo "<tr><td><a class='doc-topic' href='opendocument.php?id=$id'>". $topicname."</a></td><td>". $sendername."</td><td>". $senderunitname. "</td><td>". $year."/". $monthconvert[$row["month"]] . $row["day"]."</td></tr>";
                    //echo "<tr><td>". $topicname."</td><td>". $row["p_name"]."</td><td>". $row["unit_name"]. "</td><td>". $row["day"]." ". $monthconvert[$row["month"]] .$year."</td></tr>";
                }
                echo "</tbody>";
            } 
            else {
                echo "<tbody>";
                echo "<tr><td>0 results</td><td></td><td></td><td></td></tr>";
                echo "</tbody>";
            }

            
        ?>
    </div>
</body>