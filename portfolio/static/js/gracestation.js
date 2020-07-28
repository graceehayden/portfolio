// Display of hover text
function show(id) {
  document.getElementById(id).style.visibility = "visible";
}
function hide(id) {
  document.getElementById(id).style.visibility = "hidden";
}

function toggleDisplay(id) {
  var x = document.getElementById(id);
  if (x.style.display != "block") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
