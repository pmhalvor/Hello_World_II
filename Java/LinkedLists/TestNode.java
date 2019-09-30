public class TestNode<T>{
    TestNode neste = null; //Same as above
    T ting; //The actual object in our Lenkeliste
    int index; //The index of this specific node, to be determined upon insert

    TestNode(T ting){
        this.ting = ting;
    }
}
