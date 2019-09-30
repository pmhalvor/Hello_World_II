import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;


public class ComputerCluster{
    ArrayList<Rack> cluster = new ArrayList<Rack>(); //Here we make a list that holds Racks called cluster
    // public int clusterSize = 64;
    private int rackSize; //define a local varible that keeps tracks of this cluster's rack's size
    private int numberOfProcessors=0; //to be updated along the way
    private int numberOfRacks=0; //to be updated along the way
    private int indexCC=0; //keeps track of the next empty spot in the cluster

    public ComputerCluster(int rackSize){
        this.rackSize = rackSize;
        Rack firstRack = new Rack(rackSize); //Call rack to set standard maxNodes for racks in this cluster
        cluster.add(firstRack); //might as well add this rack to our cluster to start off with
        indexCC++; numberOfRacks++;
    }

    public ComputerCluster(String filename){
        //This portion attempts to store the contents in filename in the object scanner
        Scanner scanner;
        try{
            scanner = new Scanner(new File(filename));
        }catch(FileNotFoundException fnf){
            System.out.println("cannot find file");
            return;
        }

        this.rackSize = scanner.nextInt(); //The first line of the text files inholds the rackSize for that cluster
        Rack firstRack = new Rack(rackSize); //Call rack to set standard maxNodes for racks in this cluster
        cluster.add(firstRack); //might as well add this rack to our cluster to start off with
        indexCC++; numberOfRacks++;

        int amount;
        int memory;
        int processors; //defines variables that will be read in each line of file

        while (scanner.hasNextInt()){ //checks that there are more integers in the file
            scanner.nextLine();
            amount = scanner.nextInt();
            memory = scanner.nextInt();
            processors = scanner.nextInt();

            for (int a=0; a<amount; a++){
                Node n = new Node(memory, processors);
                addNode(n); //calls addNode for current ComputerCluster
            }

        }

    }

    public void addNode(Node n){
        Boolean added = false;  //Bool that will be used to see if current Node has been added
        Boolean lastNodeInRackEmpty = (cluster.get(indexCC-1).rack[rackSize-1]==null); //checks is last index of rack a null object
        if(!lastNodeInRackEmpty){
            Rack newRack = new Rack(0); //Rack has to be called with an int. Doesnt matter though since maxNodes will only change if it equals zero
            cluster.add(newRack);
            indexCC ++; numberOfRacks++;
        }
        for (Rack r : cluster){
            for (int i=0; i<r.length(); i++){
                if (r.rack[i] == null){ //when we find an empty space for a Node
                    r.addNode(n);
                    numberOfProcessors += n.totalProcessors();
                    added = true;
                    break;
                }
            }
            if (added){ // This means the node has been added and we are done with for loop for now
                break;
            }
        }
    }


    public int totalProcessors(){
        return numberOfProcessors; //numberOfProcessors is updated every time we add a Node.
    }

    public int nodesWithEnoughMemory(long neededMemory){ 
        int counter = 0;
        for(Rack r : cluster){
            if (r.rack != null){
                for (int j=0; j<r.index(); j++){
                    if(r.rack[j].memSize() >= neededMemory){
                        counter += 1;
                    }
                }
            }
        }
        return counter;
    }

    public int numOfRacks(){
        return numberOfRacks;
    }

}


/*

**FIXED** I need to find out why there are so many counted processors. Maybe make a variable
That keeps track of the processcors in here. Or maybe just fix what ever math error is up there
(there are only 16 extra from the expected, it could be because of the extra 16  we added. Maybe
im adding them twice? (there was no error here. there are supposed to be 682 proc)

**FIXED** Any way, theres also a nullpointer problem here at the end of these for loops.
Im guessing its because the last rack doesnt end up being full. We need to
somehow make a test for this (my && r.rack[j] != null atttempt did not work)
((My attempt did work, I just needed to make the clause before taking in r.rack.length()))

**FIXED** other than that, we'll also still need to finish E. Having trouble with Exceptions. (You have a
method that both throws and trys/catches Exception. You need to decide which is neccassary beforehand)


-P

Tips:
Learn and use java.util.list and java.util.array

You can create a Javadoc which you can load as a webpage to see another apporach to seperating datastructure drawings.

*/
