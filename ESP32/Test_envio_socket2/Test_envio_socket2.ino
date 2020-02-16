#include <WiFi.h>
#include <analogWrite.h>

const char* ssid = "VSSS_CURIOSOS";
const char* password =  "AaAjJj69420";
 
const uint16_t port = 4000;
const char * host = "192.168.0.101";
int pot;
 
void setup()
{
 
  Serial.begin(115200);
  pinMode(36, INPUT);
 
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  //Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());

}
 
void loop()
{
    pot = analogRead(36);
    WiFiClient client;
    
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
 
        delay(1000);
        return;
    }
 
    //Serial.println("Connected to server successful!");
    Serial.println(pot);
    analogWrite(5, 255);
 
    client.print("|");
    client.print(pot);
    client.print(".");
    client.stop();
 
    delay(10);
}
