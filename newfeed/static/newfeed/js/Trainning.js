$(window).load(function(){
    styleselect();
   })
   function styleselect() {
       if (document.getElementById('globalstyleselect').value == "3") {
       $("#stylediv").html('<b>3</b>');
       $("#2s1").html('');
       $("#3s1").html('Team 1');
       $("#4s1").html('');
       $("#5s1").html('Team 1');
       $("#6s1").html('');
       $("#7s1").html('');
       $("#8s1").html('');
       $("#2s2").html('Team 2');
       $("#3s2").html('');
       $("#4s2").html('');
       $("#5s2").html('Team 2');
       $("#6s2").html('');
       $("#7s2").html('');
       $("#8s2").html('');
       $("#2s3").html('Team 3');
       $("#3s3").html('Team 3');
       $("#4s3").html('');
       $("#5s3").html('');
       $("#6s3").html('Team 4');
       $("#7s3").html('');
       $("#8s3").html('Team 4'); 
     } 
       if (document.getElementById('globalstyleselect').value == "2") {
       $("#stylediv").html('<b>2</b>');
       $("#2s1").html('');
       $("#3s1").html('Team 2');
       $("#4s1").html('');
       $("#5s1").html('Team 4');
       $("#6s1").html('');
       $("#7s1").html('Team 3');
       $("#8s1").html('');
       $("#2s2").html('');
       $("#3s2").html('Team 2');
       $("#4s2").html('');
       $("#5s2").html('Team 1');
       $("#6s2").html('');
       $("#7s2").html('');
       $("#8s2").html('');
       $("#2s3").html('Team 3');
       $("#3s3").html('');
       $("#4s3").html('');
       $("#5s3").html('');
       $("#6s3").html('Team 4');
       $("#7s3").html('Team 1');
       $("#8s3").html(''); 
       } 
   
       if (document.getElementById('globalstyleselect').value == "1") {
       $("#stylediv").html('<b>1</b>');
       $("#2s1").html('Team 1');
       $("#3s1").html('');
       $("#4s1").html('');
       $("#5s1").html('Team 2');
       $("#6s1").html('');
       $("#7s1").html('Team 3');
       $("#8s1").html('');
       $("#2s2").html('');
       $("#3s2").html('Team 2');
       $("#4s2").html('');
       $("#5s2").html('Team 4');
       $("#6s2").html('');
       $("#7s2").html('');
       $("#8s2").html('');
       $("#2s3").html('Team 4');
       $("#3s3").html('');
       $("#4s3").html('');
       $("#5s3").html('Team 3');
       $("#6s3").html('');
       $("#7s3").html('');
       $("#8s3").html('Team 1'); 
   }
   }