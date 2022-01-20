import java.util.Scanner;

public class Connect
{
	
	public static void main(String[] args)
	{
		Scanner input = new Scanner(System.in);
		int widthOfGrid = input.nextInt();
		
		input.nextLine();

		int rowPositionOfAlice = input.nextInt();
		int columnPositionOfAlice = input.nextInt();
		
		input.nextLine();

		int rowPositionDestination = input.nextInt();
		int columnPositionDestination = input.nextInt();
		
		input.nextLine();
		
		int[][] earthSeaArray = new int[widthOfGrid][widthOfGrid];
		
		for (int i = 0; i < widthOfGrid; i++)
		{
			String earthSeaString = input.nextLine();
			
			for (int j = 0; j < widthOfGrid; j++)
			{
				earthSeaArray[i][j] = Integer.parseInt(earthSeaString.substring(j, j + 1));
			}
		}
		
		
	}
	
	int move()
	{
		return 0;
	}
}
