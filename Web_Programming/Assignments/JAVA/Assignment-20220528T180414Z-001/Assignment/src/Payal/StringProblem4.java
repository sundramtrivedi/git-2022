package Payal;
import java.util.Scanner;

public class StringProblem4 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the book details:");
		String book = sc.nextLine();
		
		String bookDetails[] = book.split(";");
		
		char list = 'a';
		for(String name : bookDetails) {
			String eachDetail[] = name.split("=");
			for(int i = 0; i < 2; i++) {
				if(i == 0) {
					System.out.print(list + ". ");
				}
 				System.out.print(eachDetail[i]);
				if(i == 0) {
					System.out.print(" : ");
				}
			}
			list++;
			System.out.println("");
		}
		sc.close();
	}
}
