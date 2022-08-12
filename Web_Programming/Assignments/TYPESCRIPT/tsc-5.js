function zero_ending() {
    var arr = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        arr[_i] = arguments[_i];
    }
    var scores = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 10 == 0) {
            scores.push(arr[i]);
        }
    }
    return scores;
}
console.log(zero_ending(10, 30, 22, 44, 60, 77, 80));
