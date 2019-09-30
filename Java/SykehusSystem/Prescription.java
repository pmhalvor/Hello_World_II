public abstract class Prescription{
    private int prescriptionID;
    private Doctor notedDoctor;
    private Patient patient;
    protected Medicine med;
    protected int refills;
    protected String color;
    protected double price=0;

    public Prescription(Medicine med, Doctor notedDoctor, Patient patient, int refills){
        /*
        Assign all the parameters to the respective variables in class
        */
        this.med = med;
        this.notedDoctor = notedDoctor;
        this.patient = patient;
        this.refills = refills;
        price = med.getPrice();
    }

/*
These methods are pretty self-explainartory. Each returns their respective variables for any other class to see and access
*/

    @Override
    public String toString(){
        return "Medicine: " + med.getName() + ", Doctor: " +notedDoctor.getName() + ", Patient: " + patient.getName() + ", refills left: "+refills+ "\n";
    }

    public int getID(){
        return prescriptionID;
    }

    public Medicine getMedicine(){
        return med;
    }

    public Doctor getDoctor(){
        return notedDoctor;
    }

    public Patient getPatient(){
        return patient;
    }

    public int getNumberLeft(){
        return refills;
    }

    public boolean use(){
        /*
        When there are no more refills allowed, this will return false, otherwise, every use with deduct one form refills
        */
        if(refills <= 0){
            return false;
        }
        refills -=1;
        return true;
    }


/*
Both of these methods are overwritten in subclasses, although it would be simpler to have here with variabels that change according to the subclass.
*/
    abstract public String color();

    abstract public double priceToPay();
}
