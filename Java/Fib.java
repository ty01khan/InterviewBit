public class Fib
{
	static int Fibonacci(int n)
	{
		if(n <= 1)
			return n;
		
		return Fibonacci(n-1) + Fibonacci(n-2);
	}
	
	public static void main(String[] args)
	{
		for(int i = 1; i < 15; i++)
		{
			System.out.print(Fibonacci(i) + "  ");
		}
		System.out.println();
	}
}
