import java.io.FileNotFoundException;

public class MainProgram{
    public static void main(String[] args){
        // ComputerCluster abel = new ComputerCluster(12);
        // int c = 0;
        // for (int a=0; a<650; a++){
        //     Node n = new Node(64, 1);
        //     abel.addNode(n);
        //     if (c<16){
        //         // System.out.println("c="+c);
        //         c++;
        //         Node m = new Node(1024, 2);
        //         abel.addNode(m);
        //     }
        // }
        // int tP = abel.totalProcessors();
        // System.out.println("Total processors " + tP);
        // int mem32 = abel.nodesWithEnoughMemory(32);
        // int mem64 = abel.nodesWithEnoughMemory(64);
        // int mem128 = abel.nodesWithEnoughMemory(128);
        // System.out.println("At least 32: " + mem32);
        // System.out.println("At least 64: " + mem64);
        // System.out.println("At least 128: " + mem128);
        // System.out.println("Nmber of racks: " + abel.numOfRacks());

        ComputerCluster readAbel = new ComputerCluster("regneklynge.txt"); //1 works (kinda), 2 works, 3 works, 4 works
        int totProcessors = readAbel.totalProcessors();
        int mem32 = readAbel.nodesWithEnoughMemory(32);
        int mem64 = readAbel.nodesWithEnoughMemory(64);
        int mem128 = readAbel.nodesWithEnoughMemory(128);
        System.out.println("At least 32 GB: " + mem32);
        System.out.println("At least 64 GB: " + mem64);
        System.out.println("At least 128 GB: " + mem128);  
        System.out.println("Total racks: " + readAbel.numOfRacks());
    }
}
