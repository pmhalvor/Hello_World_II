public class Specialist extends Doctor implements ApprovalExemption{
    int conID;
    public Specialist(String name, int controlID){
        /*
        Calls constructor in Doctor, as well as assigns the correct controlID for the Specialist
        */
        super(name);
        super.controlID = controlID;
        conID = controlID;
    }

    @Override
    public int getControlID(){
        return controlID;
    }

    @Override
    public String toString(){//Prints all the infor we have on spcialist
        return "Specialist "+super.getName()+ " contorlID: "+ conID + "\n";
    }
}
