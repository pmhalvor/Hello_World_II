public class Node{

    private long memorySize=0;
    private int processorAmount=0; // Both mS and pA are private so that external methods cannot change them


    public Node(int memorySize, int processorAmount){
        this.memorySize = memorySize;
        this.processorAmount = processorAmount; //sets values for mS and pA given parameters
    }

    public int totalProcessors(){
        return processorAmount;
    }

    public long memSize(){
        return memorySize;
    }
}
