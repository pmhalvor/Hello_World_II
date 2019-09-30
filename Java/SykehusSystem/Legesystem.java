import java.util.*;
import java.io.*;

public class Legesystem{
    // Opprett lister som lagrer objektene i legesystemet
    public static Lenkeliste<Patient> patientLog = new Lenkeliste<>();
    public static Lenkeliste<Medicine> medicineLog = new Lenkeliste<>();
    public static SortertLenkeliste<Doctor> doctorLog = new SortertLenkeliste<>();
    public static Lenkeliste<Prescription> prescriptionLog = new Lenkeliste<>();



    public static void main(String[] args){
        File minFil = new File("inndata.txt");
        lesFraFil(minFil);
        commandLoop();
    }

    private static void commandLoop(){
        boolean avslutt = false;
        while(!avslutt){
            System.out.println("\n\n______HOVEDMENY____\n");
            System.out.println("Velg fra alternativene: \n");
            System.out.println("    1: Skriv ut fullstendig oversikt");
            System.out.println("    2: Legg til ny elementer");
            System.out.println("    3: Bruk en resept");
            System.out.println("    4: Se statistikkene for systemet");
            System.out.println("    5: Avslutt");

            Scanner keyboard = new Scanner(System.in);
            String input = keyboard.nextLine();
            Integer inn = null;
            try{ //Her sjekker vi at det ble oppgitt en integer. Hvis ikke begynner whileløkken igjen
                inn = Integer.parseInt(input);
            }catch(Exception e){
                System.out.println("Invalid input, try again");
                continue;
            }


            if(inn == 1){
                // Skriver ut alle elementer i systemet
                System.out.println(everythingToString());
            }
            if(inn == 2){
                // leggtil noe
                addSomething();
            }
            if(inn == 3){
                // bruk resept
                usePrescription();
            }
            if(inn == 4){
                // stats
                showStats();

            }
            if(inn == 5){
                avslutt = true;
            }
        }
    }

    public static void showStats(){
        //Greeting quetion
        System.out.println("Hvilke statistikk vil du se?");
        System.out.println("    0: Vandannende legemidler");
        System.out.println("    1: Narkotisk legemidler");
        System.out.println("    2: Mulige misbrukere av narkotika");

        //Checks for valid input
        Scanner keyboard = new Scanner(System.in);
        String input = keyboard.nextLine();
        Integer inn = null;
        try{
            inn = Integer.parseInt(input);
        }catch(Exception e){
            System.out.println("Ugyldig svar");
            return;
        }
        if (inn>2){
            System.out.println("Ugyldig svar");
            return;
        }


        if(inn == 0 || inn == 1){ //first two alternatives
            int vann = 0;
            int nark = 0;
            for(Prescription p : prescriptionLog){
                if(inn==0){
                    if (p.getMedicine().getType().equals("a")){
                        vann++;
                    }
                }else if(inn==1){
                    if (p.getMedicine().getType().equals("b")){
                        nark++;
                    }
                }
            }
            if(inn==0){
                System.out.println("Antall vanndannende:"+vann);
            }else if(inn==1){
                System.out.println("Antall narkotisk:"+nark);
            }
        }

        //Last alternative
        if (inn == 2){

            // Check doctors first
            int narkDocCount = 0;
            for (Doctor d : doctorLog){
                for (Prescription p : d.getWrittenPrescritptions()){
                    if (p.getMedicine().getType().equals("b")){
                        narkDocCount++;
                    }
                }
                if(narkDocCount>0){
                    System.out.println(d.getName() + " har skrevet ut " + narkDocCount+ " narkotisk resepter");
                    narkDocCount = 0;
                }
            }

            // Now checking patients
            int narkPatCount = 0;
            for (Patient pat: patientLog){
                for (Prescription p : pat.getPrescriptionLog()){
                    if (p.getMedicine().getType().equals("b")){
                        narkPatCount++;
                    }
                }
                if (narkPatCount>0){
                    System.out.println(pat.getName() + " har " + narkPatCount+ " narkotisk resepter");
                    narkPatCount = 0;
                }
            }
        }



        return;
    }

