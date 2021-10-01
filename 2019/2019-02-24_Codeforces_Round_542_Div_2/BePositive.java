import java.util.Scanner;

public class BePositive
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		int n = input.nextInt();
		
		int halfN;
		
		if (n % 2 == 0)
		{
			halfN = n/2;
		}
		else halfN = n/2 + 1;
		
		input.nextLine();
		
		String integersString = input.nextLine();
		String[] integersArray = integersString.split(" ");
		
		int countPositive = 0;
		int countNegative = 0;
		
		for (int i = 0; i < n; i++)
		{
			if (Integer.parseInt(integersArray[i]) > 0)
			{
				countPositive++;
			}
			else if (Integer.parseInt(integersArray[i]) < 0)
			{
				countNegative++;
			}
		}
		
		if (countPositive >= halfN)
		{
			System.out.println(countPositive);
		}
		else if (countNegative >= halfN)
		{
			System.out.println((0 - countNegative));
		}
		else System.out.println(0);
	}
}
