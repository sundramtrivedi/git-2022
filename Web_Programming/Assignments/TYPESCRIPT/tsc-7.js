var Product = /** @class */ (function () {
    function Product(str) {
        this.str = str;
    }
    Product.prototype.printAllProducts = function () {
        console.log(str);
    };
    return Product;
}());
var str = [
    {
        name: "Oreo",
        id: 1,
        price: 20
    },
    {
        name: "Bourbon",
        id: 2,
        price: 30
    },
    {
        name: "Good Day",
        id: 3,
        price: 10
    },
    {
        name: "Milk",
        id: 4,
        price: 25
    }
];
var obj = new Product(str);
obj.printAllProducts();
