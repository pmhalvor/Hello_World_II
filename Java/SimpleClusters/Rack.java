
public class Rack{

    private static int maxNodes=0; //private so outside methods can't change it, static so all Rack types will have the same maxNodes after it's decided.
    private int index = 0; //keeps track of last element in rack
    public Node [] rack; //Here we make a list that holds Nodes called rack


    public Rack(int mN){
        if (this.maxNodes == 0){
            maxNodes = mN; // if maxNodes hasn't been decided, we set it one time
        }
        rack = new Node[maxNodes]; //makes list of Nodes with maxNodes amount of availble spaces
    }

    public void addNode(Node n){
            rack[index] = n; //This is a primitive way to keep track of where the next open spot in rack is. Not very flexible, but it works for this assignment
            index++;
    }

    public int length(){//To exclude NullPointerExceptions in ComputerCluster.addNode()
        try{
            Boolean b = (rack.length > 0);
            return rack.length;
        }catch(Exception e){
            return 0;
        }
    }

    public int index(){
        return this.index;
    }

}

// I think this one is 100% correct, but who knows. Matybe I misunderstood something here too, which is making the others very confusing for me.
