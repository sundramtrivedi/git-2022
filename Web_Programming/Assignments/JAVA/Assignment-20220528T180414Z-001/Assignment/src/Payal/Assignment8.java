package Payal;

public class Assignment8 {
	public static void main(String[] args) {
		int array[] = {23, 12, 34, 56, 32};
		int sum = 0;
		
		for(int items : array) {
		    sum += items;
		}
		
		System.out.println("The Sum of all the elements in the array is " + sum);
		System.out.println("The Average of all the elements in the array is " + (sum/5));
	}
}
