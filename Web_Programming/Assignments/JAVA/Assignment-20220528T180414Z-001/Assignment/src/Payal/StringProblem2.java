package Payal;

public class StringProblem2 {
	public static void main(String[] args) {
        String names[] = {"Joy", "Meena", "Anne", "Xi", "Veena"};
        String namesMoreThan4Characters[] = allTheNames(names);
        
        for(String ele : namesMoreThan4Characters) {
        	System.out.print(ele + " ");
        }
	}
	
	public static String[] allTheNames(String[] names) {
		int size = 0;
		for(String name : names) {
			if(name.length() > 4) {
				size++;
			}
		}
		String newArr[] = new String[size];
		int index = 0;
		for(String name : names) {
			if(name.length() > 4) {
				newArr[index] = name;
				index++;
			}
		}
		
		return newArr;
	}
}
