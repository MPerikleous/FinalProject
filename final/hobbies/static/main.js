var hiddenClass = 'hidden';
var shownClass = 'toggled-from-hidden';

function userSectionHover() {
    var children = this.children;
    for(var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.className === hiddenClass) {
            child.className = shownClass;
        }
    }
}

function userSectionEndHover() {
    var children = this.children;
    for(var i = 0; i < children.length; i++) {
        var child = children[i];
        if (child.className === shownClass) {
            child.className = hiddenClass;
        }
    }
}

(function() {
    var userSections = document.getElementsByClassName('username');
    for(var i = 0; i < userSections.length; i++) {
        userSections[i].addEventListener('mouseover', userSectionHover);
        userSections[i].addEventListener('mouseout', userSectionEndHover);
    }
}());
