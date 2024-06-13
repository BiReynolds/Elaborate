// Constants / DOM Elements

var contextMenu = document.getElementsByClassName("context-menu")[0];
console.log(contextMenu);
var menuState = 0;
var contextMenuActive = "block";

// Setting up screen 

document.addEventListener("contextmenu", function (event) {
    event.preventDefault();
    toggleMenuOn();
    positionMenu(event);
  });

  document.addEventListener("click", (e) => {
    var button = e.which || e.button;
    if (button === 1) {
      toggleMenuOff();
    }
  });

// Context Menu Stuff

//----------------------Helper functions------------------------//

function toggleMenuOn() {
    if (menuState != 1) {
        menuState = 1;
        contextMenu.classList.add("menuActive");
    }
}

function toggleMenuOff() {
    if (menuState != 0) {
        menuState = 0;
        contextMenu.classList.remove("menuActive");
    }
}


function positionMenu(e) {
    let clickCoords = getPosition(e);
    let clickCoordsX = clickCoords.x;
    let clickCoordsY = clickCoords.y;
  
    let menuWidth = contextMenu.offsetWidth + 4;
    let menuHeight = contextMenu.offsetHeight + 4;
  
    let windowWidth = window.innerWidth;
    let windowHeight = window.innerHeight;
  
    if (windowWidth - clickCoordsX < menuWidth) {
      contextMenu.style.left = windowWidth - menuWidth + "px";
    } else {
      contextMenu.style.left = clickCoordsX + "px";
    }
  
    if (windowHeight - clickCoordsY < menuHeight) {
      contextMenu.style.top = windowHeight - menuHeight + "px";
    } else {
      contextMenu.style.top = clickCoordsY + "px";
    }
  }

// Gets the position of the mouse on a click event
function getPosition(e) {
    var posx = 0;
    var posy = 0;
  
    if (!e) var e = window.event;
  
    if (e.pageX || e.pageY) {
      posx = e.pageX;
      posy = e.pageY;
    } else if (e.clientX || e.clientY) {
      posx =
        e.clientX +
        document.body.scrollLeft +
        document.documentElement.scrollLeft;
      posy =
        e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
    }
  
    return {
      x: posx,
      y: posy
    };
  }