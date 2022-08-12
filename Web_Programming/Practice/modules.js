"use strict";
exports.__esModule = true;
exports.sname = "Payal";
function greet() {
    console.log("hello", exports.sname);
}
exports.greet = greet;
var Student = /** @class */ (function () {
    function Student(studname, prn) {
        this.sname = studname;
        this.prn = prn;
    }
    Student.prototype.display = function () {
        console.log("Name : ", this.sname, "PRN : ", this.prn);
    };
    return Student;
}());
exports.Student = Student;
