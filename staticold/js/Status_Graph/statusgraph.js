

$(window).load(function() {
        var Dftr = sessionStorage.getItem("Dftr");
        var ustm = sessionStorage.getItem("ustm");
        var uslst = sessionStorage.getItem("uslst");
        //var sts = sessionStorage.getItem("sts");
        $('#Dftr').val(Dftr);
        $('#ustm').val(ustm);
        $('#uslst').val(uslst);
        //$('#sts').val(sts);
        if($("#tab tbody tr").length > 0){}
        else{
            var d = new Date();
            var n = d.toLocaleString([], { hour12: true});
           $("#tab tbody").append('<tr><th colspan="5">No data available in the table</th></tr>')
        }
        $("#preloader1").fadeOut();
    });


var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    var content = this.nextElementSibling;
    $(content).toggle(500)
  });
}




