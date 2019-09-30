public class Telegrafist implements Runnable{
    private Monitor monitor;
    private Kanal kanal;
    private boolean ferdig = false;
    private int antallTelegrafister;
    private int antallFerdige = 0;

    public Telegrafist(Monitor m, Kanal k, int at){
        monitor = m;
        kanal = k;
        antallTelegrafister = at;
    }

    @Override
    public void run(){
        try{
            while(!ferdig){
                String kryptertTekst = kanal.lytt(); //bruker metoden fra prekoden til aa lytte til nye meldinger

                if(kryptertTekst != null){
                    Melding kryptertMelding = new Melding(kryptertTekst, kanal);
                    monitor.leggTil(kryptertMelding);
                }else{
                    // DETTE ER LITT RART MEN FUNKER SOM DEN SKAL
                    antallFerdige++; //okes hver gang noen har naade enden av meldignen deres
                    if(antallFerdige==antallTelegrafister){
                        ferdig = true; //naar elsene har blitt naade like mange ganger som antall kanal, vil denne sla inn, og loopen vil abryte seg selv
                    }
                    //FREM TIL DENNE LINJE

                }
            }
            monitor.avsluttTelegrafister();
            // For aa kontroller at programmet kjorer riktig
            // System.out.println("Telegraph job finished");
        }catch(Exception e){} //maa altidd ha try/catch men vet ikke hvorfor nar vi vet at det ikke blir interrupted. PROBLEM: med catch(InterruptedException e) faar jeg feilmeldingen: exception InterruptedException is never thrown in body of correspnding try statement. Se paa ved slutten av oppgaven
    }
}
