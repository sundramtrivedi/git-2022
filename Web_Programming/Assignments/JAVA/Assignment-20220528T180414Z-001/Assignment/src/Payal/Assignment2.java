package Payal;

import java.util.Scanner;

public class Assignment2 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter a string: ");
		String keyboardInput = input.nextLine();
		System.out.print("Enter times to be printed: ");
		int times = input.nextInt();
		
		for(int i = 0; i < times; i++) {
			System.out.println(keyboardInput);
		}
		input.close();
	}
}
