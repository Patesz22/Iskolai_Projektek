var rossz = 0;
var jo = 0;

function run() {
    var y = Math.floor(Math.random() *201); //Generált szám
    document.getElementById("kiiras").innerHTML = y;

    var x = document.getElementById("input").value; //Tipp
    document.getElementById("gen").innerHTML = x;


if (y==x) {
    jo = jo+1
    document.getElementById("el").innerHTML = jo;
}
else {
    rossz = rossz+1;
    document.getElementById("nemel").innerHTML = rossz;
}
}



//Tóth Patrik 9.C 2021.03.22