#include <WiFi.h>
#include <analogWrite.h>
#include "Arduino.h"

TaskHandle_t Task1;
TaskHandle_t Task2;

const char* ssid = "VSSS_CURIOSOS";
const char* password =  "AaAjJj69420";
 
const uint16_t port = 4000;
const char * host = "192.168.0.100";

const int led = 13;
const int pot = 36;
int val;

String bufferMessage = "",
       lastMessage = "";

char delimitator = '.';

void setup() {
  Serial.begin(115200); 
  pinMode(led, OUTPUT);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.print("MAC ADDRESS: ");
  Serial.println(WiFi.macAddress());

  //create a task that will be executed in the Task1code() function, with priority 1 and executed on core 0
  xTaskCreatePinnedToCore(
                    Task1code,   /* Task function. */
                    "Task1",     /* name of task. */
                    10000,       /* Stack size of task */
                    NULL,        /* parameter of the task */
                    1,           /* priority of the task */
                    &Task1,      /* Task handle to keep track of created task */
                    0);          /* pin task to core 0 */                  
  delay(500); 

  //create a task that will be executed in the Task2code() function, with priority 1 and executed on core 1
  xTaskCreatePinnedToCore(
                    Task2code,   /* Task function. */
                    "Task2",     /* name of task. */
                    10000,       /* Stack size of task */
                    NULL,        /* parameter of the task */
                    1,           /* priority of the task */
                    &Task2,      /* Task handle to keep track of created task */
                    1);          /* pin task to core 1 */
    delay(500); 

}

void Task1code( void * pvParameters ){
  Serial.print("Task1 running on core ");
  Serial.println(xPortGetCoreID());

  for(;;){
    val = analogRead(pot);

    WiFiClient client;
 
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed");
        delay(3000);
        return;
    }
 
    Serial.println("Connected to server successful!");
    client.print('|');
    client.print((String) val);
    client.print('.');
    client.stop();

    delay(40);
  } 
}

void Task2code( void * pvParameters ){
  Serial.print("Task2 running on core ");
  Serial.println(xPortGetCoreID());

  WiFiServer wifiServer(4100);
   wifiServer.begin();

  for(;;){

   //WiFiServer wifiServer(4100);
   //wifiServer.begin();

   WiFiClient client = wifiServer.available();
 
  if (client) {
 
    while (client.connected()) {
      
        while (client.available()>0) {

         String line = client.readStringUntil('\n');
         //Serial.print(line);
         int caca = line.toInt();
         analogWrite(led, caca);
        } 
    }
    delay(40);
  }
  client.stop();
  }
}

void loop() {
  
}
