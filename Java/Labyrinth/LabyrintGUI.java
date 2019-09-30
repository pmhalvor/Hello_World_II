import java.io.File;
import java.io.FileNotFoundException;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.*;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ScrollPane;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.Scene;
import javafx.scene.shape.Line;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.stage.DirectoryChooser;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

public class LabyrintGUI extends Application{
    ArrayList<Line> utveiLog = new ArrayList<>();
    BorderPane globalPane = new BorderPane();
    File labFil;
    File valgtDirectory;
    Labyrint innLabyrint;
    Liste<String> listeAvUtveier;
    String filnavn = "";
    Text display = new Text("");
    Text vei = new Text("Velg ny fil og trykk \"View\"");

    /**
    * Setter Scenen i gang.
    * @param args Array av strengene skrevet etter filnavn
    */
    public static void main(String[] args){
        launch(args);
    }


    /**
    * Avslutter programmet.
    */
    public class ExitPlatform implements EventHandler<ActionEvent>{
        @Override
        public void handle(ActionEvent e){
            Platform.exit();
        }
    }


    public class VelgFil implements EventHandler<ActionEvent>{
        Stage teater;

        /**
        * Tillater brukeren aa velge labyrint-filen
        * @param s     Stage-objekt der filen skal lastes opp til
        */
        public VelgFil(Stage s){
            teater = s;
        }

        /**
        * Fjerner evt. tidligere losninger, velger fil og laster den inn
        * @param e ActionEvent-objekt som folger med alle knapper
        */
        @Override
        public void handle(ActionEvent e){
            FjernLinje f = new FjernLinje();
            f.handle(e); //Kvitter oss med tiligere losninger, om det skulle vare noen i globalPane

            try{
                FileChooser fileChooser = new FileChooser(); //Brukeren kan velger en fil til scenen
                fileChooser.setInitialDirectory(valgtDirectory); //Om spesifisert, kan brukeren sette en fast directory
                fileChooser.setTitle("Velg Labyrit fil (kun _.txt eller _.in)"); //Titlen paa vinduet som kommer opp
                labFil = fileChooser.showOpenDialog(teater); //laster valgte filen til scenen

                filnavn = labFil.getName(); //For displayet
                display.setText("Fil: "+filnavn);


                SettOppLabyrint oppsett = new SettOppLabyrint(teater);
                oppsett.handle(e); //Kaller for aa sette opp nylig innlastet labyrint
            }catch(NullPointerException npe){
                System.out.println("Choose file canceled");
            }


        }
    }

    public class SettDirectory implements EventHandler<ActionEvent>{
        Stage teater;

        /**
        *Brukeren kan sette en fast mappe, for lettere handtere av forskjellige labyrint. Ikke nodevendig men hjelpsomt i debugging.
        @param s Stage-objektet mappen skal gjelde for
        *
        */
        public SettDirectory(Stage s){
            teater = s;
        }

        @Override
        public void handle(ActionEvent e){
            DirectoryChooser dirChooser = new DirectoryChooser();
            valgtDirectory = dirChooser.showDialog(teater);
            if (valgtDirectory != null){ //I tilfelle brukeren trykker paa avbryt
                valgtDirectory.getAbsolutePath();
            }
        }
    }


    /**
    *For a konvertere kolonnenummber til pixel-nummer for linje-skriving. Maa vaere public siden jeg bruker den i to forskjellige classer.
    *@param k int-objekt med kolonnenummer
    *@return pixel-nummer til den kolonnen
    */
    public double kolTilPix(int k){
        return 16*k + 8;
    }

    /**
    *For a konvertere radenummber til pixel-nummer for linje-skriving. Maa vaere public siden jeg bruker den i to forskjellige classer.
    *@param k int-objekt med radenummer
    *@return pixel-nummer til den raden
    */
    public double radTilPix(int r){
        return 25*(r+1)+12; //The plus one here is bc of the control panel at the top of BorderPane
    }

