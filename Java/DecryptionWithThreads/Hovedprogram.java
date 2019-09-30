public class Hovedprogram{
    public static void main(String[] args) {
        int antallTelegrafister = 3;
        int antallKryptografer = 6;

        //Setter opp arbeidsplassen til alle 
        Operasjonssentral ops = new Operasjonssentral(antallTelegrafister);
        Kanal[] kanaler = ops.hentKanalArray();

        //Sett opp monitorene
        Monitor kryptertMonitor = new Monitor(ops.hentAntallKanaler());
        Monitor dekryptertMonitor = new Monitor(ops.hentAntallKanaler(), antallKryptografer);

        //Sett opp telegrasfister og sett dem i arbeid
        for (int i = 0; i<antallTelegrafister; i++){
            Runnable telegrafistJobb = new Telegrafist(kryptertMonitor, kanaler[i], antallTelegrafister); //maa defineres inni for loopen siden det telegrafene har en kanal hver
            Thread telegrafist = new Thread(telegrafistJobb);
            telegrafist.start();
        }

        //Sett opp kryptografene og sett dem i arbeid
        Runnable dekrypterJobb = new Kryptograf(kryptertMonitor, dekryptertMonitor, antallKryptografer);
        for (int i = 0; i<antallKryptografer; i++){
            Thread kryptograf = new Thread(dekrypterJobb);
            kryptograf.start();
        }

        //Sett opp Op.Leder og sett dem i arbeid
        Runnable oplederJobb = new Operasjonsleder(dekryptertMonitor, args[0]);
        Thread opleder = new Thread(oplederJobb);
        opleder.start();

    }
}
