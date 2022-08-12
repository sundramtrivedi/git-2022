package Payal;
import java.util.Scanner;

public class Assignment9 {
	public static void main(String[] args) {
		int array[] = {23, 12, 34, 56, 32, 23, 54, 10, 22, 11};
		int startIndex, stopIndex;
		
		Scanner input = new Scanner(System.in);
		System.out.print("Enter the start index of the sub array: ");
		startIndex = input.nextInt();
		System.out.print("Enter the stop index of the sub array: ");
		stopIndex = input.nextInt();
		
		int subArray[] = subArr(array, startIndex, stopIndex);
		
		System.out.println("Contents of sub array are: ");
		for(int elements : subArray) {
		    System.out.println(elements);
		}
		input.close();
	}
	
	public static int[] subArr(int array[], int startIndex, int stopIndex) {
	    int size = stopIndex - startIndex + 1;
	    int subArray[] = new int[size];
	    int index = 0;
	    
	    for(int items = startIndex; items <= stopIndex; items++) {
		    subArray[index] = array[items];
		    index++;
		}
		return subArray;
	}
}
