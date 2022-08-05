
function add(x) {
    return function (y) {
    return function (z){

        return  x + y + z;

    };
    }
    
    
}

    const addXY = add(2)(0);
    const add3 = add(3)(4);

    console.log(addXY(3));
    console.log(add3(3));


