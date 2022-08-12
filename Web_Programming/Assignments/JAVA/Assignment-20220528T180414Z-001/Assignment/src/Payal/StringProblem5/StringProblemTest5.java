package Payal.StringProblem5;

public class StringProblemTest5 {
	public static void main(String[] args) {
		Medicine tablet = new StringProblemTablet5(23, "23/11/2026");
		tablet.displayLabel();
		tablet.getDetails();
		Medicine syrup = new StringProblemSyrup5(69, "08/05/2029");
		syrup.displayLabel();
		syrup.getDetails();
		Medicine oint = new StringProblemOintment5(96, "17/03/2030");
		oint.displayLabel();
		oint.getDetails();
	}
}
