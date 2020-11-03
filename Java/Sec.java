public class Sec
{
	static void SelectionSort(int A[])
	{
		int l = A.length, i;
		for(int j=0; j<l-1; j++)
		{
			int min = A[j],x=j;
			for(i=j+1; i<l; i++)
			{
				if(A[i] < min)
				{
					min = A[i];
					x = i;
				}
			}
			if(x != 0)
			{
				int y = A[j];
				A[j] = min;
				A[x] = y;
			}		
		}
		System.out.print("Sorted Array is: ");
		for(i=0; i<l; i++)
		{
			System.out.print(A[i] + "   ");
		}
		System.out.println();
	}
	
	public static void main(String[] args)
	{
		int[] A = {7,1,5,2,8,11,6};
		SelectionSort(A);
	}
}
