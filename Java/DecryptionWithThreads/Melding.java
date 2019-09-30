public class Melding{
    private String meldingen;
    private int kanalID;
    private long sekvensnummeret;
    private static long antallMeldinger;

    public Melding(String melding, Kanal kanal){
        meldingen = melding;
        kanalID = kanal.hentId();
        sekvensnummeret = antallMeldinger++;
    }

    //De tre folgende metoder er bare for aa hente ut informasjon om meldingen:

    public String hentMeldingen(){
        return meldingen;
    }

    public long hentSekvensnummeret(){
        return sekvensnummeret;
    }

    public int hentKanalID(){
        return kanalID;
    }

    //Brukes av Kryptografer for aa endre innholdet i meldingen
    public void endreMelding(String nyMelding){
        meldingen = nyMelding;
    }
}
