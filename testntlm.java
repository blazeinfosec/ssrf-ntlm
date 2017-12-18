// based on https://stackoverflow.com/questions/10750723/suppress-ntlm-auth-in-java
// to prove NTLM is indeed sent by default in Java's HttpURLConnection

import java.net.*;
import java.io.*;

public class testntlm {

 public static void main(String[] args) {
    try {
        //TrustAllCerts.disableCertChecks();
        FileReader fr = new FileReader(new File("urls.txt"));
        BufferedReader br = new BufferedReader(fr);

        String urlStr = br.readLine();
        while (urlStr != null) {
            if (urlStr.trim().length() > 0) {
                URL url = new URL(urlStr);

                HttpURLConnection urlc = (HttpURLConnection) url.openConnection();
                urlc.connect();
                if (urlc.getResponseCode() == HttpURLConnection.HTTP_OK) {
                    System.out.println(urlStr);

                } else {
                    System.out.println("["+urlc.getResponseCode()+"] "+urlStr);
                }
                urlc.disconnect();
            }
            urlStr = br.readLine();
        }
        br.close();

    } catch (Exception e) {
        e.printStackTrace();
    }
 }

}
