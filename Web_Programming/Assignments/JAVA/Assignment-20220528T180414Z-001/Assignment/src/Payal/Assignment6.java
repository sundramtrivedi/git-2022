package Payal;
import java.util.Scanner;

public class Assignment6 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter Fahrenheit: ");
		double fahrenheit = input.nextFloat();
		
		double celsius = convertDegree(fahrenheit);
		System.out.println(String.format("%.2f", fahrenheit) + " Fahrenheit is " + String.format("%.2f", celsius) + "Celsius");
		input.close();
	}
	
	public static double convertDegree(double fahrenheit) {
        double celsius = (fahrenheit - 32) * 0.5556;
        return celsius;
	}
}
