class LCS
{
	public static int LCS(String X, String Y, int m, int n)
	{
		if(m == 0 || n == 0)
			return 0;
		
		if(X.charAt(m-1) == Y.charAt(n-1))
		{
			return LCS(X, Y, m-1, n-1) + 1;
		}
		
		return Integer.max(LCS(X, Y, m-1, n), LCS(X, Y, m, n-1));
	}
	
	public static void main(String[] args)
	{
		String X = "ABCBDAB", Y = "BDCABA";
		
		System.out.println("Maximum subsequence of X and Y is : " + LCS(X, Y, X.length(), Y.length()));
	}
}
