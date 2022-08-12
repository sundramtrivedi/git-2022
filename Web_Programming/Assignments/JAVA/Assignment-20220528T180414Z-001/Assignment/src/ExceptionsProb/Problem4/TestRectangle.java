package ExceptionsProb.Problem4;
import java.util.Scanner;

public class TestRectangle{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		Rectangle rec = new Rectangle();
		
		for(int i = 0; i < 5; i++) {
			System.out.print("Enter the length: ");
			int len = input.nextInt();
			rec.setLength(len);
			System.out.print("Enter the breadth: ");
			int bre = input.nextInt();
			rec.setBreadth(bre);
			
			rec.display(rec.getLength(), rec.getBreadth());
		}
		input.close();
	}
}
