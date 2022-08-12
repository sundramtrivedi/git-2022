package Payal;

public class Problem6 {
	int productId;
	String description;
	double price;
	int noOfUnits;
	
	public Problem6(int productId, String description, double price, int noOfUnits) {
		this.productId = productId;
		this.description = description;
		this.price = price;
		this.noOfUnits = noOfUnits;
	}
	
	public void displayDetails() {
		System.out.println("ID: " + productId + " Description: " + description + " Price: " + price + " Total Units: " + noOfUnits);
	}
}
