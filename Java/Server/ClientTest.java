import java.net.*;
import java.io.*;


public class ClientTest{
	private Socket clientSocket;
	private PrintWriter out;
	private BufferedReader in;

	public void startConnection(String ip, int port){
		try{
			clientSocket = new Socket(ip, port);
			out = new PrintWriter(clientSocket.getOutputStream(), true);
			in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
		}
		catch(Exception e){
			e.getMessage();
		}
	}

	public String sendMessage(String msg){
		String resp = null;
		try{
			out.println(msg);
			resp = in.readLine();
		}
		catch(Exception e){
			e.getMessage();
		}
		return resp;
	}

	public void stopConnection(){
		try{
			in.close();
			out.close();
			clientSocket.close();
		}
		catch(Exception e){
			e.getMessage();
		}



	// @test
	public static void main(String[] args) {
		ClientTest client = new ClientTest();
		client.startConnection("127.0.0.1", 6666);
		// client.startConnection("92.221.113.194", 6666);
		String response = client.sendMessage("hello server");
		System.out.println("These are the results!");
		System.out.println("mine: hello server");
		System.out.println("vs");
		System.out.println(response);
	}
}
