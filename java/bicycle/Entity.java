package bicycle;

import java.util.*;

public class Entity {
    private List<Integer> rank = new ArrayList<>(){
        {add(1);add(2);add(3);add(4);}
    };
    private Map<Integer, String> color = new HashMap<>(){
        {put(1, "红");put(2,"紫");put(3,"蓝");put(4,"绿");}
    };

    public Entity(){

    }

    @Override
    public String toString() {
        return "{" +
                "名次=" + rank +
                ", 颜色=" + color.values() +
                '}';
    }

    public List<Integer> getRank() {
        return rank;
    }

    public void setRank(List<Integer> rank) {
        this.rank = rank;
    }

    public Map<Integer, String> getColor() {
        return color;
    }

    public void setColor(Map<Integer, String> color) {
        this.color = color;
    }
}
