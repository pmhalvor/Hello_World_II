public class CompositionB extends Medicine{
    private int strength;

    public CompositionB(String name, double price, double substance, int strength){
        /*
        Calls constructor in Medicine as well as assigns new variable strength to given parameter
        */
        super(name, price, substance);
        this.strength = strength;
    }
    public int getNarcoticStrength(){
        return strength;
    }


    @Override
    public String toString(){ //provides all the info we have on this Composition
        return  super.getName() + ", price:" + super.getPrice() + ", subtance:"+ super.getSubstance()+ ", strength:"+strength+"\n";
    }

    @Override
    public String getType(){
        return "b";
    }

}
