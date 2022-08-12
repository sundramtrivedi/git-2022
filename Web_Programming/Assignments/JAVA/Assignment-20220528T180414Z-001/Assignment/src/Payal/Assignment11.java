package Payal;

public class Assignment11 {
	public static void main(String[] args) {
		int array[] = {23, 12, 34, 57, 32, 23, 54, 10, 23, 11, 24, 78, 45, 87, 23, 2, 6, 30, 22, 4};
		int sum = 0;
		for(int ele : array) {
		    sum += ele;
		}
		
		int average = sum / 20;
		
		System.out.println("Elements above average are:");
		for(int ele : array) {
		    if(ele > average) {
		        System.out.println(ele);
		    }
		}
	}
}
