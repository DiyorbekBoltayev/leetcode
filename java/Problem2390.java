import java.lang.reflect.Array;
import java.util.List;
import java.util.Objects;
import java.util.Stack;

public class Problem2390 {
    public String removeStars(String s) {
        Stack<Character> d=new Stack<>();
        for (int i=0;i<s.length();i++){
            if (s.charAt(i)!='*'){
                d.push(s.charAt(i));
            }else {
                d.pop();
            }
        }
        StringBuilder r = new StringBuilder();
        while (!d.isEmpty()) {
            r.append(d.pop());
        }
        return r.reverse().toString();



    }


}
