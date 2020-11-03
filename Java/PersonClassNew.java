public class PersonClassNew
{
	public static void main(String[] args)
	{
		Person obj1 = new Person();
		System.out.println("Full Name: " + obj1.fname + " " + obj1.lname);
		System.out.println("Age: " + obj1.age);
		obj1.myMethod();
	}
}
