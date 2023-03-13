/* data tools JavaScript
*/

/* Navigation Show/Hide*/

function dtNavButton(){
  var dtCheck = document.getElementById("dtCheck");
  var dtNavbutton = document.getElementById("dtNavbutton");
  var dtProfile = document.getElementById("dtProfile");
  var dtMenutext = document.getElementsByClassName('dtMenu-text');
  if (dtCheck.checked == false){
    dtNavbutton.textContent=">>";
    dtProfile.style.display = "none";
      for(var i=0; i<dtMenutext.length; i++) { 
          dtMenutext[i].style.display='none';
          }
    dtCheck.checked = true;
  } else {
    dtNavbutton.textContent="<<";
    dtProfile.style.display = "flex";
    for(var i=0; i<dtMenutext.length; i++) {
        dtMenutext[i].style.display='initial';
        }
    dtCheck.checked = false;
  }
}

function dtMobNavButton(){
  var checkBox = document.getElementById("dtMobCheck");
  var dtNav = document.getElementById("dtNav");
  if (checkBox.checked == false){
    dtNav.style.display = "none";
    checkBox.checked = true;
  } else {
    dtNav.style.display = "initial";
    checkBox.checked = false;
  }


}