public class SortertLenkeliste<T extends Comparable<T>> extends Lenkeliste<T>{



    public void leggTil(T x){
        Node nyNode = new Node(x);
        Node temp = hode;
        if (hode == null){ //needs to be in here b/c of NullPointer
            super.leggTil(nyNode.data);
            return;
        }
        int result=0;
        for(int i=0; i < super.stoerrelse(); i++){
            result = temp.data.compareTo(nyNode.data); //compares temp.data to x and stores in result
            if (result > 0){ //if temp is larger than x, we insert nyNode here
                super.leggTil(i, nyNode.data);
                return;
            }
            if (temp.neste == null){//last element gets inserted at the back with index i+1
                super.leggTil(i+1, nyNode.data);
                return;
            }
            temp = temp.neste;
        }

    }

// Removes last element (same as taAv, but since they're not directly related we cant access that...)
    @Override
    public T fjern(){
        if(length > 0){
            Node temp = hode;
            Node prev = hode;
            hode = temp;
            for (int i = 0; i<length-1; i++){ //iterates through until last element
                prev = temp;
                temp = temp.neste;
            }
            prev.neste = null; //cuts off last element
            hale = prev;
            length--;
            return temp.data;
        }else{
            throw new UgyldigListeIndeks(-1);
        }
    }

    @Override
    public void sett(int pos, T x) throws UnsupportedOperationException{
        throw new UnsupportedOperationException();
    }

    @Override
    public void leggTil(int pos, T x) throws UnsupportedOperationException{
        throw new UnsupportedOperationException();
    }
}
