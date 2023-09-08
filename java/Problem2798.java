public class Problem2798 {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
       int n=0;
        for (int hour : hours) {
            if (hour >= target) {
                n += 1;
            }
        }
        return n;
    }
}
