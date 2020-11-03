public class Factorial
{
	static int fact(int n)
	{
		if(n == 0 | n == 1)
			return n;
		
		return n*fact(n-1);
	}
	
	public static void main(String[] args)
	{
		int n = 10;
		System.out.println(n + "! = " + fact(n));
	}
}
