import java.util.List;

public class Problem2824 {
    public int countPairs(List<Integer> nums, int target) {

        int count=0;
        for(int i=0;i<nums.toArray().length;i++){
            for (int j=i+1;j<nums.toArray().length;j++){
                if (nums.get(i) + nums.get(j)<target){
                    count+=1;
                }
            }
        }
        return count;
    }
}
