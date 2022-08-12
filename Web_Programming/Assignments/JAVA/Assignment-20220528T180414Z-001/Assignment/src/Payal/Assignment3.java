package Payal;

import java.util.Scanner;

public class Assignment3 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a number: ");
		int number = input.nextInt();
		
		System.out.println("Even numbers between 0 and ");
		
		for(int i = 0; i <= number; i++) {
			if(i % 2 == 0) {
				System.out.println(i);
			}
		}
		input.close();
	}
}
