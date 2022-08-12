import java.util.Scanner;

public class Book {
	private int bookNo;
	private String title;
	private String author;
	private float price;
	
	public void setbookNo(int bookno) {
		this.bookNo=bookno;
	}
	public int getbookNo() {
		return bookNo;
	}
	public void settitle(String title) {
		this.title=title;
	}
	public String gettitle() {
		return title;
	}
	public void setauthor(String author) {
		this.author=author;
	}
	public String getauthor() {
		return author;
	}
	public void setprice(float price) {
		this.price=price;
	}
	public float getprice() {
		return price;
	}
	public void incrPrice(float percentage) {
		this.price= ((this.price*percentage)/100);
	}
	
	public Book() {
		
	}
	
	public Book(int bookNo, String title, String author, float price) {
		super();
		this.bookNo = bookNo;
		this.title = title;
		this.author = author;
		this.price = price;
	}
	public String displayBookDetails()
	{
		return "bookNo:"+this.bookNo+"\n"+"title:"+this.title+"\n"+"Author:"+this.author+"\n"+"Price:"+this.price+"\n";
	}
	public static void main(String[] args) {
		Book b1 = new Book();
		Scanner sc= new Scanner(System.in);
		System.out.println("Enter Book NO");
		int bookno = sc.nextInt();
		System.out.println("Enter Book Title");
		String booktitle = sc.next();
		System.out.println("Enter Author");
		String author = sc.next();
		System.out.println("Enter Book Price");
		float price = sc.nextFloat();
		b1.setbookNo(bookno);
		b1.settitle(booktitle);
		b1.setauthor(author);
		b1.setprice(price);
		System.out.println(b1.displayBookDetails());
		System.out.println("Enter the percnetage to increase book price");
		float percentage = sc.nextFloat();
		b1.incrPrice(percentage);
		System.out.println(b1.displayBookDetails());
		sc.close();
	}

}
