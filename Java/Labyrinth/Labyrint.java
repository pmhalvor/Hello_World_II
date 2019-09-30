import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Labyrint{
    Rute[][] ruterArray;
    int antallRader;
    int antallKolonner;
    Liste<String> funnetUtveier;

    private Labyrint(Rute[][] rA, int rader, int kolonner){
        ruterArray = rA;
        antallRader = rader;
        antallKolonner = kolonner;
    }

    public static Labyrint lesFraFil(File fil) throws FileNotFoundException{
        // Static FActory metoden som lager Labyrinten min

        // Leser forste linje i filen
        Scanner scanner = new Scanner(fil);
        String innlest = scanner.nextLine();

        // Finner ut stoerrelse pa arrayen
        String [] radOgKol = innlest.split(" ");
        int rader = Integer.parseInt(radOgKol[0]);
        int kolonner = Integer.parseInt(radOgKol[1]);

        // Lager imidlertidige array som static factory skal sette inni konstrukoren til Labyrint
        Rute[][] tempArray = new Rute[rader][kolonner];

        // Leser linjene og oppretter Rute-objekter med hensyn til elementene funnet
        Character current;
        int rad = 0;
        while(scanner.hasNextLine()){
            innlest = scanner.nextLine();
            for(int k =0; k < kolonner; k++){
                current = new Character(innlest.charAt(k));
                if (current.equals('.')){
                    if (erAapning(rad, k, rader, kolonner)){ // Bruker metoden nedenfor å bestemme om ruten er apning
                        tempArray[rad][k] = new Aapning(rad, k);
                    }else{
                        tempArray[rad][k] = new HvitRute(rad, k);
                    }
                }else if (current.equals('#')){
                    tempArray[rad][k] = new SortRute(rad, k);
                }  // Her er det viktig a papeke at jeg antar at fil-formaten er helt riktig!
            }
            rad++;
        }

        // Na star alle rutene uten nabo. Fikses med folgende for-loop
        for (int r =0; r<rader; r++){
            for(int k =0; k<kolonner; k++){
                // Over
                if(r>0){
                    tempArray[r][k].naboene[0] = tempArray[r-1][k];
                }

                // Hoyre
                if(k<(kolonner-1)){
                    tempArray[r][k].naboene[1] = tempArray[r][k+1];
                }

                // Under
                if(r<(rader-1)){
                    tempArray[r][k].naboene[2] = tempArray[r+1][k];
                }

                // Venstre
                if(k>0){
                    tempArray[r][k].naboene[3] = tempArray[r][k-1];
                }
            }
        }

        // lager nye Labyrint-objektet som skal returneres
        return new Labyrint(tempArray, rader, kolonner);
    }

    private static boolean erAapning(int r, int k, int antallRader, int antallKolonner){
        if (r==0 || k==0){
            return true;
        }else if (r==(antallRader-1) || k==(antallKolonner-1)){
            return true;
        }
        return false;
    }

    public Liste<String> finnUtveiFra(int kol, int rad){
        // Oppretter listen som skal lagres alle utveiene
        Lenkeliste<String> listeAvUtveier = new Lenkeliste<>();

        // Finner frem til riktige start posisjonen
        Rute startRute = ruterArray[rad][kol];

        // Alle utveiene blir returnert som en streng seperert av en ";"
        String toSplit = startRute.gaa("");
        String[] utveier = toSplit.split(";");
        for (String u : utveier){ //
            listeAvUtveier.leggTil(u);
        }

        reset();
        funnetUtveier = listeAvUtveier;
        return listeAvUtveier;
    }

    public void reset(){
        for (Rute[] r : ruterArray){
            for (Rute k : r){
                k.vertHer = false;
            }
        }
    }


    /**
    *Skrives til string
    *@return strengen av infoet
    */
    @Override
    public String toString(){
        String toReturn = "";
        for (Rute[] r: ruterArray){
            for (Rute k : r){
                toReturn += k.charToTegn();
            }
            toReturn += "\n";
        }
        return toReturn;
    }

    public String kortesteUtvei(){
        String korteste = funnetUtveier.hent(0);
        for(int i=1; i<funnetUtveier.stoerrelse(); i++){
            if(funnetUtveier.hent(i).length() < korteste.length()){
                korteste = funnetUtveier.hent(i);
            }
        }
        int ledd = (korteste.length() + 5)/10;
        System.out.println("Korteste utvei har "+ledd+" ledd:\n" + korteste +"\n");
        return korteste;
    }

    /**
    *Gir private verdier
    * @return antallRader
    */
    public int hentAntallRader(){
        return antallRader;
    }

    /**
    *Gir private verdier
    *@return antallKolonner
    */
    public int hentAntallKolonner(){
        return antallKolonner;
    }

    /**
    *Gir private verdier
    *@return ruterArray
    */
    public Rute[][] hentRuteArray(){
        return ruterArray;
    }

}
