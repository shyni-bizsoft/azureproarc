$(window).load(function() {
    console.log('load')
        $('#preloader1').fadeOut();
        var Dft = sessionStorage.getItem("Dft");
        var sts = sessionStorage.getItem("sts");
        var dept = sessionStorage.getItem("dept");
        var hrs = sessionStorage.getItem("hrs");
        var atd_typ = sessionStorage.getItem("atd_typ");
        $('#atd_typ').val(atd_typ); 
        $('#Dft').val(Dft);
        $('#sts').val(sts);
        $('#dept').val(dept);
        $('#hrs').val(hrs);
        console.log($('#sts').val())
        if ($('#sts').val() == "Offline"){
            $('#Dft').find('option[value="6"]').attr('hidden',false)
        }else{
            $('#Dft').find('option[value="6"]').attr('hidden',true)
        };
        if($('#Dft').val() == "5"){
            $('.dates').append('<div><input name="strt" id = "strt" type="date"><input name="end" id = "end" type="date"></div>')
            var strt = sessionStorage.getItem("strt");
            $('#strt').val(strt);
            var end = sessionStorage.getItem("end");
            $('#end').val(end);
        }else{}
        if($('#Dft').val() == "3" || $('#Dft').val() == "4" || $('#Dft').val() == "5"){
           var sort = sessionStorage.getItem("sort");
            $('#sort').val(sort);
        }else{$('#sort').attr('disabled',true)}
        if($("#tab tbody tr").length > 0){}
        else{
            //var d = new Date();
            //var n = d.toLocaleString([], { hour12: true});
           $("#tab tbody").append('<tr><th colspan="5">No data available in the table</th></tr>')
        }
    });

(function () {
        function sdrag(onDrag, onStop, direction) {
            var startX = 0;
            var startY = 0;
            var el = this;
            var dragging = false;

            function move(e) {
                var fix = {};
                onDrag && onDrag(el, e.pageX, startX, e.pageY, startY, fix);
                if ('vertical' !== direction) {
                    var pageX = ('pageX' in fix) ? fix.pageX : e.pageX;
                    if ('startX' in fix) {
                        startX = fix.startX;
                    }
                    if (false === ('skipX' in fix)) {
                        el.style.left = (pageX - startX) + 'px';
                    }
                }
                if ('horizontal' !== direction) {
                    var pageY = ('pageY' in fix) ? fix.pageY : e.pageY;
                    if ('startY' in fix) {
                        startY = fix.startY;
                    }
                    if (false === ('skipY' in fix)) {
                        el.style.top = (pageY - startY) + 'px';
                    }
                }
            }

            function startDragging(e) {
                if (e.currentTarget instanceof HTMLElement || e.currentTarget instanceof SVGElement) {
                    dragging = true;
                    var left = el.style.left ? parseInt(el.style.left) : 0;
                    var top = el.style.top ? parseInt(el.style.top) : 0;
                    startX = e.pageX - left;
                    startY = e.pageY - top;
                    window.addEventListener('mousemove', move);
                }
                else {
                    throw new Error("Your target must be an html element");
                }
            }

            this.addEventListener('mousedown', startDragging);
            window.addEventListener('mouseup', function (e) {
                if (true === dragging) {
                    dragging = false;
                    window.removeEventListener('mousemove', move);
                    onStop && onStop(el, e.pageX, startX, e.pageY, startY);
                }
            });
        }
        Element.prototype.sdrag = sdrag;
    })();

    var leftPane = document.getElementById('left-pane');
    var rightPane = document.getElementById('right-pane');
    var paneSep = document.getElementById('panes-separator');
    var leftLimit = 10;
    var rightLimit = 90;

    paneSep.sdrag(function (el, pageX, startX, pageY, startY, fix) {
        fix.skipX = true;

        if (pageX < window.innerWidth * leftLimit / 100) {
            pageX = window.innerWidth * leftLimit / 100;
            fix.pageX = pageX;
        }
        if (pageX > window.innerWidth * rightLimit / 100) {
            pageX = window.innerWidth * rightLimit / 100;
            fix.pageX = pageX;
        }

        var cur = pageX / window.innerWidth * 100;
        if (cur < 0) {
            cur = 0;
        }
        if (cur > window.innerWidth) {
            cur = window.innerWidth;
        }


        var right = (100-cur-2);
        leftPane.style.width = cur + '%';
        rightPane.style.width = right + '%';

    }, null, 'horizontal');

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    var content = this.nextElementSibling;
    $(content).toggle(500)
  });
}


$('#Dft').change(function() { 
    var Dft = $('#Dft').val();
    //console.log(Dft)
    sessionStorage.setItem("Dft", Dft);
});

$('#sts').change(function() { 
    var sts = $('#sts').val();
    console.log(sts)
    sessionStorage.setItem("sts", sts);
    if (sts =="Offline"){
        $('#Dft').find('option[value="6"]').attr('hidden',false)
    }
    else{
        $('#Dft').find('option[value="1"]').attr('selected','selected');
        $('#Dft').find('option[value="6"]').attr('hidden',true)
        var Dft = $('#Dft').val();
        console.log(Dft)
        sessionStorage.setItem("Dft", Dft);
    }
});

$('#hrs').change(function() { 
    var hrs = $('#hrs').val();
    sessionStorage.setItem("hrs", hrs);
});


$('#atd_typ').change(function() { 
    var atd_typ = $('#atd_typ').val();
    sessionStorage.setItem("atd_typ", atd_typ);
});

$('#ref').click(function(){
    location.reload(true);
});