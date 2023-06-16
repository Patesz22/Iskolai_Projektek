var numbers = [1, 5, 7, 2, 3, 21, 4, 6, 11, 111];
console.log("A tömb hossza: ",numbers.length);
/*console.log(numbers,[0]);
console.log(numbers,[1]);
console.log(numbers,[2]);
console.log(numbers,[3]);
console.log(numbers,[4]);
console.log(numbers,[5]);       Ugyan azt csinálja mint az alatta lévő
console.log(numbers,[6]);
console.log(numbers,[7]);
console.log(numbers,[8]);
console.log(numbers,[9]);*/

for(i=0; i<10; i++) {
    if (numbers,[i]%2 == 0){
        console.log(numbers[i]);
    }
}

function ismetles(darab, mit) {
    var eredmeny = "";
    for (i=0; i<darab; i++) {
        eredmeny += mit //+= --> Összeadás || -= --> Kivonás
    }
    return eredmeny;
}
console.log(ismetles(5, "a"));

function osszeg(szam) {

var sum = 0;
for (i=0; i<=10; i++) {
    sum += i;
    }
    return sum;
}
console.log(osszeg);
