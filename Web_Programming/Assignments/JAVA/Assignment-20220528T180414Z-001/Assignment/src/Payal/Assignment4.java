package Payal;
import java.util.Scanner;

public class Assignment4 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Table of: ");
		int table = input.nextInt();
		
		for(int times = 1; times <= 10; times++) {
			System.out.println(table + " x " + times + " = " + (table * times));
		}
		input.close();
	}
}
