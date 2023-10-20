/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function dropdown(id) {
document.getElementById(id).classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(e) {
if (!e.target.matches('.dropbtn')) {
const dropdowns = ["example"];
for (let x of dropdowns) {
    var myDropdown = document.getElementById(x);
    if (myDropdown.classList.contains('show')) {
        myDropdown.classList.remove('show');
    }
}
}
}