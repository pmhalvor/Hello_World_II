public class IllegalPrint extends Exception {
    /*
    I just changed everything to english, since its good coding nomenclature to write in english
    */
  IllegalPrint(Doctor d, Medicine med){
    super("Doctor "+d.getName()+ " cannot write a prescription for "+ med.getName());
  }
}
