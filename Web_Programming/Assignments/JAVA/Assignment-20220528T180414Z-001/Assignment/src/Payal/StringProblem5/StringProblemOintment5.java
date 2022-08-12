package Payal.StringProblem5;

public class StringProblemOintment5 extends Medicine{
	public StringProblemOintment5(int price, String date) {
		super.price = price;
		super.expDate = date;
	}
	public void displayLabel() {
		System.out.println("for external use only");
	}
}
