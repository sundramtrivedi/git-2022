package Payal;

public class StringProblem3 {
	public static void main(String[] args) {
        String website[] = {"www.Joy.com", "ww.Meena.com", "Anne.com", "www.Xi.cu", "www.Veena.in"};
        int totalWebsiteWithWWW = allTheWebsites(website);
        
        System.out.println("Total websites starting with www are: " + totalWebsiteWithWWW);
	}
	
	public static int allTheWebsites(String[] websites) {
		int counter = 0;
		System.out.println("The website names are:");
		for(String name : websites) {
			if(name.startsWith("www.")) {
				System.out.println(name);
				counter++;
			}
		}
		
		return counter;
	}
}
