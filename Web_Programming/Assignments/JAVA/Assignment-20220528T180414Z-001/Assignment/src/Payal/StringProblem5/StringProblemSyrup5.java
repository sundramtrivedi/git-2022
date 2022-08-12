package Payal.StringProblem5;

public class StringProblemSyrup5 extends Medicine{
	public StringProblemSyrup5(int price, String date) {
		super.price = price;
		super.expDate = date;
	}
	public void displayLabel() {
		System.out.println("Keep away from children");
	}
}
