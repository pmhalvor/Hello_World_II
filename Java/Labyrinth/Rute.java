abstract class Rute{
    int rade;
    int kolonne;

    // Nabo-objektene for denne ruten lagret i en Ruter array
    Rute[] naboene = new Rute[4]; //Med klokke, altså over:0, hoyre:1, under:2, venstre:3

    // Forteller om denne ruten er brukt eller ikke
    boolean vertHer = false;

    // Om vi vil ha detaljert utskrift, ville denne instansen bli endret i Labyrint
    public static boolean detaljert = false;

    public Rute(int r, int k){
        rade = r;
        kolonne = k;
    }

    abstract public String charToTegn();

    abstract public String typ();

    abstract public boolean erAapning();

    public void finnUtvei(){
        System.out.println(gaa(""));
    }

    public String gaa(String vH){
        // Srteng med tidligere koordinater
        String veienHit = vH;

        // boolean som forteller om denne ruten har hatt besok enna
        vertHer = true;

        // Forteller systemeet hvilke rute vi ser pa na, og danne retur strengen
        if (detaljert){
            System.out.println("Current coordinates: col="+kolonne+" rad="+rade);
        }
        String koordinater = "(" + kolonne + "," + rade + ")";
        if (veienHit.length() != 0){
            veienHit+= " --> ";
        }
        veienHit += koordinater;

        //vil ha en tom streng som kun oppdateres hvis apning finnes, ellers vil den returnen denne null strengen tar dette opp igjen om en kort pause
        String toReturn = "";

        // Sjekker om vi har funnet veien ut enna
        if (erAapning()){
            if (detaljert){
                System.out.println("found opening");
            }
            return veienHit + ";";
        }

        // Prover seg pa alle naboene
        for (Rute nabo : naboene){
            if(!nabo.vertHer){
                if (nabo.typ().equals("h")){
                    String returned = nabo.gaa(veienHit);
                    if(returned!=null){
                        toReturn += returned;
                        nabo.vertHer = false;
                    }
                }
            }
        }
        // Ferdig med for-loop og dermed her sjekket alle mulighetene for denne ruten
        // Gar et skritt tilbake for a sjekke resterende naboene derfra
        return toReturn;
    }


}
