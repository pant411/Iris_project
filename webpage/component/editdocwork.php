<?php
    include 'component/auth.php';
    //$edit = $_GET["edit"];
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
<?php
    $id = $_POST["id"];
    //echo $id;
    $ntopic = $_POST["topic"];
    
    $nyear = $_POST["year"];
    if($nyear!=0){
        $nyear = $nyear-543;
        $change = "year=$nyear";
    }
    else{
        $change = "year=$nyear";
    }
    echo $nyear;
    

    echo $ntopic;
    if($ntopic==NULL){
        echo "notopic";
    }
    else{
        $change = $change.", name='$ntopic'";
    }
    $nday = $_POST["day"];
    echo $nday;
    if($nday==NULL){
        echo "noday";
    }
    else{
        $change = $change.", day=$nday";
    }
    $nmonth = $_POST["month"];
    echo $nmonth;
    if($nmonth==NULL){
        echo "nomonth";
    }
    else{
        $change = $change.", month=$nmonth";
    }
    if(($nday!=NULL)&&($nmonth!=NULL)&&($nyear!=0)){
        $change = $change.", date='$nyear-$nmonth-$nday'";
    }
    
    
      
    $nsender = $_POST["sender"];
    echo $nsender;
    if($nsender==NULL){
        echo "nosender";
        //$nsender = "''";
    }
    
    $nsenderunit = $_POST["senderunit"];
    echo $nsenderunit;
    if($nsenderunit==NULL){
        echo "nosenderunit";
        //$nsenderunit = "''";
    }
    else{
        //$nsenderunit = "''";
    }
    $nrecipient = $_POST["recipient"];
    echo $nrecipient;
    if($nrecipient==NULL){
        echo "norecipient";
    }
    $nrecipientunit = $_POST["recipientunit"];
    echo $nrecipientunit;
    if($nrecipientunit==NULL){
        echo "norecipientunit";
    }

    $sql = "UPDATE Document SET $change WHERE ID=$id";

    echo "<br>".$sql;
    if ($conn->query($sql) === TRUE) {
        echo "Record updated successfully";
    } 
    else {
        echo "Error updating record: " . $conn->error;
    }

    $checksenderunit = "SELECT ID, Name FROM Unit WHERE Name='$nsenderunit'";
    $resultchecksenderunit = $conn->query($checksenderunit);

    if ($resultchecksenderunit->num_rows == 1) {
    // output data of each row
        while($row = $resultchecksenderunit->fetch_assoc()) {
            //echo "id: " . $row["ID"]. " - Name: " . $row["Name"];
            $newsenderidunit = $row["ID"];
        }
        
    } else {
        $updatesenderunit = "INSERT INTO Unit (Name, Typeedit) VALUES ('$nsenderunit', 'UserEdit')";

        if ($conn->query($updatesenderunit) === TRUE) {
            //echo "New record created successfully";
            $newsenderidunit = $conn->insert_id;
        } 
        else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    }
    echo "<br>หน่วยงานที่ส่ง".$newsenderidunit;
    $checksender = "SELECT ID, Name FROM Person WHERE Name='$nsender'";
    $resultchecksender = $conn->query($checksender);

    if ($resultchecksender->num_rows == 1) {
    // output data of each row
        while($row = $resultchecksender->fetch_assoc()) {
            //echo "id: " . $row["ID"]. " - Name: " . $row["Name"];
            $newsenderid = $row["ID"];
        }
        
    } else {
        $updatesender = "INSERT INTO Person (Name, Unit_ID, Typeedit) VALUES ('$nsender', $newsenderidunit, 'UserEdit')";

        if ($conn->query($updatesender) === TRUE) {
            echo "New record created successfully";
            $newsenderid = $conn->insert_id;
        } 
        else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    }
    echo "<br>ผู้ส่ง".$newsenderid;
    
    $checkrecipientunit = "SELECT ID, Name FROM Unit WHERE Name='$nrecipientunit'";
    $resultcheckrecipientunit = $conn->query($checkrecipientunit);

    if ($resultcheckrecipientunit->num_rows == 1) {
    // output data of each row
        while($row = $resultcheckrecipientunit->fetch_assoc()) {
            //echo "id: " . $row["ID"]. " - Name: " . $row["Name"];
            $newrecipientidunit = $row["ID"];
        }
        
    } else {
        $updaterecipientunit = "INSERT INTO Unit (Name, Typeedit) VALUES ('$nrecipientunit', 'UserEdit')";

        if ($conn->query($updaterecipientunit) === TRUE) {
            echo "New record created successfully";
            $newrecipientidunit = $conn->insert_id;
        } 
        else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    }
    echo "<br>หน่วยงานที่รับ".$newrecipientidunit;
    $checkrecipient = "SELECT ID, Name FROM Person WHERE Name='$nrecipient'";
    $resultcheckrecipient = $conn->query($checkrecipient);

    if ($resultcheckrecipient->num_rows == 1) {
    // output data of each row
        while($row = $resultcheckrecipient->fetch_assoc()) {
            //echo "id: " . $row["ID"]. " - Name: " . $row["Name"];
            $newrecipientid = $row["ID"];
        }
        
    } else {
        $updaterecipient = "INSERT INTO Person (Name, Unit_ID, Typeedit) VALUES ('$nrecipient', $newrecipientidunit, 'UserEdit')";

        if ($conn->query($updaterecipient) === TRUE) {
            echo "New record created successfully";
            $newrecipientid = $conn->insert_id;
        } 
        else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    }
    echo "<br>ผู้รับ".$newrecipientid;
    $sqlt = "UPDATE Transaction SET Sender_ID='$newsenderid', SenderUnit_ID='$newsenderidunit', Recipient_ID='$newrecipientid', RecipientUnit_ID='$newrecipientidunit' WHERE Document_ID=$id";

    if ($conn->query($sqlt) === TRUE) {
      echo "Record updated successfully";
    } else {
      echo "Error updating record: " . $conn->error;
    }
    $ntopic = $_POST["topic"];
    $sqlkt = "UPDATE Keyword SET tag='$ntopic' WHERE Document_ID=$id AND word='Topic'";

    if ($conn->query($sqlkt) === TRUE) {
      echo "Record updated successfully";
    } else {
      echo "Error updating record: " . $conn->error;
    }
    $osender = $_POST["osender"];
    $sqlks = "UPDATE Keyword SET tag='$nsender' WHERE Document_ID=$id AND word='Person' AND tag='$osender'";

    if ($conn->query($sqlks) === TRUE) {
      echo "Record updated successfully";
    } else {
      echo "Error updating record: " . $conn->error;
    }
    $orecipient = $_POST["orecipient"];
    $sqlkr = "UPDATE Keyword SET tag='$nrecipient' WHERE Document_ID=$id AND word='Person' AND tag='$orecipient'";

    if ($conn->query($sqlkr) === TRUE) {
      echo "Record updated successfully";
    } else {
      echo "Error updating record: " . $conn->error;
    }

    $osenderunit = $_POST["osenderunit"];
    $sqlksu = "UPDATE Keyword SET tag='$nsenderunit' WHERE Document_ID=$id AND word='Org' AND tag='$osenderunit'";

    if ($conn->query($sqlksu) === TRUE) {
      echo "Record updated successfully";
    } else {
      echo "Error updating record: " . $conn->error;
    }
    $orecipientunit = $_POST["orecipientunit"];
    $sqlkru = "UPDATE Keyword SET tag='$nrecipientunit' WHERE Document_ID=$id AND word='Org' AND tag='$orecipientunit'";

    if ($conn->query($sqlkru) === TRUE) {
      echo "Record updated successfully";
    } else {
      echo "Error updating record: " . $conn->error;
    }
    $oyear = $_POST["oyear"];
    $sqlky = "UPDATE Keyword SET tag='$nyear' WHERE Document_ID=$id AND word='Year'";

    if ($conn->query($sqlky) === TRUE) {
      echo "Record updated successfully";
    } else {
      echo "Error updating record: " . $conn->error;
    }
    $omonth = $_POST["omonth"];
    $sqlkm = "UPDATE Keyword SET tag='$nmonth' WHERE Document_ID=$id AND word='Month' AND tag='$omonth'";

    if ($conn->query($sqlkm) === TRUE) {
      echo "Record updated successfully";
    } else {
      echo "Error updating record: " . $conn->error;
    }
    
    header( "refresh: 2; url=../opendocument.php?id=$id" );
    exit(0);
?>