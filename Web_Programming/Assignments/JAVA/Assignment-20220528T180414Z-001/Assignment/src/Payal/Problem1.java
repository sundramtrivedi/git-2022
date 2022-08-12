package Payal;
import java.util.Scanner;

public class Problem1 {
	static int intday, intMonth, intYear;
	
	public int getIntday() {
		return intday;
	}

	public void setIntday(int intday) {
		if(intday >= 1 && intday <= 31) {
			Problem1.intday = intday;
		}
		else {
			System.out.println("Invalid Input!");
		}
	}

	public int getIntMonth() {
		return intMonth;
	}

	public void setIntMonth(int intMonth) {
		if(intMonth >= 1 && intMonth <= 12) {
			Problem1.intMonth = intMonth;
		}
		else {
			System.out.println("Invalid Input!");
		}
	}

	public int getIntYear() {
		return intYear;
	}

	public void setIntYear(int intYear) {
		if(intYear >= 1984 && intYear <= 2022) {
			Problem1.intYear = intYear;
		}
		else {
			System.out.println("Invalid Input!");
		}
	}

	public static void main(String[] args) {
		Problem1 pb = new Problem1();
		Scanner input = new Scanner(System.in);
		System.out.print("Enter date: ");
		int date = input.nextInt();
		pb.setIntday(date);
		System.out.print("Enter month: ");
		int month = input.nextInt();
		pb.setIntMonth(month);
		System.out.print("Enter year: ");
		int year = input.nextInt();
		pb.setIntYear(year);
		
		System.out.println("The date is: " + pb.getIntday() + "/" + pb.getIntMonth() + "/" + pb.getIntYear());
		input.close();
	}
}
