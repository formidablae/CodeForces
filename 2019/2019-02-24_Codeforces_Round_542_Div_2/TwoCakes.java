import java.util.ArrayList;
import java.util.Scanner;

public class TwoCakes
{
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		int sizes = Integer.parseInt(input.nextLine());
		
		int houses = 2 * sizes;
		
		int[] street = new int[houses];
		
		String tiersString = input.nextLine();
		String[] tiersArray = tiersString.split(" ");
		
		ArrayList<Integer> tiersArrayList = new ArrayList<Integer>();
		
		for (int i = 0; i < houses; i++)
		{
			tiersArrayList.add(Integer.parseInt(tiersArray[i]));
		}
		
		int cakesBoughtLeft = 0;
		int cakesBoughtRight = 0;
		int positionNowLeft = 0;
		int positionNowRight = 0;
		int cakeTierNowLeft = 0;
		int cakeTierNowRight = 0;
		int traveledDistanceLeft = 0;
		int traveledDistanceRight = 0;
		
		while (cakesBoughtLeft + cakesBoughtRight < houses)
		{
			System.out.println("while");
			int[] resultLeft = distanceToCake(tiersArrayList, positionNowLeft, positionNowRight, cakeTierNowLeft);
			traveledDistanceLeft = resultLeft[0] + traveledDistanceLeft;
			positionNowLeft = resultLeft[1];
			cakeTierNowLeft = resultLeft[2];
			cakesBoughtLeft++;
			
			int[] resultRight = distanceToCake(tiersArrayList, positionNowRight, positionNowLeft, cakeTierNowRight);
			traveledDistanceRight = resultRight[0] + traveledDistanceRight;
			positionNowRight = resultRight[1];
			cakeTierNowRight = resultRight[2];
			cakesBoughtRight++;
		}
		
		System.out.println((traveledDistanceLeft + traveledDistanceRight));
	}
	
	public static int[] distanceToCake(ArrayList<Integer> theTiersArrayList, int positionNowLeft, int positionNowRight, int cakeTierNow)
	{
		int[] result = new int[3];				// distance, new position, new cake tier
		int distance = 0;
		int newPosition = positionNowLeft;
		int newCakeTier = cakeTierNow;
		
		for (int i = 1; i < theTiersArrayList.size(); i++)
		{
			System.out.println("for");
			int tierNow = theTiersArrayList.get(positionNowLeft);
			
			if (positionNowLeft + i < theTiersArrayList.size() && positionNowLeft + i != positionNowRight && tierNow == theTiersArrayList.get(positionNowLeft + i) - 1)
			{
				System.out.println("if");
				distance = distance + i;
				newPosition = positionNowLeft + i;
				newCakeTier++;
				break;
			}
			else if (positionNowLeft - i >= 0 && positionNowLeft - i != positionNowRight && tierNow == theTiersArrayList.get(positionNowLeft - i) - 1)
			{
				System.out.println("else");
				distance = distance + i;
				newPosition = positionNowLeft - i;
				newCakeTier++;
				break;
			}
		}
		result[0] = distance;
		result[1] = newPosition;
		result[2] = newCakeTier;
		
		return result;
	}
}