    /**
    *For a konvertere stringen med koordinater til an ArrayList<Integer>
    *@param locString String-objekt med koordinater
    *@return ArrayList<Integer> med koordinater
    */
    public ArrayList<Integer> locTilInt(String locString){
        ArrayList<Integer> locArray = new ArrayList<Integer>();

        Pattern p = Pattern.compile("\\d+");
        Matcher m = p.matcher(locString);
        while(m.find()){
            locArray.add(Integer.parseInt(m.group()));
        }
        return locArray;
    }


    public class LagLinje implements EventHandler<ActionEvent>{
        int kol; int x; //x is the pixel location of kolonnen
        int rad; int y; //y is the pixel location of raden

        /**
        *Tegner utvei fra gitte koordinater
        @param X int-objekt med kolonnenummeret
        @param Y int-objekt med radenummeret
        */
        public LagLinje(int X, int Y){
            kol = X; //input value for kol
            rad = Y; //input value for rad
        }

        @Override
        public void handle(ActionEvent e){
            FjernLinje f = new FjernLinje();
            f.handle(e); //Fjerner evt. tidligere losninger

            //Fyller listen med mulige losninger
            listeAvUtveier = innLabyrint.finnUtveiFra(kol, rad);

            //Den kortste utvei vil vises her
            String korteste = innLabyrint.kortesteUtvei();

            //Omgjor strengen til en ArrayList<>
            ArrayList<Integer> koordinater = locTilInt(korteste);

            //Lager linjer mellom alle koordinater
            for(int i=0; i<(koordinater.size()-3); i=i+2){
                Line linje = new Line(kolTilPix(koordinater.get(i)), radTilPix(koordinater.get(i+1)), kolTilPix(koordinater.get(i+2)), radTilPix(koordinater.get(i+3)));
                linje.setStroke(Color.RED); //Kan endres til de fleste andre farger. mer pa https://docs.oracle.com/javase/8/javafx/api/javafx/scene/paint/Color.html
                linje.setStrokeWidth(3);
                globalPane.getChildren().add(linje);
                utveiLog.add(linje);  //Loggfores for lettere sletting eterpa
            }
            //Oppdaterer informasjonen
            vei.setText("Fant " + listeAvUtveier.stoerrelse() +" utveier.");
        }
    }


    public class FjernLinje implements EventHandler<ActionEvent>{

        /**
        *Fjerner alle tegnet linjer fra globaPane
        */
        @Override
        public void handle(ActionEvent e){
            for(Line ele : utveiLog){ //Sletter hver linje element en-for-en
                globalPane.getChildren().remove(ele);
            }

            //Sletter tidligere lagret linjer fra loggen
            utveiLog = new ArrayList<>();
        }
    }

    public class NesteUtevei implements EventHandler<ActionEvent>{


        /**
        *Tegner neste utvei fra utveiListe lagd i LagLinje()
        */
        @Override
        public void handle(ActionEvent e){
            //Rydder i panen
            FjernLinje f = new FjernLinje();
            f.handle(e);

            //String for neste losningen
            String neste = "";
            try{

                //TESTESTESTESTESTESTESTESTESTEST
                System.out.println(listeAvUtveier.hent(0));

                neste = listeAvUtveier.fjern(0);
            }catch(Exception E){
                System.out.println("No more solutions.");
            }

            //Konvertere losningen til array
            ArrayList<Integer> koordinater = locTilInt(neste);

            //Lag en ny linje mellom hver koordinat
            for(int i=0; i<(koordinater.size()-3); i=i+2){
                Line linje = new Line(kolTilPix(koordinater.get(i)), radTilPix(koordinater.get(i+1)), kolTilPix(koordinater.get(i+2)), radTilPix(koordinater.get(i+3)));
                linje.setStroke(Color.RED); //flere farger pa https://docs.oracle.com/javase/8/javafx/api/javafx/scene/paint/Color.html
                linje.setStrokeWidth(3);
                globalPane.getChildren().add(linje);
                utveiLog.add(linje); //Oppdaterer losning-loggen
            }

        }
    }


