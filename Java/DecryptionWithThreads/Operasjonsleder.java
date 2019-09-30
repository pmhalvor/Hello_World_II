import java.util.LinkedList;
import java.util.ArrayList;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.UnsupportedEncodingException;
import java.io.PrintWriter;


public class Operasjonsleder implements Runnable{
    //les in meldingene fra monitoren
    //sorter meldingene til forskjellige arrays
    //skriv ut arrays til en fil
    private Monitor dekryptertMonitor;
    private boolean ferdig = false;
    private int antallKanaler;
    private ArrayList<ArrayList<Melding>> meldingene = new ArrayList<ArrayList<Melding>>();;
    private String utfil;

    public Operasjonsleder(Monitor dm, String utfil){
        dekryptertMonitor = dm;
        antallKanaler = dm.hentAntallKanaler();
        this.utfil = utfil;
        for (int i = 0 ; i < antallKanaler; i++){
            //lager de tre forskjellige kanaler i meldingslisten
            ArrayList<Melding> kanal = new ArrayList<>();
            meldingene.add(kanal);
        }
        // System.out.println("Antall kanal: "+ meldingene.size()); //kontrollerer at vi fikk riktige antall kanaler
    }


    @Override
    public void run(){
        try{
            while(!ferdig){ //Er ikke ferdig for dekrypterte monitoren er tom
                Thread.sleep(5); //Mulig at jeg ikke trenger denne lenger, men programmet hang seg opp uten. kommer tilbake helt til sist
                if (dekryptertMonitor.startOperasjonLeder() && !dekryptertMonitor.erTom()){
                        //Kommer inni her kun etter vi har faatt start signal og fortsetter frem til monitoren er tom

                        //Henter melding og dens ID nummer for aa bruke i for loopen
                        Melding denneMeldingen = dekryptertMonitor.hentNesteMelding();
                        int denneKanalID = denneMeldingen.hentKanalID();
                        ArrayList<Melding> kanal = meldingene.get(denneKanalID-1);

                        //Nyttig for aa kontroller at programmet kjører
                        // System.out.println("adding message: k:"+ denneMeldingen.hentKanalID()+" s:"+denneMeldingen.hentSekvensnummeret());

                        if(kanal.size() == 0){
                            //Dette er for aa begynne oppfyllingen av listene
                            kanal.add(denneMeldingen);
                            continue;
                        }
                        for (int i = 0; i < kanal.size(); i++){ //De fleste er i riktige rekkefolge, men vi trenger begge de folgende betingelser for at alt blir sortert riktig
                            if(denneMeldingen.hentSekvensnummeret() < kanal.get(i).hentSekvensnummeret()){
                                kanal.add(i, denneMeldingen);
                                break;
                            }else if(i == kanal.size()-1){
                                kanal.add(denneMeldingen);
                                break;
                            }
                        }

                }else if(dekryptertMonitor.startOperasjonLeder() && dekryptertMonitor.erTom()){
                    //Etter baade start signal er gitt, og monitoren er tom
                    ferdig = true;
                }

            }
        }catch(InterruptedException e){
            System.out.println(e.getMessage());
        }

        //Dette brukte jeg kun for aa kontroller at alt annet funker, for utskrivning til fil
        /*for (int i = 0; i < antallKanaler; i++){
            ArrayList<Melding> mL = meldingene.get(i);
            for (int j = 0; j < mL.size(); j++){
                System.out.println(mL.get(j).hentMeldingen());
            }
            System.out.println("\n\n");
        }*/

        //Bruker metoden som finnens under for aa skrive til fil
        skrivTilFil(meldingene);
    }


    public void skrivTilFil(ArrayList<ArrayList<Melding>> meldingList){
        File f = new File(utfil);
        try{
            PrintWriter pw = new PrintWriter(f);

            for(ArrayList<Melding> kanal : meldingList){
                for(Melding m : kanal){
                    pw.append(m.hentMeldingen()+"\n");
                }
                pw.append("\n\n");
            }

            pw.close(); //Viktig aa stenge printed fil

        }catch(FileNotFoundException e){ //Begge exceptions trengers her for at komtilator skal vare fornoyd
            System.out.println(e.getMessage());
        }
    }
}
