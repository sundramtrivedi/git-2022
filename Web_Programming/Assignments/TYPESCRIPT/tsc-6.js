var Product = /** @class */ (function () {
    function Product() {
        this.product_id = 12;
        this.product_name = "Biryani";
        this.product_price = 300;
    }
    return Product;
}());
var product_obj = new Product;
console.log(product_obj.product_id);
console.log(product_obj.product_name);
console.log(product_obj.product_price);
