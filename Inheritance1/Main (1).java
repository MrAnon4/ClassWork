import java.util.Scanner;
import java.util.ArrayList;
class Main {
  public static void main(String[] args) {
    System.out.println("Hello world!");

    Scanner sc = new Scanner(System.in);

    ArrayList<Assignment> assignments = new ArrayList<Assignment>();
    
      
      System.out.println("Please enter an assignment name (exit to quit):");
      String aName = sc.nextLine();
    
    double total = 0;
    double count = 0;
  
    while(!(sc.nextLine().equals("exit"))){
      System.out.println("Please enter the available points:");
      double totalPoints = sc.nextDouble();

      System.out.println("Please enter the earned points:");
      double earnedPoints = sc.nextDouble();

      System.out.println("Is this a (t)est or (p)roject:");
      String selection = sc.nextLine();

      Assignment a1 = new Assignment(aName, totalPoints, earnedPoints);
      assignments.add(a1);

      if (selection.equals("t")){

        System.out.println("Please enter the test date:");
        String testDate = sc.nextLine();

        a1 = new Test(a1.getName(), a1.getAvaliablePoints(), a1.getEarnedPoints(), testDate);
        
      }else{

        System.out.println("Please enter the due date:");
        String projectDate = sc.nextLine();

        System.out.println("Group project? true or false:");
        boolean isGroup = sc.nextBoolean();

        a1 = new Project(a1.getName(), a1.getAvaliablePoints(), a1.getEarnedPoints(), projectDate, isGroup);
      }

      
      
    }
    Assignment.average(assignments);
  }
}