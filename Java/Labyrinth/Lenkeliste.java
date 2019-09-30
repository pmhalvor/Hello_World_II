import java.util.Iterator;

public class Lenkeliste<T> implements Liste<T>{
    protected Node hode; //protected to be alble to be used in subclasses later
    protected Node hale;//protected to be alble to be used in subclasses later
    protected int length = 0;
    // private Node rump; //since tail will represent the space behind the last, i want a Node representing the last element in the list as well.

    protected class Node{ //protected to be alble to be used in subclasses later
        Node neste = null; //Doesnt need to be static because they can be placed anywhere in the Lenkeliste
        T data; //The actual object in our Lenkeliste
        Integer index; //The index of this specific node, to be determined upon insert

        Node(T data){
            this.data = data;
            }
    }

    public Iterator<T> iterator(){
        return new LenkelisteIterator();
    }

    public class LenkelisteIterator implements Iterator<T>{
        Node thisNode;

        public LenkelisteIterator(){
            thisNode = hode;
        }

        public boolean hasNext(){
            return thisNode != null;
        }

        public T next(){
            Node temp = thisNode;
            thisNode = thisNode.neste;
            return temp.data;
        }

        public void remove(){
            fjern(thisNode.index);
        }
    }

    public int stoerrelse(){
        return length; //length is updated everytime a new leggTil() is called
    }

    public boolean erTom(){
        return hode == null; //hode is updated the first time leggTil is called
    }

    public boolean gyldigIndeks(int pos){
        return pos < length && pos >=0; //makes sure pos is within the lists limits
    }

    public void leseListe(){ //for my own testing purposes
        Node temp = hode;
        for (int i=0; i<length; i++){
            System.out.println(temp.data + " has index: "+temp.index);
            temp = temp.neste;
        }
    }
    public void checkHodeAndHale(){ //for my own testing purposes
        System.out.println(hode.data + " = hode");
        System.out.println(hale.data + " = hale");

    }

    public void leggTil(T x){
        Node nyNode = new Node(x);
        Node temp = hode;
        Node prev = hode;
        length++;
        if(erTom()){  //Setting the first element in Lenkeliste
            nyNode.index = 0;
            hode = nyNode;
            hale = hode;
            return;
        }else{ //Setting the next element in Lenkeliste
            nyNode.index = length-1;
            hale.neste = nyNode; //current last element now points to nyNode
            hale = nyNode; //tail is set to last element in Lenkeliste
        }
    }

    public void leggTil(int pos, T x) throws UgyldigListeIndeks{
        Node nyNode = new Node(x);
        length++;
        if(erTom() && pos != 0){ //to avoid nullPointer exception
            length--; //Needed to keep length++ above, so this changes length back to both method was called
            throw new UgyldigListeIndeks(pos); //might be special case specified in assignment text
        }else if(erTom() && pos == 0){ //This was needed to pass a specific test
            nyNode.index = pos;  // pos = 0 as checked for above
            hode = nyNode;
            hale = hode;

        }else if(gyldigIndeks(pos)){ //Can leggTil() at exactly back of array, or anywhere already defined, but no wheree else.
            //set in and push current element back one
            Node curr = hode;
            Node prev = hode;
            hode = curr; //Now hode is pointing at curr, which is a replica of the values of hode before. This will not change as curr changes later in for-loop
            int stop = length-1;
            if (pos == length-1){
                stop++;
            }
            for(int i = 0 ; i < stop; i++){ //Since length is increased when new Node() is created, this for-loop will go up to the correct length
                if(i == pos && pos == length-1){
                    curr = nyNode;
                    curr.index = pos; //needed to make sure teh index changes
                    prev.neste = curr;
                    prev = curr;
                }
                else if(curr != null && curr.index == pos){ //avoids nullPointer and finds element at current index
                    nyNode.neste = curr; //pushes the current element back one
                    curr = nyNode;
                    curr.index = pos;
                    if(pos!=0){ //only for elements after teh first one in the list, since the first won't have a previous
                        prev.neste = curr;
                    }else{
                        hode = curr;
                    }
                    prev = curr; //the regular updating after the new element is inserted
                    curr = curr.neste;
                    nyNode = null;
                }
                // System.out.println(curr.data + " has index" + curr.index);
                if(nyNode == null){
                    curr.index += 1; //Changes the indices after newly inserted Node
                }

                if(curr != null){
                    prev = curr; //iterates until the end of list when curr will be pointing a null
                    curr = curr.neste;
                }
            }
            hale = prev; //need to keep hale since I used it in my first leggTil(). Need to restructure that if I have time.

        }else{
            length--; //removing the length+++ from earlier since no new element will be added
            throw new UgyldigListeIndeks(pos);
        }

    }

    public void sett(int pos, T x) throws UgyldigListeIndeks{
        Node nyNode = new Node(x);
        Node temp = hode;
        Node prev = hode;
        hode = temp; //makes sure the new head gets updated with our newly relinked elements
        if(gyldigIndeks(pos)){
            for(int i=0; i<length; i++){
                if(temp.index == pos){
                    temp.data = nyNode.data; //the only thing that will change with this Node is it's data, this makes it simpler
                }
                prev = temp;
                temp = temp.neste;
            }
            hale = prev; //keeps hale in the correct list
        }else{
            throw new UgyldigListeIndeks(pos);
        }
    }



    public T hent(int pos){ //this could have return a node, if the nodes had a forrige we could access. Would have made fjern() easier
        Node temp = null; //needed to make sure toReturn was initialized for compiling
        if(gyldigIndeks(pos)){
            //need a for loop starting at head, and going to each neste until correct temp.index
            temp = hode;
            for (int i = 0; i<pos; i++){ //iterates to the correct position
                temp = temp.neste;
            }
            return temp.data;
        }else{
            throw new UgyldigListeIndeks(pos);
        }
    }


    public T fjern(int pos){
        T toReturn = null;
        Node temp = hode;
        Node prev = hode;
        boolean changed = false;
        if(gyldigIndeks(pos)){
            for (int i = 0; i<length-1; i++){
                if (temp != null){ //to prevent NullPointer
                    if(temp.index == pos){
                        prev.neste = temp.neste; //rerouting previous elements neste to current temp.neste
                        toReturn = temp.data;
                        changed = true; //in order to update the indices after this element in list
                    }
                    if(changed){ //updating the rest of the indices
                        temp.index -=1;
                    }
                    prev = temp; //standard next element proccedure
                    temp = temp.neste; //these could have been made into their own method...
                }
            }

            if(!changed && temp != null){ //last element is being removed here b/c of problems with not having length-1 above
                toReturn = temp.data;
                prev.neste = null; //prev now loses his next, ie cutting off last element from list
            }
            hale = prev;
            length--; //updating length since we removed an element
            return toReturn;
        }else{
            throw new UgyldigListeIndeks(pos);
        }
    }


    public T fjern() throws UgyldigListeIndeks{
        if(length > 0){
            T toReturn = hode.data;
            Node temp = hode;
            Node prev = hode;
            hode = temp.neste;//removing the first element in the list b/c FIFO requested in project text
            for (int i = 0; i<length; i++){
                temp.index -=1; //updating rest of indices
                prev = temp; //standard next element proccedure
                temp = temp.neste;
            }
            hale = prev;
            length--;
            return toReturn;
        }else{
            throw new UgyldigListeIndeks(-1);
        }
    }




}
