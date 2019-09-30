public class WhitePrescription extends Prescription{
    public WhitePrescription(Medicine med, Doctor notedDoctor, Patient patient, int refills){
        /*
        Call constructor of super to makes sure all the arguments from there are executed before calling any new ones
        */
        super(med, notedDoctor, patient, refills);
        super.color = "white"; //sets color to white
    }

    @Override
    public String color(){ //Since i made color a variable in Prescription, I could have just had this method in precription, but the exercise asked specifically for an abstract method there that is to be ovveriden in the subclasses
        return color;
    }

    @Override
    public double priceToPay(){
        return super.price; //price is a varible in the super class which will change accornding to which white prescription is created. If none is assigned, then the price will remain the same.
    }

    @Override
    public String toString(){ //prints all the information we have on white prescriptions
        return "Color:"+color+ " Type: Not Defined \n Medicine: "+med.getName()+" \n Doctor: "+super.getDoctor().getName()+" \n Patient ID: "+super.getPatient()+" \n Refills: "+refills+" \n Price: " +super.price;
    }
}
