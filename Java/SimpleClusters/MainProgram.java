import java.io.FileNotFoundException;

public class MainProgram{
    public static void main(String[] args){

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
