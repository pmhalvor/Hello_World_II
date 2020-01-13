import java.net.*;
import java.io.*;


public class EchoServer{
	private Socket clientSocket;
	private ServerSocket serverSocket;
	private PrintWriter out;
	private BufferedReader in;
	private EchoClient client;
	private long startTime = System.nanoTime();

	public void start(int port) throws IOException, ClassNotFoundException{
		serverSocket = new ServerSocket(port);
		clientSocket = serverSocket.accept();


		out = new PrintWriter(clientSocket.getOutputStream(), true);
		in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

		String inputLine;
		int counter = 0;
		while((inputLine = in.readLine()) != null){
			System.out.println("Round " + counter);
			if(".".equals(inputLine)){ // communtication between cleint and server ends when '.' is recieved
				System.out.println("good bye");
				break;
			}
			if(inputLine.equals("quit")){
				break;
			}
			out.print(inputLine);
			out.println(" [server runtime: "+ (System.nanoTime()-startTime)/1000000.0 + " milliseconds]");
			System.out.println(inputLine);
			counter++;
		}

		stop();  // Close the socket when the while loopis broken to avoid Exception messages
	}

	public void stop() throws IOException{
		clientSocket.close();
	}


// Why do you have both throws ex. and a try/catch?
	public static void main(String[] args) throws ClassNotFoundException, IOException, SocketException{
		EchoServer server = new EchoServer();
		server.start(6666);
	}
}
