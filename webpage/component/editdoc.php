<form action="component/editdocwork.php" method="post" >
                    <input type="hidden" name="id" value="<?php echo $doc_id;?>" />
                    <input type="hidden" name="otopic" value="<?php echo $dtopic;?>" />
                    <input type="hidden" name="oday" value="<?php echo $dday;?>" />
                    <input type="hidden" name="omonth" value="<?php echo $dmonth;?>" />
                    <input type="hidden" name="oyear" value="<?php echo $$dyear;?>" />
                    <input type="hidden" name="osender" value="<?php echo $dsender;?>" />
                    <input type="hidden" name="osenderunit" value="<?php echo $dsenderunit;?>" />
                    <input type="hidden" name="orecipient" value="<?php echo $drecipient;?>" />
                    <input type="hidden" name="orecipientunit" value="<?php echo $drecipientunit;?>" />
                    <div class="form-group row">
                        <label for="topic" class="col-sm-2 col-form-label">หัวข้อ</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" name="topic" value="<?php echo $dtopic?>" placeholder="หัวข้อ"/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="topic" class="col-sm-2 col-form-label">วันที่</label>
                        <div class="col-sm-2">
                            <input type="number" class="form-control" name="day" value="<?php echo $dday;?>" placeholder="วันที่" min="0" max="31"/>
                        </div>
                        <div class="col-sm-4">
                            <select class="form-control form-select form-select-lg" aria-label="Default select example" name="month">
                                <option value="<?php echo $dmonth;?>" selected><?php echo $monthconvert[$dmonth];?></option>
                                <option value="1">มกราคม</option>
                                <option value="2">กุมภาพันธ์</option>
                                <option value="3">มีนาคม</option>
                                <option value="4">เมษายน</option>
                                <option value="5">พฤษภาคม</option>
                                <option value="6">มิถุนายน</option>
                                <option value="7">กรกฎาคม</option>
                                <option value="8">สิงหาคม</option>
                                <option value="9">กันยายน</option>
                                <option value="10">ตุลาคม</option>
                                <option value="11">พฤศจิกายน</option>
                                <option value="12">ธันวาคม</option>
                            </select>
                        </div>
                        <label for="year" class="col-sm-1 col-form-label">พ.ศ.</label>
                        <div class="col-sm-3">
                            <input type="number" class="form-control" name="year" value="<?php 
                            if($dyear!=0){
                                echo $dyear+543;
                            }
                            else{
                                echo 0;
                            }

                            ?>" placeholder="ปีพ.ศ." min="0"/>
                        </div>
                    </div>
                    <p>หากไม่พบปี ปีจะเท่ากับ 0</p>
                    <div class="form-group row">
                        <label for="sender" class="col-sm-2 col-form-label">ส่งโดย</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" name="sender" value="<?php echo $dsender;?>" placeholder="ผู้ส่ง"/>
                        </div>
                    </div>
                    
                    <div class="form-group row">
                        <label for="sender" class="col-sm-2 col-form-label">ส่งโดยสังกัด</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" name="senderunit" value="<?php echo $dsenderunit;?>" placeholder="หน่วยงานส่ง"/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="sender" class="col-sm-2 col-form-label">ส่งถึง</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" name="recipient" value="<?php echo $drecipient;?>" placeholder="ผู้รับ"/>
                        </div>
                    </div>
                    <div class="form-group row">
                        <label for="sender" class="col-sm-2 col-form-label">ส่งถึงสังกัด</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" name="recipientunit" value="<?php echo $drecipientunit;?>" placeholder="หน่วยงานที่รับ"/>
                        </div>
                    </div>
                    <p><b>ชื่อไฟล์ </b><?php 
                    
                        echo $filename; 
                    ?></p>
                    <b>
                        เนื้อหา
                    </b><p><?php echo $content; ?></p>
                    <button type="submit" class="btn btn-block btn-primary" name="edit" value="TRUE">แก้ไข</button>
</form>
