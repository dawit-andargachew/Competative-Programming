class Solution {
  public int countStudents(int[] students, int[] sandwiches) {
      // how do we know the number of students who are unable to eat?
      // just count the number_of_changes, if the number_of_changes >= stud.size()
      //            we add every student to the end of the queue and no one get sandwitch

     // RULE: Everytime a student gets sandwich number_of_changes is set to zero.

     // like students = [1,1,1,0,0,1], sandwich = [1,0,0,0,1,1]
     // after several iterations we get 
     //     students = [1,1,1], sandwiches = [0,1,1]
     //     number_of_changes = 3, so no one will get sandwith

    Stack < Integer > stud = new Stack();
    Stack < Integer > sand_w = new Stack();

    int len = students.length;
    // copy sandwich to stack
    for (int i = len - 1; i >= 0; i--)
      sand_w.add(sandwiches[i]);

    // copy student to stack
    for (int i = len - 1; i >= 0; i--)
      stud.add(students[i]);

    int number_of_changes = 0;
    // control the number_of_changes
    while (stud.size() > 0) {
      if (stud.peek() == sand_w.peek()) {
        stud.pop();
        sand_w.pop();
        number_of_changes = 0;// number_of_changes must be set to zero, everytime the student gets sandwich
      } else {
        int c = stud.pop();
        stud.add(0, c);
        number_of_changes++;// increment to controll the number of changes
      }
      if (number_of_changes >= stud.size())// number_of_changes >= stud.size() => repeating the process does't make change
        break;
    }

    return stud.size();
  }
}