    public class SettOppLabyrint implements EventHandler<ActionEvent>{
        Stage teater;

        /**
        *Tegner Labyrinten
        @param s Stage-objekt som foteller hvilke teater vi bruker
        */
        public SettOppLabyrint(Stage s){
            teater = s;
        }

        @Override
        public void handle(ActionEvent e){
            if (labFil != null){ //kjøres kun naar vi har en gyldig fil innhentet
                //Omradet vi skal bygge labyrinten
                GridPane gridpane = new GridPane();

                //Min to mulige brikker
                Rectangle svart;
                Button hvit;

                //Hent labyrint fra lab.-fil
                try{
                    innLabyrint = Labyrint.lesFraFil(labFil);
                }catch(FileNotFoundException fnfe){
                    System.out.printf("FEIL: Kunne ikke lese fra '%s'\n", filnavn);
                    System.exit(1);
                }

                //Find rows, columns and ruterArray from methods in Labyrint.java
                int maxX = innLabyrint.hentAntallKolonner();
                int maxY = innLabyrint.hentAntallRader();
                Rute[][] ruterArray = innLabyrint.hentRuteArray();

                //Create visual repersentation of Labyrinth as own gridpane
                for (int i=0; i<maxX; i++){
                    for(int j=0; j<maxY; j++){
                        if(ruterArray[j][i].typ().equals("s")){  //SortRute
                            svart = new Rectangle(16, 25); //Fyll omrade med en svart rektangle
                            svart.setFill(Color.BLACK);
                            gridpane.add(svart, i, j);
                        }else{ //HvitRute
                            hvit = new Button(); //fyll omrade med et knapp som kan finne en utvei
                            hvit.setOnAction(new LagLinje(i, j));
                            gridpane.add(hvit, i, j);
                            gridpane.setFillWidth(hvit, true); //fyll knappen til omradet
                            gridpane.setFillHeight(hvit, true);
                        }
                    }
                }

                //Endre instruksjoner
                vei.setText("Trykk en hvit knapp");
                //Setting newly created gridpane to the center of global pane
                globalPane.setCenter(gridpane);
                //resizes the scene to fix all new elements
                teater.sizeToScene();
            }
        }
    }


    /**
    *Starter programet
    @param teater Stage-objekt som skal presenteres
    */
    @Override
    public void start(Stage teater){
        //This contorl panel will remain at the top of my Scene
        GridPane controlPanel = new GridPane();

        Button settDir = new Button("Set directory");
        settDir.setOnAction(new SettDirectory(teater));
        controlPanel.add(settDir, 0,0);

        Button loadNew = new Button("New");
        loadNew.setOnAction(new VelgFil(teater));
        controlPanel.add(loadNew, 1,0);

        Button viewLab = new Button("View");
        viewLab.setOnAction(new SettOppLabyrint(teater));
        controlPanel.add(viewLab, 2, 0);

        Button fjernLinje = new Button("Clear");
        fjernLinje.setOnAction(new FjernLinje());
        controlPanel.add(fjernLinje, 3, 0);

        Button neste = new Button("Next");
        neste.setOnAction(new NesteUtevei());
        controlPanel.add(neste, 4, 0);

        Button avslutt = new Button("End");
        avslutt.setOnAction(new ExitPlatform());
        controlPanel.add(avslutt, 5, 0);

        //Legge til contorl panel paa toppen av BorderPane
        globalPane.setTop(controlPanel);

        //This part will give info on filename and path found
        GridPane infoBar = new GridPane();

        infoBar.add(vei, 0,1);
        infoBar.add(display, 0,0);

        //Legge til infoBar helt nederst
        globalPane.setBottom(infoBar);

        //For lettere handtering av store labyrinter
        ScrollPane scroller = new ScrollPane(globalPane);

        //Skaper scroll-bar scene
        Scene scene = new Scene(scroller);

        //Viser frem forestillingen
        teater.setTitle("Labyrint forestilling");
        teater.setScene(scene);
        teater.show();
    }
}
