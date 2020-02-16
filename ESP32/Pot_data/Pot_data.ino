#include <WiFi.h>
#include <analogWrite.h>
 
const char* ssid = "VSSS_CURIOSOS";
const char* password =  "AaAjJj69420";
 
const uint16_t port = 4000;
const char * host = "192.168.0.100";

int pot;
int val;
 
void setup()
{
  pinMode(13, OUTPUT);
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.print("MAC ADDRESS: ");
  Serial.println(WiFi.macAddress());
 
}
 
void loop()
{
    pot = analogRead(36);
    Serial.println(pot);
    val = map(pot, 0, 4095, 0, 255);
    analogWrite(13, val);
    
    WiFiClient client;
 
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
        delay(3000);
        return;
    }
 
    Serial.println("Connected to server successful!");
    client.print('|');
    client.print(pot);
    client.print('.');
    client.stop();
    
 
    //Serial.println("Disconnecting...");
    
 
    delay(10);
}
