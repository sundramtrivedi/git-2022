package ExceptionsProb.Problem4;

public class Rectangle {
	private int length;
	private int breadth;
	
	public Rectangle() {
		this.length = 0;
		this.breadth = 0;
	}

	public int getLength() {
		return length;
	}

	public void setLength(int length) {
		this.length = length;
	}

	public int getBreadth() {
		return breadth;
	}

	public void setBreadth(int breadth) {
		this.breadth = breadth;
	}
	
	public int calculateArea(int l, int b) {
		int area = l * b;
		return area;
	}
	
	public int calculatePeri(int l, int b) {
		int perimeter = 2 * (l + b);
		return perimeter;
	}
	
	public void display(int len, int bre) {
		System.out.println("The area of rectangle is " + calculateArea(len, bre));
		System.out.println("The perimeter of rectangle is " + calculatePeri(len, bre));
		System.out.println("");
	}
}
