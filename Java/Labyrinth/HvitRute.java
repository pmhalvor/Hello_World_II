public class HvitRute extends Rute{

    public HvitRute(int r, int k){
        super(r, k);
    }

    @Override
    public String charToTegn(){
        return ".";
    }

    @Override
    public String typ(){
        return "h";
    }


    @Override
    public boolean erAapning(){
        return false;
    }
}
