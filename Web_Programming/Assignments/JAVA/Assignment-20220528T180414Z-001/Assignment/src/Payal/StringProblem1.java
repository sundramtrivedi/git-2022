package Payal;
import java.util.Scanner;

public class StringProblem1 {
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a string to compare: ");
        String str = input.next();
        
        if(validator(str)) {
            System.out.println("It is a palindrome string!");
        }
        else {
            System.out.println("It is not a palindrome string!");
        }
        input.close();
	}
	
	public static boolean validator(String str) {
        String revStr = str;
        for(int i = 0; i < str.length(); i++) {
            if(str.charAt(i) != revStr.charAt(str.length()-i-1)) {
                return false;
            }
        }
        return true;
	}
}
