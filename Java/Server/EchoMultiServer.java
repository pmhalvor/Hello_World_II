import java.net.*;
import java.io.*;

/*
* This code uses thread to allow for multiple clients to connect to a
* single server.
*
* If you leave it open, multiple clients can connect to it, using
* the correct portnr
*
* Also a ping-functio is added, updating the feed once per second
*
* It can be used as a reference for later projects where
* threads could be useful to utilize.
*
*
*
*/

public class EchoMultiServer{
	private ServerSocket serverSocket;
	private static EchoMultiServer server;


	public void start(int port) throws IOException{
		serverSocket = new ServerSocket(port);

		while(true){
			new EchoClientHandler(serverSocket.accept()).start();
		}
	}

	public void stop() throws IOException{
		serverSocket.close();
	}

	private static class EchoClientHandler extends Thread{
		private Socket clientSocket;
		private PrintWriter out;
		private BufferedReader in;

		public EchoClientHandler(Socket socket){
			this.clientSocket = socket;
			System.out.println("new thread created");
		}

		public void run(){
			try{
				out = new PrintWriter(clientSocket.getOutputStream(), true);
				in  = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

				String inputLine;
				while((inputLine = in.readLine()) != null){
					System.out.println(inputLine);
					if(".".equals(inputLine)){
						out.println("Server shutting down.");
						break;
					}
					out.println(inputLine);
					System.out.println(inputLine);
					// Thread.sleep(1000);
				}

				in.close();
				out.close();
				clientSocket.close();
			}
			catch(Exception e){
				System.out.println("some exception was thrown!");
				e.getMessage();
			}
		}
	}


	public static void main(String[] args) throws IOException{
		server = new EchoMultiServer();
		server.start(6666);
	}
}
