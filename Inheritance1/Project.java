public class Project extends Assignment{

  private String dueDate;
  private boolean groups;

  public Project(String name, double avaliblePoints, double earnedPoints, String dueDate, boolean groups){
    this.dueDate = dueDate;
    this.groups = groups;
  }

  public String getDueDate(){
    return dueDate;
  }
  public boolean getGroups(){
    return groups;
  }

  public void setDueDate(String due2){
    dueDate = due2;
  }
  public void setGroups(boolean b2){
    groups = b2;
  }
}