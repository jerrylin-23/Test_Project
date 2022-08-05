let numArray = [140000, 104, 99,78];
numArray.sort(function(a,b){
if (a>b) return 1;
if (a<b) return -1;
return 0;
});
console.log(numArray)

