//This example code is in the Public Domain (or CC0 licensed, at your option.)
//By Evandro Copercini - 2018
//
//This example creates a bridge between Serial and Classical Bluetooth (SPP)
//and also demonstrate that SerialBT have the same functionalities of a normal Serial

#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#include <analogWrite.h>

const int IN1_IZQ = 27;
const int IN2_IZQ = 14;
const int IN1_DER = 26;
const int IN2_DER = 25;
const int EN_IZQ = 12;
const int EN_DER = 13;

void Adelante();
void Giro_izq();
void Giro_der();
void Atras();
void Stop();
void Adelante_izq();
void Adelante_der();
void Atras_izq();
void Atras_der();

BluetoothSerial SerialBT;
char orden;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
  pinMode(IN1_IZQ, OUTPUT);
  pinMode(IN2_IZQ, OUTPUT);
  pinMode(IN1_DER, OUTPUT);
  pinMode(IN2_DER, OUTPUT);
  pinMode(EN_IZQ, OUTPUT);
  pinMode(EN_DER, OUTPUT);
}

void loop() {
  if (SerialBT.available()) {
    orden = SerialBT.read();
    Serial.println(orden);
    if (orden == 'F')
      Adelante(); 
    else if (orden == 'B')
      Atras();
    else if (orden == 'L')
      Giro_izq();  
    else if (orden == 'R')
      Giro_der();
    else if (orden == 'G')
      Adelante_izq();
    else if (orden == 'I')
      Adelante_der();
    else if (orden == 'H')
      Atras_izq();
    else if (orden == 'J')
      Atras_der();
    else if (orden == 'S')
      Stop();
  //delay(20);
}
}

void Atras(){
  digitalWrite(IN1_IZQ, HIGH);
  digitalWrite(IN2_IZQ, LOW);
  analogWrite(EN_IZQ, 120);

  digitalWrite(IN1_DER, HIGH);
  digitalWrite(IN2_DER, LOW);
  analogWrite(EN_DER, 120);
}

void Stop(){
  digitalWrite(IN1_IZQ, LOW);
  digitalWrite(IN2_IZQ, LOW);
  analogWrite(EN_IZQ, 0);

  digitalWrite(IN1_DER, LOW);
  digitalWrite(IN2_DER, LOW);
  analogWrite(EN_DER, 0);
}

void Giro_der(){
  digitalWrite(IN1_IZQ, HIGH);
  digitalWrite(IN2_IZQ, LOW);
  analogWrite(EN_IZQ, 200);

  digitalWrite(IN1_DER, LOW);
  digitalWrite(IN2_DER, LOW);
  analogWrite(EN_DER, 0);
}

void Giro_izq(){
  digitalWrite(IN1_IZQ, LOW);
  digitalWrite(IN2_IZQ, LOW);
  analogWrite(EN_IZQ, 0);

  digitalWrite(IN1_DER, HIGH);
  digitalWrite(IN2_DER, LOW);
  analogWrite(EN_DER, 200);
}

void Adelante(){
  digitalWrite(IN1_IZQ, LOW);
  digitalWrite(IN2_IZQ, HIGH);
  analogWrite(EN_IZQ, 120);

  digitalWrite(IN1_DER, LOW);
  digitalWrite(IN2_DER, HIGH);
  analogWrite(EN_DER, 120);
}

void Atras_der(){
  digitalWrite(IN1_IZQ, HIGH);
  digitalWrite(IN2_IZQ, LOW);
  analogWrite(EN_IZQ, 120);

  digitalWrite(IN1_DER, HIGH);
  digitalWrite(IN2_DER, LOW);
  analogWrite(EN_DER, 75);
}

void Atras_izq(){
  digitalWrite(IN1_IZQ, HIGH);
  digitalWrite(IN2_IZQ, LOW);
  analogWrite(EN_IZQ, 75);

  digitalWrite(IN1_DER, HIGH);
  digitalWrite(IN2_DER, LOW);
  analogWrite(EN_DER, 120);
}

void Adelante_izq(){
  digitalWrite(IN1_IZQ, LOW);
  digitalWrite(IN2_IZQ, HIGH);
  analogWrite(EN_IZQ, 75);

  digitalWrite(IN1_DER, LOW);
  digitalWrite(IN2_DER, HIGH);
  analogWrite(EN_DER, 120);
}

void Adelante_der(){
  digitalWrite(IN1_IZQ, LOW);
  digitalWrite(IN2_IZQ, HIGH);
  analogWrite(EN_IZQ, 120);

  digitalWrite(IN1_DER, LOW);
  digitalWrite(IN2_DER, HIGH);
  analogWrite(EN_DER, 75);
}
