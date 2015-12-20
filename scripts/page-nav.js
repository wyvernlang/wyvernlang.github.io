function rippleAndOpenNewWindow(linkLocation) {
    setTimeout(function() {
        var win = window.open(linkLocation, '_blank');
        win.focus();
    }, 250);
}

function onLoad(selectedPageIndex) {
    var pageNum = selectedPageIndex;
    if (!(history.state === null)) {
        pageNum = history.state.num;
    }
    if(!(window.location.pathname === "/")) {
        // TODO: include a way to navigate to the page based on the URL
    }
    console.log(window.location.pathname);
    document.querySelector('iron-pages').select(pageNum);
}

function onPopState(event) {
    document.querySelector('iron-pages').select(event.state.num);
}

function selectPage() {
    var pages = document.querySelector('iron-pages');
    return function(num, title) {
        var pageName = "Iron Page " + title;
        history.pushState({ num: num, title: title}, pageName, title);
        pages.select(num);
    };
}


window.onpopstate = onPopState;
