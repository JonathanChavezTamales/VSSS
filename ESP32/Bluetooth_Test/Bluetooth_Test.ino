//This example code is in the Public Domain (or CC0 licensed, at your option.)
//By Evandro Copercini - 2018
//
//This example creates a bridge between Serial and Classical Bluetooth (SPP)
//and also demonstrate that SerialBT have the same functionalities of a normal Serial

#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;
int estado = 0;
char orden;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
  pinMode(5, OUTPUT);
}

void loop() {
  if (SerialBT.available()) {
    orden = SerialBT.read();
    Serial.write(orden);
    if ((orden == 'A') && (estado == 0)){
      digitalWrite(5, HIGH);
      estado = 1;
    }
    else if ((orden == 'A') && (estado == 1)){
      digitalWrite(5, LOW);
      estado = 0;
    }
  }
  delay(20);
}
