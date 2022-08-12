/* Create a database named BOXOFFICE */

use BOXOFFICE;

/* Create a collection named movie */


db.createCollection('MOVIE');

db.createCollection('MOVIE1');

/* insert one document {name: "Pardes", "Box_office_collection": 900000, "invested_amount": 30000} */

db.MOVIE.insertOne
(
    {
        name: "Pardes", 
        "Box_office_collection": 900000, 
        "invested_amount": 30000,
        "genre": "Love",
        _id: "Pardes"
    }
);

db.MOVIE1.insertOne
(
    {
        name: "Pardes", 
        "Box_office_collection": 900000, 
        "invested_amount": 30000
    }
);

/* insert one document {name: "DDLJ", "Box_office_collection": 400000, "invested_amount": 10000} */


db.MOVIE.insertOne
(
    {
        name: "DDLJ", 
        "Box_office_collection": 400000, 
        "invested_amount": 10000,
        "genre": "Love",
        _id: "DDLJ"
    }
);

db.MOVIE1.insertOne
(
    {
        name: "DDLJ", 
        "Box_office_collection": 400000, 
        "invested_amount": 10000
    }
);

/* insert many documents 
{name: "HULK", "Box_office_collection": 200000, "invested_amount": 1000}
{name: "IRON MAN", "Box_office_collection": 15000, "invested_amount": 100} */

db.MOVIE.insertMany
([
    {
        name: "HULK", 
        "Box_office_collection": 200000, 
        "invested_amount": 1000,
        "genre": "Marvel",
        _id: "HULK1"
    },
    {
        name: "IRON MAN", 
        "Box_office_collection": 15000, 
        "invested_amount": 100,
        "genre": "Marvel",
        _id: "IRON MAN1"
    }
]);


db.MOVIE1.insertMany
([
    {
        name: "HULK", 
        "Box_office_collection": 200000, 
        "invested_amount": 1000
    },
    {
        name: "IRON MAN", 
        "Box_office_collection": 15000, 
        "invested_amount": 100
    }
]);

/* display the inserted documents using find function syntax: db.<collection_name>.find(); */

db.getCollection('MOVIE').find({}, {});

db.getCollection('MOVIE1').find({}, {});

/* drop the collection named movie */

db.MOVIE1.drop();


/* display the name of the movie and the invested amount using find function 
syntax : db.<collection_name>.find({where clause},{select clause}) */

db.MOVIE.find({}, {_id : 0, 'name' : 1, 'invested_amount' : 1});

/* display the name of the movie and the invested amount whose name = 'DDLJ' using find function
syntax : db.<collection_name>.find({where clause}, {select clause}) */

db.MOVIE.find({'name' : 'DDLJ'}, {_id : 0, 'name' : 1, 'invested_amount' : 1});

/* insert many documents 
[
{name: "HULK", "Box_office_collection": 200000, "invested_amount": 1000},
{name: "IRON MAN", "Box_office_collection": 150000, "invested_amount": 100},
{name: "HULK", "Box_office_collection": 200000, "invested_amount": 1000},
{name: "IRON MAN", "Box_office_collection": 150000, "invested_amount": 100},
{name: "DOCTOR STRANGE", "Box_office_collection": 200000, "invested_amount": -9999},
{name: "DOCTOR STRANGE", "Box_office_collection": 200000, "invested_amount": -9999},
{name: "WAQT", "Box_office_collection": 150000, "invested_amount": -9},
{name: "WAQT", "Box_office_collection": 150000, "invested_amount": -8}
] */