    public static void usePrescription(){
        //Greeting question
        System.out.println("Hvilke pasient vil du bruke resept for");
        int counter =0;
        for(Patient p : patientLog){
            System.out.println("    " +(counter++) + ": "+ p.getName());
        }

        //Checks for valid input
        Scanner keyboard = new Scanner(System.in);
        String input = keyboard.nextLine();
        Integer answer = null;
        try{
            answer = Integer.parseInt(input);
        }catch(Exception e){
            System.out.println("Vennligst velg en av de øvrige alternativene");
        }
        if (answer > counter){
            System.out.println("Ugyldig svar.");
            return;
        }

        if(answer!=null){
            //Locate the correct patient
            Patient chosenPatient = patientLog.hent(answer);
            System.out.println("\n Valgt pasient: "+ chosenPatient.getName());

            //New question
            System.out.println("Hvilke resept vil du bruke?");
            counter = 0;
            for (Prescription p : chosenPatient.getPrescriptionLog()){
                System.out.println((counter++) + ": "+ p.getMedicine().getName() + "(" + p.getNumberLeft() + " reit)" );
            }

            //Checks valid input
            Scanner keyboard2 = new Scanner(System.in);
            String input2 = keyboard2.nextLine();
            answer = null;
            try{
                answer = Integer.parseInt(input2);
            }catch(Exception e){
                System.out.println("Vennligst velg en av de øvrige alternativene");
            }
            if (answer > counter){
                System.out.println("Ugyldig svar.");
                return;
            }

            //Gets correct prescription
            Prescription chosenPrescription = chosenPatient.getPrescriptionLog().hent(answer);
            if (chosenPrescription.use()){ //method use() was a boolean, came in handy here
                System.out.println("Brukt resept for " + chosenPrescription.getMedicine().getName() + ". Antall reit igjen:" + chosenPrescription.getNumberLeft());
            }else{
                System.out.println("Kunne ikke bruke resept for " + chosenPrescription.getMedicine().getName() +". Ingen reit igjen.");
            }
        }
        return;
    }

    public static void addSomething(){
        boolean validInput = false;
        while(!validInput){  //added looping feature here too for debugging, with exit alternartive if needed
            //Greeting question
            System.out.println("\nHva vil du legge til?");
            System.out.println("    1: Patient");
            System.out.println("    2: Lege");
            System.out.println("    3: Resept");
            System.out.println("    4: Legemiddel");
            System.out.println("    5: Tilbake til hovedmenyen");

            // Checking valid input
            Scanner keyboard = new Scanner(System.in);
            String input = keyboard.nextLine();
            Integer inn = null;
            try{ //Her sjekker vi at det ble oppgitt en integer. Hvis ikke begynner whileløkken igjen
                inn = Integer.parseInt(input);
            }catch(Exception e){
                System.out.println("Invalid input, try again");
                continue;
            }

            if(inn == 1){
                // Skal legge til en Pasient
                System.out.println("Oppgi navn og personnummer separert av et \", \" ");
                Scanner key = new Scanner(System.in);
                String[] info = key.nextLine().split(", ");
                Patient newPatient = new Patient(info[0], info[1]);
                patientLog.leggTil(newPatient);

            }

            if(inn == 2){
                // Skal legge til en lege
                System.out.println("Oppgi navn og evt. kontrollid separert av et \", \" ");
                Scanner key = new Scanner(System.in);
                String[] info = key.nextLine().split(", ");
                Doctor newDoc;
                if (info.length == 1 || info[1].equals("0")){
                    newDoc = new Doctor(info[0]);
                } else {
                    newDoc = new Specialist(info[0], Integer.parseInt(info[1]));
                }
                doctorLog.leggTil(newDoc);
            }

            if(inn == 3){
                // Skal legge til en resept
                System.out.println("Oppgi legen, legemiddel, pasient og reit separert av et \", \"");
                Scanner key = new Scanner(System.in);
                String[] info = key.nextLine().split(", ");

                // Check if Doctor is in system
                Doctor correctDoctor = null;
                for (Doctor d :doctorLog){
                    if(info[0].compareTo(d.getName()) == 0){
                        correctDoctor = d;
                    }
                }
                if(correctDoctor==null){
                    System.out.println("Finner ikke legen, " + info[0] + ", i systemet. Legg den til ved alternativ 2.");
                    return;
                }

                // Check if Medicine is in system
                Medicine correctMedicine = null;
                for (Medicine m : medicineLog){
                    if(info[1].compareTo(m.getName()) == 0){
                        correctMedicine = m;
                    }
                }
                if(correctMedicine==null){
                    System.out.println("Finner ikke legemiddel, " + info[1] + ", i systemet. Legg den til ved alternativ 4.");
                    return;
                }

                // Check if Patient is in system
                Patient correctPatient = null;
                for (Patient p : patientLog){
                    if (info[2].compareTo(p.getName()) == 0){
                        correctPatient = p;
                    }
                }
                if (correctPatient==null){
                    System.out.println("Finner ikke pasient, " + info[2] + ", i systemet. Legg den til ved alternativ 1.");
                }

                // All variables in system, now make prescription
                if(info.length!=4){ //If misssing reit
                    System.out.println("Mangler noe informasjon. Skal oppgi 4 ting; legen, legemiddel, pasient og reit.");
                }

                Prescription newPrescription = null;

                try{ //Needed since writePrescription() throws Exception
                    newPrescription = correctDoctor.writePrescription(correctMedicine, correctPatient, Integer.parseInt(info[3]));
                    System.out.println("Created new prescription");
                }catch(IllegalPrint ip){
                    new IllegalPrint(correctDoctor, correctMedicine);
                }

                prescriptionLog.leggTil(newPrescription);

            }

            if(inn == 4){
                // Skal legge til en legemiddel
                System.out.println("Oppgi navn, type, pris, virkestoff og evt styrken separert av et \", \" ");
                Scanner key = new Scanner(System.in);
                String[] info = key.nextLine().split(", ");
                Medicine newMed = null;
                if (info.length>4){
                    if(info[1].equals("a")){
                        newMed = new CompositionA(info[0], Double.parseDouble(info[2]), Double.parseDouble(info[3]), Integer.parseInt(info[4]));
                    }else if(info[1].equals("b")){
                        newMed = new CompositionB(info[0], Double.parseDouble(info[2]), Double.parseDouble(info[3]), Integer.parseInt(info[4]));
                    }else{
                        System.out.println("Invalid input, try again");
                    }
                }else if(info[1].equals("c")){
                        newMed = new CompositionC(info[0], Double.parseDouble(info[2]), Double.parseDouble(info[3]));
                }else{
                    System.out.println("Invalid input, try again");
                }
                medicineLog.leggTil(newMed);

            }
            if(inn == 5){
                // tilbake til hovedmenyen
                return;
            }
        }
        return;
    }

