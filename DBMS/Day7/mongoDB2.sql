/* select * from customer where address = 'Pune' */

use LMS;

db.customer.find({'address' : 'Pune'}, {});

db.getCollection("customer").aggregate([{"$match" : {"address" : "Pune"}}]);


/* select * from customer where street_no = 123 */

db.customer.find({'billing_address.street_no' : 123}, {});

db.getCollection("customer").aggregate([{"$match" : {"billing_address.street_no" : 123}}]);

/* select * from customer where total_cost > 350 */

db.customer.find({'Cart.total_cost' : {$gt : 350}}, {});

db.customer.aggregate([{"$match" : {"Cart.total_cost" : {$gt : 350}}}]);



/* select * from customer where total_cost > 350 and address = Pune */

db.customer.find({$and : [{'Cart.total_cost' : {$gt : 350}}, {'address' : 'Pune'}]}, {});

db.customer.aggregate([{"$match" : {$and : [{'Cart.total_cost' : {$gt : 350}}, {'address' : 'Pune'}]}}]);


/* select * from customer where address in ('Pune', 'Chennai') */

db.customer.find({$or : [{'address' : 'Pune'}, {'address' : 'Chennai'}]}, {});

db.customer.aggregate([{"$match" : {$or : [{'address' : 'Pune'}, {'address' : 'Chennai'}]}}])


/* select * from customer where lower(address) in ('pune', 'chennai') */

db.customer.find({$or : [{'address' : /.*pune.*/i}, {'address' : /.*chennai.*/i}]}, {});

db.customer.aggregate([{"$match" : {$or : [{'address' : /.*pune.*/i}, {'address' : /.*chennai.*/i}]}}])



/* select * from customer where address != 'Chennai' */

db.customer.find({'address' : {$ne : 'Chennai'}}, {});

db.customer.aggregate([{"$match" : {'address' : {$ne : 'Chennai'}}}])

/* select * from customer where address like '%pune%' */

db.customer.find({'address' : /pune/i}, {});

db.customer.aggregate([{"$match" : {'address' : /pune/i}}]);


/* select * from customer where lower('address') like '%pune%' */

db.customer.find({'address' : /pune/i}, {});

db.customer.aggregate([{"$match" : {'address' : /pune/i}}]);

/* select * from customer.cart.added_products[] where [].product_id = 'X001' // invalid syntax just  */

db.customer.find({'Cart.added_products' : {$elemMatch : {'product_id' : 'X001'}}}, {});

db.customer.aggregate([{"$match" : {'Cart.added_products' : {$elemMatch : {'product_id' : 'X001'}}}}]);

db.customer.aggregate([
                        {"$match" : {'Cart.added_products' : {$elemMatch : {'product_id' : 'X001'}}}}, 
                        {"$project" : {$rename : { 'Cart.added_products' : {$elemMatch : {'product_id' : 'payal'}}}}}
                     ]);


/* select * from customer.cart.added_products[] where [].product_id = 'X003' // invalid syntax just */

db.customer.find({'Cart.added_products' : {$elemMatch : {'product_id' : 'X003'}}}, {});

db.customer.aggregate([{"$match" : {'Cart.added_products' : {$elemMatch : {'product_id' : 'X003'}}}}]);


/* name of the supplier that reside in chennai [case insensitive] */

db.LMS_SUPPLIERS_DETAILS.find({'ADDRESS' : /Chennai/i}, {'SUPPLIER_NAME' : 1, 'ADDRESS' : 1});

db.LMS_SUPPLIERS_DETAILS.aggregate([
                                    {"$match" : {'ADDRESS' : /Chennai/i}}, 
                                    {"$project" :{'SUPPLIER_NAME' : 1, 'ADDRESS' : 1}}
                                  ]);

/* name of the supplier that reside in chennai / delhi / ahmedabad [case insensitive] */

