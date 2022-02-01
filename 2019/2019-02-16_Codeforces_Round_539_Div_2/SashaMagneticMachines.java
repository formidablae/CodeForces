import java.util.Scanner;

public class SashaMagneticMachines
{
	public static void main(String[] args)
	{
		String firstLine  = new Scanner(System.in).nextLine();
		int numberOfMachines = Integer.parseInt(firstLine);
		String secondLine  = new Scanner(System.in).nextLine();
		String[] powersOfMachinesStrings = secondLine.split(" ");
		int[] powersOfMachinesInt = new int[numberOfMachines];
		int[] xDivisors = new int [numberOfMachines];
		int smallestPower = Integer.parseInt(powersOfMachinesStrings[0]);
		
		for (int i = 0; i < numberOfMachines; i++)
		{
			powersOfMachinesInt[i] = Integer.parseInt(powersOfMachinesStrings[i]);
			if (powersOfMachinesInt[i] < smallestPower)
			{
				smallestPower = powersOfMachinesInt[i];
			}
		}
		
		for (int i = 0; i < numberOfMachines; i++)
		{
			for (int j = 0; j < numberOfMachines; j++)
			{
				if (i != j)
				{
					if (powersOfMachinesInt[i] / powersOfMachinesInt[j] > 2)
					{
						
					}
					else if (powersOfMachinesInt[j] / powersOfMachinesInt[i] > 2)
					{
						
					}
					/*if (!isPrime(powersOfMachinesInt[i]) && powersOfMachinesInt[i] != 1)
					{
						
						smallestPower * 
					}*/
				}
			}
		}
	}
	
	public static boolean isPrime(int nunber)
	{
	    int num = nunber;
	    boolean flag = false;
	    for(int i = 2; i <= num/2; ++i)
	    {
	        // condition for nonprime number
	        if(num % i == 0)
	        {
	            flag = true;
	            break;
	        }
	    }
	
	    return flag;
	}
}
