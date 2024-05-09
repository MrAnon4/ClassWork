import java.util.ArrayList;
public class Assignment{

  private String name;
  private double avaliablePoints;
  private double earnedPoints;

  public Assignment(String name, double avaliablePoints, double earnedPoints){

    this.name = name;
    this.avaliablePoints = avaliablePoints;
    this.earnedPoints = earnedPoints;
  }
  
  public Assignment(){

  }

  public String getName(){
    return name;
  }
  public double getAvaliablePoints(){
    return avaliablePoints;
  }
  public double getEarnedPoints(){
    return earnedPoints;
  }

  public void setName(String n2){
    name = n2;
  }
  public void setAvaliablePoints(double d2){
    avaliablePoints = d2;
  }
  public void setEarnedPoints(double d2){
    earnedPoints = d2;
  }

  public static double average(ArrayList<Assignment> assignments){

    double e = 0;
    double a = 0;

    for (int i = 0; i < assignments.size(); i++){

      e += assignments.get(i).getEarnedPoints();
      a += assignments.get(i).getAvaliablePoints();
    }

    return (e/a) * 100;
  }
}