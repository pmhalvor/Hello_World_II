public class Medicine{
    protected Double price;
    private String name;
    private Double substance;
    private int id;
    private static int counter = 0;

    public Medicine(String name, double price, double substance){
        /*
        Assign all the parameters to the respective variables in class
        */
        this.name = name;
        this.price = price;
        this.substance = substance;
        id = counter++;
    }

    public int getID(){
        return id;
    }
    public String getName(){
        return name;
    }
    public double getPrice(){
        return price;
    }
    public double getSubstance(){
        return substance;
    }
    public void setNewPrice(double price){
        /*
        Change the price to new price given as paramter
        */
        this.price = price;
    }

    public String getType(){
        return "";
    }
}
