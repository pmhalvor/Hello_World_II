import java.util.Scanner;

public class Doctor implements Comparable<Doctor>{
    private String name;
    protected int controlID = 0;
    private Lenkeliste<Prescription> writtenPrescriptions = new Lenkeliste<>();

    public Doctor(String name){
        /*
        Assign all the parameters to the respective variables in class
        */
        this.name = name;
    }

    @Override
    public int compareTo(Doctor doc){
        if (this.name.compareTo(doc.getName()) < 0){
            return -1;
        } else if(this.name.compareTo(doc.getName()) > 0){
            return 1;
        }
        return 0;
    }

    public String getName(){
        return name;
    }

    @Override
    public String toString(){ //all the current info we have on doctor
        String toReturn = name;
        return name + "\n";
    }

    public Prescription writePrescription(Medicine medicine, Patient patient, int numberLeft) throws IllegalPrint{
        /*
        This method asks the program users questions to decide which prescription to write.
         If color == white, the user will be asked if it should be military or prevention.
         When all the needed information is recieved, the correct prescription will be returned.
         Returns null if none of the if's catch
        */
        Prescription writtenPrescription = null;
        if(medicine instanceof CompositionA && controlID == 0){
            throw new IllegalPrint(this, medicine);
        }
        boolean validInput1 = false;
        while (!validInput1){ //will only become valid when the first letter of input equals w or b
            System.out.println("White (Military or Prevention) or Blue prescription?");
            Scanner keyboard = new Scanner(System.in);
            String input = keyboard.nextLine();
            input = input.toUpperCase();
            if (input.charAt(0) == 'W'){ //since we're comparing chars, we have to use single quotations.
                validInput1 = true;
                System.out.println("White prescription registered");
                boolean validInput2 = false;
                while (!validInput2){//will only become valid if first letter of input equals m or p
                    System.out.println("Military or Prevention?");
                    keyboard = new Scanner(System.in);
                    input = keyboard.nextLine().toUpperCase();
                    if (input.charAt(0) == 'M'){ //single quotations
                        validInput2 = true;
                        System.out.println("Military registered");
                        writtenPrescription = new MilitaryPrescription(medicine, this, patient, numberLeft);
                    }
                    else if(input.charAt(0) == 'P'){ //single quotations
                        validInput2 = true;
                        System.out.println("Prevention registered");
                        writtenPrescription = new PPrescription(medicine, this, patient, numberLeft);
                    }
                    else{
                        System.out.println("Error: Invalid entry. Please try again.");
                    }
                }
            }

            else if (input.charAt(0) == 'B'){ //single quotations
                validInput1 = true;
                System.out.println("Blue prescription registered");
                writtenPrescription = new BluePrescription(medicine, this, patient, numberLeft);
            }

            else{
                System.out.println("Error: Invalid entry. Please try again.");
            }
        }
        writtenPrescriptions.leggTil(writtenPrescription);
        patient.addPrescription(writtenPrescription);
        return writtenPrescription;
    }

    public void addPrescription(Prescription p){
        writtenPrescriptions.leggTil(p);
    }

    public Lenkeliste<Prescription> getWrittenPrescritptions(){
        return writtenPrescriptions;
    }

    public String writtenPrescriptionsToString(){
        String toReturn = "";
        /*
        This isn't done yet. Finish when you've written the rest of written prescription
        */
        return toReturn;
    }


}
