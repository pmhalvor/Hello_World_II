public class PPrescription extends WhitePrescription{

    public PPrescription(Medicine med, Doctor notedDoctor, Patient patient, int refills){
        /*
        Call constructor of super to get all the arguments from that before giving any new ones
        */
        super(med, notedDoctor, patient, refills);
        if (super.price > 108){ //This clause makes sure the price never falls below zero
            super.price -= 108;
        }else{
            super.price = 0.;
        }
        super.refills = 3;
    }

    @Override
    public String toString(){ //prints all info of PPrescription to string
        return "Color:"+color+ " Type: Prevention \n Medicine: "+med.getName()+" \n Doctor: "+super.getDoctor().getName()+" \n Patient ID: "+super.getPatient()+" \n Refills: "+refills+" \n Price: " +super.price;
    }

}
