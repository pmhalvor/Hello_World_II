public class MilitaryPrescription extends WhitePrescription{

    public MilitaryPrescription(Medicine med, Doctor notedDoctor, Patient patient, int refills){
        super(med, notedDoctor, patient, refills); //make sure to do eveerything in super's constructor as well
        super.price = 0.; //Military gets free meds so we change the price to zero
    }

    @Override
    public String toString(){
        return "Color: "+color+ " Type: Military \n Medicine: "+med.getName()+" \n Doctor: "+super.getDoctor().getName()+" \n Patient ID: "+super.getPatient()+" \n Refills: "+refills+" \n Price: " +super.price;
    }
}
