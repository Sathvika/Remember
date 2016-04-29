$(function(){
    $("#gridView").addClass("hideMe");
});

function changeView(value){
    if (value === "gallery"){
        $("#listView").addClass("hideMe");
        $("#gridView").removeClass("hideMe");
    } else {
        $("#listView").removeClass("hideMe");
        $("#gridView").addClass("hideMe");
    }
}

