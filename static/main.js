
$(document).ready(function(){

  function getRdnDream() {
    $.get("/get_rdn_dream", function(data, status){
      // alert("Data: " + data + "\nStatus: " + status);
      // console.log(data);
      $("#feature-dream").fadeIn(1000);
      $('#feature-dream-info').html('"..'+data.info+'.."');
      $('#feature-dream-date').html(data.date);
      $("#feature-dream").delay(5500).fadeOut(1000);
    });
  }
  getRdnDream();
  setInterval(getRdnDream, 7500);
});
