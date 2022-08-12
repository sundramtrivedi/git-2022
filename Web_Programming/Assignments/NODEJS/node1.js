
function monthWord(month) {
    var toReturn
    if(month == 0) {
        toReturn = "January"
    }
    else if(month == 1) {
        toReturn = "February"
    }
    else if(month == 2) {
        toReturn = "March"
    }
    else if(month == 3) {
        toReturn = "April"
    }
    else if(month == 4) {
        toReturn = "May"
    }
    else if(month == 5) {
        toReturn = "June"
    }
    else if(month == 6) {
        toReturn = "July"
    }
    else if(month == 7) {
        toReturn = "August"
    }
    else if(month == 8) {
        toReturn = "September"
    }
    else if(month == 9) {
        toReturn = "October"
    }
    else if(month == 10) {
        toReturn = "November"
    }
    else {
        toReturn = "December"
    }
    return toReturn
}

function dayWord(day) {
    var dayOfWeek
    if(day == 0) {
        dayOfWeek = "Sunday"
    }
    else if(day == 1) {
        dayOfWeek = "Monday"
    }
    else if(day == 2) {
        dayOfWeek = "Tuesday"
    }
    else if(day == 3) {
        dayOfWeek = "Wednesday"
    }
    else if(day == 4) {
        dayOfWeek = "Thursday"
    }
    else if(day == 5) {
        dayOfWeek = "Friday"
    }
    else {
        dayOfWeek = "Saturday"
    }
    return dayOfWeek
}
function greeting()
{
    var dat = new Date()
    if(dat.getHours() <= 12) {
        console.log("Today is " + dayWord(dat.getDay()) + ", " + dat.getDate() + " " + monthWord(dat.getMonth()) + " " + dat.getFullYear() + ", Welcome, and Good Morning to You.") 
    }
    else if(dat.getHours() > 12 && dat.getHours() <= 18) {
        console.log("Today is " + dayWord(dat.getDay()) + ", " + dat.getDate() + " " + monthWord(dat.getMonth()) + " " + dat.getFullYear() + ", Welcome, and Good Afternoon to You.") 
    }
    else if(dat.getHours() > 18 && dat.getHours() <= 20) {
        console.log("Today is " + dayWord(dat.getDay()) + ", " + dat.getDate() + " " + monthWord(dat.getMonth()) + " " + dat.getFullYear() + ", Welcome, and Good Evening to You.") 
    }
    else {
        console.log("Today is " + dayWord(dat.getDay()) + ", " + dat.getDate() + " " + monthWord(dat.getMonth()) + " " + dat.getFullYear() + ", Welcome, and Good Night to You.")
    }
}
exports.greeting = greeting