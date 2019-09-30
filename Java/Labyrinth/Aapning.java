public class Aapning extends HvitRute{
    // Spesielle tilfele av en HvitRute der enten rad eller kolonne == grenser(edges)

    public Aapning(int r, int k){
        super(r, k);
    }

    @Override
    public boolean erAapning(){
        return true;
    }
}
