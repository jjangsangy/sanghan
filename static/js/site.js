document.addEventListener("load", pageFullyLoaded, false);
 
function pageFullyLoaded(e) {
    $(".mo[style*='STIXGeneral']").each(function() {
        var avenir = $(this).attr("style").replace("STIXGeneral", "AvenirNext");
        return $(this).attr("style", avenir);
    });
    $(".mi[style*='STIXGeneral']").each(function() {
        var avenir = $(this).attr("style").replace("STIXGeneral", "AvenirNext");
        return $(this).attr("style", avenir);
    });
};
