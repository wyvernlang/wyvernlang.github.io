function rippleAndOpenNewWindow(linkLocation) {
    setTimeout(function() {
        var win = window.open(linkLocation, '_blank');
        win.focus();
    }, 250);
}
