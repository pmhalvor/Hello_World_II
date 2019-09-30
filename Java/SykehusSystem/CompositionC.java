public class CompositionC extends Medicine{
    public CompositionC(String name, double price, double substance){
        /*
        Calls constructor in Medicine
        */
        super(name, price, substance);
    }


    @Override
    public String toString(){//provides all the info we have on this Composition
        return  super.getName() + ", price:" + super.getPrice() + ", subtance:"+ super.getSubstance()+"\n";
    }

    @Override
    public String getType(){
        return "c";
    }
}
