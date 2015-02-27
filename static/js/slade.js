$(document).ready(function(){
    $(".parent").mouseout(function(){
        $(".slade").slideUp();
    });
    $(".parent").mouseover(function(){
        $(".slade").slideDown();
    });
});