package Payal;

import java.util.Scanner;

public class Assignment1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter three numbers:");
		System.out.print("No_1: ");
		int numberOne = input.nextInt();
		System.out.print("No_2: ");
		int numberTwo = input.nextInt();
		System.out.print("No_3: ");
		int numberThree = input.nextInt();
		
		if(numberOne > numberTwo && numberOne > numberThree) {
			System.out.println("Largest number is " + numberOne);
		}
		else if(numberTwo > numberThree) {
			System.out.println("Largest number is " + numberTwo);
		}
		else {
			System.out.println("Largest number is " + numberThree);
		}
		input.close();
	}
}