db.MOVIE.insertMany
([
    {
        name: "HULK", 
        "Box_office_collection": 200000, 
        "invested_amount": 1000,
        "genre": "Marvel",
        _id: "HULK2"
    },
    {
        name: "IRON MAN", 
        "Box_office_collection": 150000, 
        "invested_amount": 100,
        "genre": "Marvel",
        _id: "IRON MAN2"
    },
    {
        name: "HULK", 
        "Box_office_collection": 200000, 
        "invested_amount": 1000,
        "genre": "Marvel",
        _id: "HULK3"
    },
    {
        name: "IRON MAN", 
        "Box_office_collection": 150000, 
        "invested_amount": 100,
        "genre": "Marvel",
        _id: "IRON MAN3"
    },
    {
        name: "DOCTOR STRANGE", 
        "Box_office_collection": 200000, 
        "invested_amount": -9999,
        "genre": "Friction",
        _id: "DOCTOR STRANGE1"
    },
    {
        name: "DOCTOR STRANGE", 
        "Box_office_collection": 200000, 
        "invested_amount": -9999,
        "genre": "Friction",
        _id: "DOCTOR STRANGE2"
    },
    {
        name: "WAQT", 
        "Box_office_collection": 150000, 
        "invested_amount": -9,
        "genre": "Romantic",
        _id: "WAQT1"
    },
    {
        name: "WAQT", 
        "Box_office_collection": 150000, 
        "invested_amount": -8,
        "genre": "Romantic",
        _id: "WAQT1"
    }
]);



/* delete all the document that has name = HULK */

db.MOVIE.deleteMany({'name' : 'HULK'});


/* delete any one document that has name = IRON MAN */

db.MOVIE.deleteOne({'name' : 'Pardes'});



/* update the invested_amount by 10000 for all document that has name = DOCTOR STRANGE */

db.MOVIE.updateMany({'name' : 'DOCTOR STRANGE'}, {$set : {'invested_amount' : 10000}});



/* update the invested_amount by 10 for any one document that has name = WAQT */

db.MOVIE.updateOne({'name' : 'WAQT'}, {$set : {'invested_amount' : 10}});


/* update the invested_amount by 10000 for all document that has name = DOCTOR STRANGE */

db.MOVIE.updateMany({name : "DOCTOR STRANGE"}, {$inc : {invested_amount : 999}});


/* update the invested_amount by 10 for any one document that has name = WAQT */

db.MOVIE.updateMany({name : "WAQT"}, {$inc : {invested_amount : 5050}});


/* output the name of the movie, invested amount of all those whose names have a/A in it */

db.MOVIE.find({'name' : /.*a.*/i}, {_id : 1, 'name' : 1, 'invested_amount' : 1});



/* output the name of the movie, invested amount of all those who invested amount is greater than 10000
HINT : use $gt operator to do the comparison */

db.MOVIE.find({invested_amount : {$gt : 10000}}, {_id : 1, 'name' : 1, 'invested_amount' : 1});


/* output the name of the movie, invested amount of all those who have genre Fiction
(case insensitive search) */

db.MOVIE.find({'genre' : 'Friction'}, {_id : 1, 'name' : 1, 'invested_amount' : 1});


/* name of the movie who have profit greater than 10000 rs */


/* name of the supplier that reside in chennai [case insensitive] */


use LMS;
db.LMS_SUPPLIERS_DETAILS.find({'ADDRESS' : /.*Chennai.*/i}, {});

/* name of the supplier that reside in chennai / delhi / ahmedabad [case insensitive] */

db.LMS_SUPPLIERS_DETAILS.find({$or : [{'ADDRESS' : /.*Delhi.*/i}, 
                                        {'ADDRESS' : /.*Chennai.*/i}, 
                                        {'ADDRESS' : /.*Ahmedabad.*/i}]}, {});


/* name of the supplier, contact, email, address who resides in either mumbai or delhi [case insensitive] 
and email does not belong to gmail account */

db.LMS_SUPPLIERS_DETAILS.find({$and :[{$or : [{'ADDRESS' : /.*Delhi.*/i}, 
                                      {'ADDRESS' : /.*Mumbai.*/i}]},
                                       {'EMAIL' : {$not : /.*gmail*./i}}]}, {});



/* book_name, book_publication of all books placed on rack_num = a1 and publication is not equal to tata mcgraw hill */

use LMS;
db.LMS_BOOK_DETAILS.find({$and :[{'RACK_NUM' : 'A1'}, {'PUBLICATION' : {$not : /.*mcgraw.*/i}}]}, {});


/* book_code, member_id of all book issuances which have been fined book_name */

db.LMS_BOOK_ISSUE.find({'FINE_RANGE' : {$ne : null}}, {});

/* query for embedded json dataset book_name and publication whose has atleast one supplier from chennai (case insensitive) 
HINT : $elemmatch*/

use LMS;
db.EMBEDDED_JSON.find({'BOOKS_SUPPLIED' : {$ne : null}}, {});







