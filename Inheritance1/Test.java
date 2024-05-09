public class Test extends Assignment{

  private String testDate;

  public Test(String name, double avaliblePoints, double earnedPoints, String testDate){
    this.testDate = testDate;
  }

  public String getTestDate(){
    return testDate;
  }
  
  public void setTestDate(String s2){
    testDate = s2;
  }
}