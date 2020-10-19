package bicycle;

import java.util.*;
public class TestCX {
    /*
    * Mike, Ellie, Rohan, Fatma四个人参加自行车比赛,分别获得1-4名,
    他们每个人骑不同颜色的自行车（红，紫，蓝，绿）。基于以下线索，谁获得了第二名？
    Ellie骑紫色的车，Rohan没有骑绿色的车。
    Mike和Ellie不是第一，也不是最后。
    骑蓝色车的人领先Fatma。
    骑绿色车的人领先骑紫色车的人。
    * */

    public static void main(String[] args) {
        cx();
    }

    public static void cx() {
        List<Entity> entityList = new ArrayList<>();
        Entity Mike = new Entity();
        Entity Ellie = new Entity();
        Entity Rohan = new Entity();
        Entity Fatma = new Entity();
        entityList.add(Mike);
        entityList.add(Ellie);
        entityList.add(Rohan);
        entityList.add(Fatma);

        //Ellie骑紫色的车
        Ellie.getColor().remove(1);
        Ellie.getColor().remove(3);
        Ellie.getColor().remove(4);
        Mike.getColor().remove(2);
        Rohan.getColor().remove(2);
        Fatma.getColor().remove(2);

        //Rohan没有骑绿色的车
        Rohan.getColor().remove(4);

        //Mike和Ellie不是第一，也不是最后。
        Mike.getRank().remove(new Integer(1));
        Mike.getRank().remove(new Integer(4));
        Ellie.getRank().remove(new Integer(1));
        Ellie.getRank().remove(new Integer(4));
        Rohan.getRank().remove(new Integer(2));
        Rohan.getRank().remove(new Integer(3));
        Fatma.getRank().remove(new Integer(2));
        Fatma.getRank().remove(new Integer(3));

        //骑蓝色车的人领先Fatma。
        //Fatma 不是蓝色
        Fatma.getColor().remove(3);
        //Fatma 不是第一
        Fatma.getRank().remove(new Integer(1));

        //因为Fatma是第四 所以其他人删除第四
        Rohan.getRank().remove(new Integer(4));

        //骑绿色车的人领先骑紫色车的人。

        //Fatma 只有第四 不能领先别人  所以Fatma不是绿色
        Fatma.getColor().remove(4);

        //Fatma只剩下红色  所以其他人红色删除
        Mike.getColor().remove(1);
        Rohan.getColor().remove(1);

        //其他三人颜色都唯一确定  所以Mike只能是绿色
        Mike.getColor().remove(3);

        //骑绿色车的人领先骑紫色车的人。所以Mike第二 Ellie第三
        Mike.getRank().remove(new Integer(3));
        Ellie.getRank().remove(new Integer(2));

        System.out.println("Mike:"+Mike);
        System.out.println("Ellie:"+Ellie);
        System.out.println("Rohan:"+Rohan);
        System.out.println("Fatma:"+Fatma);
    }
}
