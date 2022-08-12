package Payal;

public class Assignment10 {
	public static void main(String[] args) {
		int array[] = {23, 12, 34, 57, 32, 23, 54, 10, 23, 11};
		evenElements(array);
	}
	
	public static void evenElements(int array[]) {
	    System.out.println("All the even elements in the array are: ");
	    for(int items : array) {
	        if(items % 2 == 0) {
	            System.out.println(items);
	        }
	    }
	}
}