    public static String everythingToString(){
        String toReturn = "\n  ****** PATIENTS ******\n";
        for (Patient p : patientLog){
            toReturn += p.toString();
        }

        toReturn += "\n  ****** DOCTORS ******\n";
        for (Doctor d : doctorLog){
            toReturn += d.toString();
        }

        toReturn += "\n  ****** MEDICINES ******\n";
        for (Medicine m: medicineLog){
            toReturn += m.toString();
        }

        toReturn += "\n  **** PRESCRIPTIONS ****\n";
        for (Prescription p : prescriptionLog){
            toReturn += p.toString();
        }

        return toReturn;
    }

    private static void lesFraFil(File fil){
        Scanner scanner = null;
        try{
            scanner = new Scanner(fil);
        }catch(FileNotFoundException e){
            System.out.println("Fant ikke filen, starter opp som et tomt Legesystem");
            return;
        }

        String innlest = scanner.nextLine();


        while(scanner.hasNextLine()){

            String[] info = innlest.split(" ");

            // Legger til alle pasientene i filen
            if(info[1].compareTo("Pasienter") == 0){
                Patient p = null;
                while(scanner.hasNextLine()) {
                    innlest = scanner.nextLine();

                    //Om vi er ferdig med å legge til pasienter, bryt whileløkken,
                    //slik at vi fortsetter til koden for å legge til legemiddler
                    if(innlest.charAt(0) == '#'){
                        break;
                    }
                    String deler[] = innlest.split(", ");
                    String navn = deler[0];
                    String fnr = deler[1];
                    p = new Patient(navn, fnr);
                    patientLog.leggTil(p);
                }
            }


            //Legger inn Legemidlene
            else if(info[1].compareTo("Legemidler") == 0){
                while(scanner.hasNextLine()){
                    innlest = scanner.nextLine();
                    //Om vi er ferdig med å legge til legemidler, bryt whileløkken,
                    //slik at vi fortsetter til koden for å legge til leger
                    if(innlest.charAt(0) == '#'){
                        break;
                    }
                    String[] legemiddel = innlest.split(", ");
                    String navn = legemiddel[0];
                    Double pris = Double.parseDouble(legemiddel[2]);
                    Double virk = Double.parseDouble(legemiddel[3]);
                    int  styrke;
                    if(legemiddel[1].compareTo("a") == 0){
                        styrke = Integer.parseInt(legemiddel[4]);
                        CompositionA med = new CompositionA(navn, pris, virk, styrke);
                        medicineLog.leggTil(med);
                    }
                    else if(legemiddel[1].compareTo("b") == 0){
                        styrke = Integer.parseInt(legemiddel[4]);
                        CompositionB med = new CompositionB(navn, pris, virk, styrke);
                        medicineLog.leggTil(med);

                    }else if (legemiddel[1].compareTo("c") == 0){
                        CompositionC med = new CompositionC(navn, pris, virk);
                        medicineLog.leggTil(med);

                    }
                }


            }
            //Legger inn leger
            else if(info[1].compareTo("Leger") == 0){
                while(scanner.hasNextLine()){
                    innlest = scanner.nextLine();
                    //Om vi er ferdig med å legge til leger, bryt whileløkken,
                    //slik at vi fortsetter til koden for å legge til resepter
                    if(innlest.charAt(0) == '#'){
                        break;
                    }
                    info = innlest.split(", ");
                    int kontrollid = Integer.parseInt(info[1]);
                    if(kontrollid == 0){
                        Doctor doc = new Doctor(info[0]);
                        doctorLog.leggTil(doc);
                    }else{
                        Specialist spec = new Specialist(info[0], kontrollid);
                        doctorLog.leggTil(spec);
                    }
                }


            }
            //Legger inn Resepter
            else if(info[1].compareTo("Resepter") == 0){
                while(scanner.hasNextLine()){
                    innlest = scanner.nextLine();
                    info = innlest.split(", ");
                    int legemiddelNummer = Integer.parseInt(info[0]);
                    String legeNavn = info[1];
                    int patientID = Integer.parseInt(info[2]);
                    int reit = Integer.parseInt(info[3]);

                    int lengst = patientLog.stoerrelse();
                    if(lengst < medicineLog.stoerrelse()){
                        lengst = medicineLog.stoerrelse();
                    }
                    if (lengst < doctorLog.stoerrelse()){
                        lengst = doctorLog.stoerrelse();
                    }

                    //
                    // Her må du finne legen, legemiddelet, og pasienten som ligger
                    // i lenkelistene utifra informasjonen.
                    //

                    Doctor docForPrescription = null;
                    Integer docIndex = null;
                    int counter = 0;
                    for(Doctor d : doctorLog){
                        if (legeNavn.compareTo(d.getName()) == 0){
                            docForPrescription = d;
                            docIndex = counter;
                        }
                        counter++;
                    }

                    Medicine medForPrescription = null;
                    for(Medicine m : medicineLog){
                        if (legemiddelNummer == m.getID()){
                            medForPrescription = m;
                        }
                    }

                    Patient patForPrescription = null;
                    for(Patient p : patientLog){
                        if (patientID == p.getID()){
                            patForPrescription = p;
                        }
                    }

                    // Assuming BluePrescription since no other direction is given
                    BluePrescription resept = new BluePrescription(medForPrescription, docForPrescription, patForPrescription, reit);
                    prescriptionLog.leggTil(resept);

                    // Update patients prescriptionlog
                    Patient temp = patientLog.hent(patientID);
                    temp.addPrescription(resept);
                    patientLog.sett(patientID, temp);

                    // Update doctors prescriptionlog
                    if (docIndex != null){
                        Doctor temp2 = doctorLog.hent(docIndex);
                        temp2.addPrescription(resept);
                        doctorLog.fjern(docIndex);
                        doctorLog.leggTil(temp2);
                    }




                    // Dette burde skilles ut i hjelpemetoder leter gjennom listene
                    // og returnerer riktig objekt, ut ifra informasjonen som ble lest inn
                    //
                    // Opprett et reseptobjekt med skrivResept funksjonen i legen,
                    // og legg det til i en lenkeliste
                    //
                    // Dersom legeobjektene dine oppretter PResepter, kan du ignorere reit
                    //
                    //
                }
            }
        }
    }
}
