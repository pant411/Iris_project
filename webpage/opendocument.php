<?php
    include 'component/auth.php';
    $edit = $_GET["edit"];
?>
<?php
    //echo $_GET["id"];
    $doc_id = $_GET["id"];
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
    include 'component/sqlconnect.php';
    $got_trans = "
        SELECT Document.ID AS doc_id, Document.name AS doc_name, Document.day, Document.month, Document.year, Unit.Name AS unit_name, Person.Name AS p_name
        FROM (((Transaction
        INNER JOIN Document ON Transaction.Document_ID = Document.ID)
        INNER JOIN Unit ON Transaction.SenderUnit_ID = Unit.ID)
        INNER JOIN Person ON Transaction.Sender_ID = Person.ID)
        WHERE Transaction.Document_ID = $doc_id;";
                
    //echo $got_trans;
    $ownerres = $conn->query($got_trans);
    //echo $ownerres->num_rows;
    if($ownerres->num_rows === 0){
        header( "refresh: 2; url=notfound.php");
        exit(0);
    } 
    else{
        while($row = $ownerres->fetch_assoc() ){
            if($row["year"] == 0){
                $year = " ไม่ปรากฏปี";
              }
            else{
                $year = " พ.ศ.".($row["year"] + 543);
            }
            if($row["doc_name"] == NULL){
                $topic = "ไม่ปรากฏชื่อเรื่อง";
            }
            else{
                $topic = $row["doc_name"];
            }
            $dtopic = $row["doc_name"];
            if($row["p_name"] == NULL){
                $sender = "ไม่พบชื่่อผู้ส่ง";
            }
            else{
                $sender = $row["p_name"];
            }
            $dsender = $row["p_name"];
            if($row["unit_name"] == NULL){
                $senderunit = "ไม่พบหน่วยงานที่ส่ง";
            }
            else{
                $senderunit = $row["unit_name"];
            }
            $dsenderunit = $row["unit_name"];
            //$topic = $row["doc_name"];
            $showdate = $row["day"]. " ". $monthconvert[$row["month"]]. $year;
            $dday = $row["day"];
            $dmonth = $row["month"];
            $dyear = $row["year"];
            //$sender = $row["p_name"];
            //$senderunit = $row["unit_name"];
        }
        $got_trans2 = "
            SELECT Document.ID AS doc_id, Document.filename AS doc_filename, Document.content AS doc_content, Unit.Name AS unit_name, Person.Name AS p_name
            FROM (((Transaction
            INNER JOIN Document ON Transaction.Document_ID = Document.ID)
            INNER JOIN Unit ON Transaction.RecipientUnit_ID = Unit.ID)
            INNER JOIN Person ON Transaction.Recipient_ID = Person.ID)
            WHERE Transaction.Document_ID = $doc_id;";   
        $docinfo = $conn->query($got_trans2); 
        while($row = $docinfo->fetch_assoc() ){
            if($row["p_name"] == NULL){
                $recipient = "ไม่พบชื่อผู้รับ";
            }
            else{
                $recipient = $row["p_name"];
            }
            if($row["unit_name"] == NULL){
                $recipientunit = "ไม่พบหน่วยงานที่ส่ง";
            }
            else{
                $recipientunit = $row["unit_name"];
            }
            $drecipient = $row["p_name"];
            $drecipientunit = $row["unit_name"];
            $content = $row["doc_content"];
            $doc_file = $row["doc_filename"];
        }
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <title><?php echo $topic; ?></title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <link rel="stylesheet" href="component/css/opendoc.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
    <?php
        include 'component/navbar.php';
        
    ?>
    <div class="indexsearchbox">
      <?php
          include 'component/searchbox.php';
      ?>
    </div>
    <div class="row">
        <div class="col-4">
            <?php
                $filename = end(explode("/", $doc_file));
                if($edit == "TRUE"){
            ?>
            <div class="docdata">
                
                
                <?php 
                    include 'component/editdoc.php'; 
                ?>
                <br>
                <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="get" >
                    <input type="hidden" name="id" value="<?php echo $doc_id?>" />
                    <button type="submit" class="btn btn-block btn-outline-dark">กลับ</button>
                </form>
            </div>                
            <?php
                }
                else{
            ?>
            <div class="docdata">
                <h3><?php echo $topic;?></h3>
                <p><?php echo $showdate;?></p>
                <p><b>ส่งโดย </b><?php echo $sender; ?></p>
                <p><b>ส่งโดยสังกัด </b><?php echo $senderunit; ?></p>
                <p><b>ส่งถึง </b><?php echo $recipient; ?></p>
                <p><b>ส่งถึงสังกัด </b><?php echo $recipientunit; ?></p>
                <p><b>ชื่อไฟล์ </b><?php 
                    
                    echo $filename; 
                ?></p>
                <b>
                    เนื้อหา
                </b>
                <p><?php echo $content; ?></p>
                <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="get" >
                    <input type="hidden" name="id" value="<?php echo $doc_id?>" />
                    <button type="submit" class="btn btn-block btn-primary" name="edit" value="TRUE">แก้ไขข้อมูลเอกสาร</button>
                </form>
            </div>
            <?php } ?>
        </div>
        <div class="col-8">
            <div class="docshow">    
                
            
            <?php
                $skul = end(explode(".", $filename));
                if($skul == "pdf"){
                    ?>  
                        <iframe src="<?php echo $doc_file;?>" width="100%" height="100%"></iframe>
                    <?php
                }
                elseif ($skul == "dummydoc") {
                    ?>  
                        <div class="dummydoc">
                            <p>นี่เป็นข้อมูลสำหรับการทดสอบ จึงไม่มีข้อมูล</p>
                        </div>
                    <?php
                }
                elseif ($skul == "png" || $skul == "PNG" || $skul == "jpg" || $skul == "JPG" || $skul == "jpeg" || $skul == "JPEG") {
                    ?>  
                        <img src="<?php echo $doc_file;?>" width="100%" height="100%"></img>
                    <?php
                }
                else{
                    ?>  
                        <div class="dummydoc">
                            <p>ไม่พบเอกสารจากแหล่งที่มาดังกล่าว</p>
                        </div>
                    <?php
                }

            ?>
            </div>
        </div>
        
    </div>
    

</body>
