public class SortRute extends Rute{

    public SortRute(int r, int k){
        super(r, k);
    }

    @Override
    public String charToTegn(){
        return "#";
    }

    @Override
    public String typ(){
        return "s";
    }

    @Override
    public boolean erAapning(){
        return false;
    }
}
