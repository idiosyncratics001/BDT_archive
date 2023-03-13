/* data tools JavaScript
*/

/* Navigation Show/Hide*/

function dtNavButton(){
  var checkBox = document.getElementById("check");
  var navbutton = document.getElementById("navbutton");
  var navprofile = document.getElementById("navprofile");
  var menutext = document.getElementsByClassName('menu-text');
  if (checkBox.checked == false){
    navbutton.textContent=">>";
    navprofile.style.display = "none";
      for(var i=0; i<menutext.length; i++) { 
          menutext[i].style.display='none';
          }
    checkBox.checked = true;
  } else {
    navbutton.textContent="<<";
    navprofile.style.display = "flex";
    navmenu.style.display = "initial";
    for(var i=0; i<menutext.length; i++) { 
        menutext[i].style.display='initial';
        }
    checkBox.checked = false;
  }
}

function dtMobNavButton(){
  var checkBox = document.getElementById("check");
  var checkBox = document.getElementById("nav");
  if (checkBox.checked == false){
    nav.style.display = "none";
    checkBox.checked = true;
  } else {
    nav.style.display = "initial";
    checkBox.checked = false;
  }


}