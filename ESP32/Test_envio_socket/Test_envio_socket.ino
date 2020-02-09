#include <WiFi.h>

const char* ssid = "VSSS_CURIOSOS";
const char* password =  "AaAjJj69420";
 
const uint16_t port = 4000;
const char * host = "192.168.0.101";
int pot;
int estado = 0;

WiFiServer server (80);
 
void setup()
{
 
  Serial.begin(115200);
  pinMode(36, INPUT);
  pinMode(5, OUTPUT);
  digitalWrite(5, LOW);
 
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());

  
  
  server.begin();
}
 
void loop()
{
    pot = analogRead(36);
    WiFiClient client;
    WiFiClient client2 = server.available();
    
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
 
        delay(1000);
        return;
    }
 
    //Serial.println("Connected to server successful!");
    Serial.println(pot);
 
    client.print("|");
    client.print(pot);
    client.print(".");
    client.stop();
 
    delay(10);

    if (client2) {
 
    while (client2.connected()) {
        if (client2.available()>0) {
          char c = client2.read();
          Serial.write(c);
          
          if((c == 'b') && (estado == 0)){
            digitalWrite(5, HIGH);
            estado = 1;
          }
          else if((c == 'b') && (estado == 1)){
            digitalWrite(5, LOW);
            estado = 0;
          }

          Serial.print("available bits");
        }else{
          break;
          
         }

        Serial.println("client2 connected");
        
        delay(100);
    }

    Serial.print("end of program");
 
    client2.stop();
 
  }
}

    
