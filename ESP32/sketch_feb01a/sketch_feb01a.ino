#include <WiFi.h>
#include "Arduino.h"

const char* ssid = "VSSS_CURIOSOS";  // Enter SSID here
const char* password = "AaAjJj69420";  //Enter Password here

String bufferMessage = "",
       lastMessage = "";

char delimitator = '.';

const int led = 5;
 
WiFiServer wifiServer(80);
 
void setup() {
 
  Serial.begin(115200);
  pinMode(led, OUTPUT);
 
  delay(1000);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting..");
  }
 
  Serial.print("Connected to WiFi. IP:");
  Serial.println(WiFi.localIP());
 
  wifiServer.begin();
}
 
void loop() {
  WiFiClient client = wifiServer.available();
 
  if (client) {
 
    while (client.connected()) {
      
        while (client.available()>0) {

         String line = client.readStringUntil('\n');
         Serial.print(line);
      /*
          if (line=="1") {
            digitalWrite(led, HIGH);
            Serial.println("rivera es una puta");
          }
          else if (line=="1") {
            digitalWrite(led, LOW);
            Serial.println("agus es una puta");
          }

          */


          int caca = line.toInt();
          analogWrite(led, caca);

          }

          
        }
  
 
      delay(10);
    }
 
    client.stop();
}
