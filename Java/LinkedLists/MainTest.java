public class MainTest{
    public static void main(String[] args){
        int a;
        int b;
        int c = -1;
        a = c;
        b = a;
        b = 3;
        // System.out.println("If 3, a changes with b, not if 1. a = "+a);

// These two examples are contradicting eachother...
// The only differentce is that the above changes the whole object
// whereas below we change an atttribute to the object

        TestNode<String> newTestNode = new TestNode <String>("new onew");
        TestNode<String> head;
        TestNode<String> tail;
        head = newTestNode;
        tail = head;
        TestNode<String> newnewTestNode = new TestNode <String>("new new onew");
        tail.neste = newnewTestNode;
        // tail = newnewTestNode;

        // System.out.println(newTestNode.ting);
        // System.out.println(head.ting);
        // System.out.println(tail.ting);
        // System.out.println(head.neste.ting); //this answers my question about hode
        // System.out.println(tail.neste.ting);




        Lenkeliste<String> newLenkeliste = new Lenkeliste<String>();
        newLenkeliste.leggTil("first string inserted");
        newLenkeliste.leggTil(1, "second string inserted");
        newLenkeliste.fjern(1);
        String str1 = "number 1";
        String str2 = "number 2";
        int res = str1.compareTo(str2);
        System.out.println("Result of comapre is:"+res);



        // System.out.println(newLenkeliste.hent(0));
        // System.out.println(newLenkeliste.hent(2));
        // newLenkeliste.leggTil("third string inserted");
        // newLenkeliste.leggTil(3, "fourth string inserted");
        // newLenkeliste.sett(0, "fifth string insterted");
        // newLenkeliste.sett(2, "sixth string insterted");
    }

}
