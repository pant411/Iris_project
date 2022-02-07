<head>
    <link rel="stylesheet" href="component/css/searchbox.css">
</head>

<div class="searchall">
    <form class="form-inline" action= "search.php" method="get">
        <div class="searchby">
            <select class="form-select searchinput searchselect" name="type">
                <?php
                    if($type === "all"){
                        echo "<option value='all' selected>ทั้งหมด</option>" ;
                    }
                    else{
                        echo '<option value="all">ทั้งหมด</option>';
                    }
                    if($type === "topic"){
                        echo '<option value="topic" selected>หัวข้อ</option>';
                    }
                    else{
                        echo '<option value="topic">หัวข้อ</option>';
                    }
                    if($type === "person"){
                        echo '<option value="person" selected>บุคคล</option>';
                    }
                    else{
                        echo '<option value="person">บุคคล</option>';
                    }
                    if($type === "organize"){
                        echo '<option value="organize" selected>องค์กร</option>';
                    }
                    else{
                        echo '<option value="organize">องค์กร</option>';
                    }
                ?>
            </select>
        </div>
        <div class="searchbox">
            <input type="text" class="searchinput searchkeywordinput" placeholder="คำค้นหา" name="keyword" value="<?php echo $key;?>">
        </div>
        <div class="searchsubmit">
            <button type="submit" class="searchinput searchcon btn btn-primary"><i class="material-icons">search</i></button>
        </div>
    </form>
</div>
