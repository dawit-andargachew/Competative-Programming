class Solution {
  public int distinctAverages(int[] nums) {

    // Lets sort the array and find the average of start and end numbers
    // to keep decimals use List<Float> 
    // and list.size() is number of distnict averages

    Arrays.sort(nums);/// sort array

    List < Float > list = new ArrayList();// store distnict averages
    int start = 0, end = nums.length - 1;
    while (start < end) {
      float average = nums[start] + nums[end];
      average /= 2;

      if (!list.contains(average))// if avearage is not found, add the new average
        list.add(average);

        start++;
        end--;
    }

    return list.size();
  }
}