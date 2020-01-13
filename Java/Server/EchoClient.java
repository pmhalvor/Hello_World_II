import java.net.*;
import java.io.*;
import java.util.Scanner;


public class EchoClient{
	private Socket clientSocket;
	private PrintWriter out;
	private BufferedReader in;

	public void startConnection(String ip, int port) throws IOException{
		clientSocket = new Socket(ip, port);
		out = new PrintWriter(clientSocket.getOutputStream(), true);
		in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

	}

	public String sendMessage(String msg) throws Exception{
		String resp;
		out.println(msg);
		resp = in.readLine();
		return resp;
	}

	public void stopConnection() throws IOException{
		in.close();
		out.close();
		clientSocket.close();
	}


	// public void setup() throws IOException{
	// 	client = new EchoClient();
	// 	client.startConnection("127.0.0.1", 6666);
	// }
	//
	//
	// public void tearDown() throws IOException{
	// 	client.stopConnection();
	// }



	// @test
	public static void main(String[] args) throws Exception, SocketException{
		// EchoClient client = new EchoClient();
		// client.startConnection("84.212.68.25", 8084);
		// client.startConnection("92.221.113.194", 6666);
		// String response = client.sendMessage("hello server");
		// String resp2 = client.sendMessage(".");
		// System.out.println("These are the results!");
		// System.out.println("mine: hello server");
		// System.out.println("vs");
		// System.out.println(response);
		//
		// EchoClient client2 = new EchoClient();
		// client2.startConnection("84.212.68.25", 8084);
		// // client.startConnection("92.221.113.194", 6666);
		// String response2 = client2.sendMessage("second round of greetings");
		// System.out.println("These are the results!");
		// System.out.println("mine: second rount of greetings");
		// System.out.println("vs");
		// System.out.println(response2);
		EchoClient client = new EchoClient();
		client.startConnection("84.212.68.25", 8084);

		System.out.println("Type what you want to send to server and press enter.");
		String commandInput;
		String serverResp;
		Scanner is;
		while(true){
			is = new Scanner(System.in);
			commandInput =is.nextLine();
			System.out.println("Server: " + client.sendMessage(commandInput));
			if(commandInput.equals("quit")){
				break;
			}
		}
	}
}
