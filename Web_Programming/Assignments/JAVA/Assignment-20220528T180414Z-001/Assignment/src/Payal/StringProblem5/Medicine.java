package Payal.StringProblem5;

abstract class Medicine {
	int price;
	String expDate;
	
	public Medicine() {}
	
	public Medicine(int price, String expDate) {
		this.price = price;
		this.expDate = expDate;
	}
	
	public void getDetails() {
		System.out.println("Price : " + this.price + " Expiray Date : " + this.expDate);
	}
	public abstract void displayLabel();
}
