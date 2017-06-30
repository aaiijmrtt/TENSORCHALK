$(document).ready(function(){
    var dH = $(window).height() - $("#navbar").outerHeight();
    $("#index-body-div, #api-elems").css({
        height: dH
    });
    console.log(dH);
});
$(document).foundation();
