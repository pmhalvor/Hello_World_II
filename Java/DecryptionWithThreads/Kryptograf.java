public class Kryptograf implements Runnable{
    private Monitor kryptertMonitor;
    private Monitor dekryptertMonitor;
    private boolean ferdig = false;
    private int antallKryptografer;
    private int antallFerdige = 0;

    public Kryptograf(Monitor km, Monitor dm, int ak){
        kryptertMonitor = km;
        dekryptertMonitor = dm;
        antallKryptografer = ak;
    }

    @Override
    public void run(){
        try{
            while(!ferdig){
                Melding melding = kryptertMonitor.hentNesteMelding();

                if(melding != null){ //null hvis meldingListen paa monitoren er tom (MERK! dette skjer baade for og etter telegrafene har begynt)
                    String dekryptertTxt = Kryptografi.dekrypter(melding.hentMeldingen());

                    //Brukte denne for aa se at programmet kjorte riktig
                    System.out.println("kan:"+melding.hentKanalID() +"  seq:"+ melding.hentSekvensnummeret());

                    melding.endreMelding(dekryptertTxt);//Bruker metod i Melding for aa endre teksten i Meldingen
                    dekryptertMonitor.leggTil(melding);//Legger nye, dekyrpterte melding til monitoren

                }else if(kryptertMonitor.erFerdig()){//slaar in naar meldingen er null og kryptertMonitor.erFerdig() metoden er sant (dvs telegrafister er ferdige)
                    antallFerdige++;
                    if (antallFerdige == antallKryptografer){
                        ferdig = true;
                    }
                }
            }

            dekryptertMonitor.avsluttKryptografer(); //Dette trenges for aa fortelle op.leder at de maa starte

        }catch(Exception e){ //Fikk ikke bruke Thread uten aa ha med den generell try/catch
            System.out.println(e.getMessage());
        }
        //Fint aa ha for aa se hvor langt programmet her kommet
        // System.out.println("Decryption job finished");
    }
}
