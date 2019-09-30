public class Patient{
    private String name;
    private String personalNumber;
    private static int totalIDs = 0;
    private int thisID;
    private Stabel<Prescription> prescriptionLog = new Stabel<>();

    public Patient(String n, String pn){
        name = n;
        personalNumber = pn;
        thisID = totalIDs++;
    }

    public String getName(){
        return name;
    }

    public int getID(){
        return thisID;
    }

    @Override
    public String toString(){
        return name +"\n  Personal number: " + personalNumber + "\n  ID: " + thisID +  "\n";//
    }

    public Stabel<Prescription> getPrescriptionLog(){
        return prescriptionLog;
    }

    public void addPrescription(Prescription p){
        prescriptionLog.leggPaa(p);
    }
}
