import java.util.Scanner;

public class SashaTrip
{
	public static void main(String[] args)
	{
		String input  = new Scanner(System.in).nextLine();
		String[] arrayInputs = input.split(" ");
		int cities = Integer.parseInt(arrayInputs[0]);
		int capacity = Integer.parseInt(arrayInputs[1]);
		int filled = 0;
		int cost = 0;
		
		if (capacity >= (cities - 1))
		{
			System.out.println((cities - 1));
		}
		else
		{
			for (int i = 1; i < cities + 1; i++)
			{
				int distanceToDrive = cities - i;
				int newFill = 0;
//				System.out.println("cicle init filled of " + i + " = " + filled);
//				System.out.println("cicle init distanceToDrive of " + i + " = " + distanceToDrive);
				if (filled < distanceToDrive)
				{
					if (capacity >= (distanceToDrive - filled))
					{
//						System.out.println("if init filled of " + i + " = " + filled);
//						System.out.println("if init cost of " + i + " = " + cost);
						newFill = capacity - filled;
						filled = filled + newFill;
						cost = cost + newFill * i;
//						System.out.println("if newFill of " + i + " = " + newFill);
//						System.out.println("if end filled of " + i + " = " + filled);
//						System.out.println("if end cost of " + i + " = " + cost);
					}
					else
					{
//						System.out.println("else init filled of " + i + " = " + filled);
//						System.out.println("else init cost of " + i + " = " + cost);
						newFill = capacity - filled;
						filled = filled + newFill;
						cost = cost + newFill * i;
//						System.out.println("else newFill of " + i + " = " + newFill);
//						System.out.println("else end filled of " + i + " = " + filled);
//						System.out.println("else end cost of " + i + " = " + cost);
					}
					// drives 1
					filled--;
				}
				// drives 1
				else filled--;
			}
			System.out.println((cost));
		}
	}
}
