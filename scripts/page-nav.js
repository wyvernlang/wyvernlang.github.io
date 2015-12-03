function rippleAndOpenNewWindow(linkLocation) {
    setTimeout(function() {
        var win = window.open(linkLocation, '_blank');
        win.focus();
    }, 250);
}

function onLoad(selectedPageIndex) {
    document.querySelector('iron-pages').select(selectedPageIndex);
}

function selectPage() {
    var pages = document.querySelector('iron-pages');
    return function(num) {
        pages.select(num);
    };
}
