public class BluePrescription extends Prescription{

    public BluePrescription(Medicine med, Doctor notedDoctor, Patient patient, int refills){
        super(med, notedDoctor, patient, refills);
        super.price = super.price*0.25; //Nullpointer exception... rethink this
        super.color = "Blue";
    }

    @Override
    public String color(){ //Same as in white, could have made this in super.
        return color;
    }


    @Override
    public double priceToPay(){
        return super.price; //price in super changes in construcotr of BluePrescription
    }

    @Override
    public String toString(){ //print out all the info we have on BluePrescription
        return "\nColor:"+color+ " \n Medicine: "+super.getMedicine().getName()+" \n Doctor: "+super.getDoctor()+" Patient: "+super.getPatient()+" Refills: "+refills+" \n Price: " +super.price + "\n";
    }
}
