function operations() {
    var arr = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        arr[_i] = arguments[_i];
    }
    var min = arr[0];
    var max = arr[0];
    var total = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
        if (arr[i] > max) {
            max = arr[i];
        }
        total += arr[i];
    }
    var average = total / arr.length;
    console.log("The minimum value in the array is : " + min);
    console.log("The maximum value in the array is : " + max);
    console.log("The average value in the array is : " + total);
}
operations(6, 12, 53, 7, 3, 5, 6, 2, 44);
