import java.util.ArrayList;
import java.util.LinkedList;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Condition;

public class Monitor{
    private LinkedList<Melding> meldingList = new LinkedList<>();
    private Lock laas = new ReentrantLock();
    private Condition ikkeTom = laas.newCondition();
    private boolean ferdig = false;
    private int antallFerdige = 0;
    private int antallKanaler;
    private boolean startOpLeder = false;
    private int antallKryptografer;


    public Monitor(int antallKanaler){ //kryptertMonitor vil bruke denne
        this.antallKanaler = antallKanaler;
    }

    public Monitor(int antallKanaler, int antallKryptografer){ //dekryptertMonitor vil bruke denne
        this.antallKanaler = antallKanaler;
        this.antallKryptografer = antallKryptografer;
    }

    public void leggTil(Melding m){
        //Tar imot nye meldinger og legger dem i koen
        laas.lock(); //Selv om oppgaven utfores veldig fort, regnet jeg med at vi trengte fortsatt en laas
        meldingList.add(m); //legger til ved slutten av meldingListen
        laas.unlock();
    }

    public Melding hentNesteMelding(){
        //Skal ha oppgaven om aa returnere den overste melding og fjerne den fra listen
        laas.lock();
        Melding temp =  meldingList.poll(); //Returnerer/fjerner det forste elementet i meldingListen
        laas.unlock();
        return temp; //trivalt aa ha med, men kompilator trenger en fall-back return verdi
    }

    public void avsluttTelegrafister(){
        //KUN BRUKES AV TELEGRAFISTER
        antallFerdige++;
        if (antallFerdige == antallKanaler){
            ferdig = true;
        }
    }

    public void avsluttKryptografer(){
        //KUN BRUKES AV KRYPTOGRAFER
        antallFerdige++;
        if (antallFerdige == antallKryptografer){
            //Signaliser Operasjonsleder at den kan begynne aa skrive ut hele dekryptert meldingen
            startOpLeder = true;
        }
    }


    public boolean startOperasjonLeder(){
        //Signalet OpLeder venter for for aa begynne aa jobbe
        return startOpLeder;
    }

    public boolean erFerdig(){
        //Om alle meldingene har blitt tatt med
        return ferdig;
    }

    public boolean erTom(){
        //Om monitor er tom eller ikke
        if(meldingList.size()==0){
            // System.out.println("Monitor er tom"); //Viser meg naar denne metoden har blitt kalt
            return true;
        }
        return false;
    }

    public int hentAntallKanaler(){
        //I tilfelle det trenges
        return antallKanaler;
    }
}
