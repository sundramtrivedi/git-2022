package Payal;
import java.util.Scanner;

public class Assignment7 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter your weight (kg): ");
		float weight = input.nextFloat();
		System.out.print("Enter your height (m): ");
		float height = input.nextFloat();
		
		System.out.println("You are "+ bmiCalculator(weight, height));
		input.close();
	}
	
	public static String bmiCalculator(float weight, float height) {
        double bmiValue = weight / (height * height);
        if(bmiValue < 18.5) {
            return "Underweight";
        }
        else if(bmiValue >= 18.5 && bmiValue < 25.0) {
            return "Normal";
        }
        else if(bmiValue >= 18.5 && bmiValue < 25.0) {
            return "Overweight";
        }
        else {
            return "Obese";
        }
	}
}
