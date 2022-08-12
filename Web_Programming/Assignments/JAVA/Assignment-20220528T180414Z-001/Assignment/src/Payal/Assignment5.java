package Payal;
import java.util.Scanner;

public class Assignment5 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter First Number: ");
		int numberOne = input.nextInt();
		System.out.print("Enter Second Number: ");
		int numbertwo = input.nextInt();
		System.out.print("Enter the operator: ");
		char operator = input.next().charAt(0);
		
		switch(operator) {
		    case '+':
		        System.out.println("Addition of " + numberOne + " and " + numbertwo + " is " + (numberOne + numbertwo));
		        break;
            case '-':
		        System.out.println("Subtraction of " + numberOne + " and " + numbertwo + " is " + (numberOne - numbertwo));
		        break;
            case '*':
		        System.out.println("Multiplication of " + numberOne + " and " + numbertwo + " is " + (numberOne * numbertwo));
		        break;
            case '/':
                if(numbertwo == 0) {
                    System.out.println("Division ERROR!");
                }
                else {
		            System.out.println("Division of " + numberOne + " and " + numbertwo + " is " + (numberOne / numbertwo));
                }
		        break;
		    default:
		        System.out.println("Invalid Input!");
		}
		input.close();
	}
}