db.LMS_SUPPLIERS_DETAILS.find(
                    {$or : [{'ADDRESS' : /Chennai/i}, {'ADDRESS' : /Delhi/i}, {'ADDRESS' : /Ahmedabad/i}]}, 
                    {'SUPPLIER_NAME' : 1, 'ADDRESS' : 1}
                );
                
db.LMS_SUPPLIERS_DETAILS.aggregate([{"$match" : {$or : 
                                    [{'ADDRESS' : /Chennai/i}, {'ADDRESS' : /Delhi/i}, {'ADDRESS' : /Ahmedabad/i}]}}, 
                                    {"$project" : {'SUPPLIER_NAME' : 1, 'ADDRESS' : 1}}]);


/* name of the supplier, contact, email, address who reside in either mumbai or delhi [case insensitive] and email does not belong to gmail acoount */

db.LMS_SUPPLIERS_DETAILS.find(
                                {$and :
                                    [{$or : 
                                        [{'ADDRESS' : /Mumbai/i}, {'ADDRESS' : /Delhi/i}]}, 
                                    {'EMAIL' : {$not : /.*gmail.*/}}]}, 
                                {'SUPPLIER_NAME' : 1, 'CONTACT' : 1, 'EMAIL' : 1, 'ADDRESS' : 1}
                             );
                             
db.LMS_SUPPLIERS_DETAILS.aggregate([
                                {"$match" : 
                                    {$and :
                                        [{$or : 
                                            [{'ADDRESS' : /Mumbai/i}, {'ADDRESS' : /Delhi/i}]}, 
                                        {'EMAIL' : {$not : /.*gmail.*/}}]}}, 
                                {"$project" : 
                                    {'SUPPLIER_NAME' : 1, 'CONTACT' : 1, 'EMAIL' : 1, 'ADDRESS' : 1}}]);
                                    
                                    




/* get the gender and the respective count from customer collection */

use LMS;

db.getCollection('customer').aggregate
(
    [
        {
            '$group' :  {
                            '_id' : {'gender' : '$gender'},
                            'count' : {'$sum' : 1}
                        }
        },
        {
            '$project' :    {
                                'gender' : '$_id.gender',
                                'count' : '$count'
                            }
        }
    ]
);

/* name of the customer who has a gmail account and has added_products array an element which was added after 1/10/2021 */

db.getCollection('customer').aggregate([{'$match' : 
                                            {'email_id' : /.*gmail.com.*/i}
                                         }, 
                                        {'$unwind' : {path : '$Cart.added_products'}},
                                        {'$match' : {'Cart.added_products.date_added' : {'$gte' : '2021-10-01T00:00:00.000Z'}}}
                                        ]);

/* select lms_members from lms_members left join lms_book_issue on (lms_members.member_id = lms_book_issue.member_id) */

db.LMS_MEMBERS.aggregate([{$lookup : {from : 'LMS_BOOK_ISSUE', 
                                        localField : 'MEMBER_ID', 
                                        foreignField : 'MEMBER_ID', 
                                        as : 'output array of issuances'}}]);


/* name of the suppliers who reside in 'pune / mumbai / chennai' (case insensitive) 
who have supplied a book placed on rack_numbers A1 / A2 / A3 */


db.LMS_SUPPLIERS_DETAILS.aggregate([
                                    {$match : 
                                        {$or : 
                                            [{'ADDRESS' : /pune/i}, 
                                            {'ADDRESS' : /mumbai/i}, 
                                            {'ADDRESS' : /chennai/i}]}},
                                    {$lookup : {from : 'LMS_BOOK_DETAILS', 
                                        localField : 'SUPPLIER_ID', 
                                        foreignField : 'SUPPLIER_ID', 
                                        as : 'output array of rack number'}},
                                    {'$unwind' : {path : '$output array of rack number'}},
                                    {$match : 
                                        {$or : 
                                            [{'output array of rack number.RACK_NUM' : 'A1'}, 
                                            {'output array of rack number.RACK_NUM' : 'A2'},
                                            {'output array of rack number.RACK_NUM' : 'A3'}]
                                        }}
                                  ]);








