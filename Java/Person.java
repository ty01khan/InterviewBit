class Person
{
	String fname = "Talha";
	String lname = "Yaseen";
	int age = 21;
	public void myMethod()
	{
		System.out.println("My Full Name is: Md Talha Yaseen Khan");
	}

	public static void main(String[] args)
	{
		Person obj1 = new Person();
		System.out.println("Full Name: " + obj1.fname + " " + obj1.lname);
		System.out.println("Age: " + obj1.age);
		obj1.myMethod();
	}
}
