public class Stabel<T> extends Lenkeliste<T>{

    public void leggPaa(T x){
        //this is what my previous leggTil() does. Maybe I misunderstood previous exercise?
        super.leggTil(x);
    }



    public T taAv(){
        //removes last element from list
        if(length > 0){
            Node temp = hode;
            Node prev = temp;
            for (int i = 0; i<length-1; i++){//iterate to the last element
                    prev = temp; //standard next element proccedure
                    temp = temp.neste; //goes to next element, even though i hasnt gottenthat far yet
            }
            prev.neste = null;
            hale = prev; //cut off last element
            length--;
            return temp.data; //returns item at last index
        }else{
            throw new UgyldigListeIndeks(-1);
        }
    }
}
