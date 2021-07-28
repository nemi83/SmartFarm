#include "DHT.h"
#define DHTPIN 7
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);
int sensor_pin = A0;
int hs;

void setup() {
  Serial.begin(9600);
  dht.begin(); //start the temp reading
}

void loop() {
  //read the temperature and humidity
  delay(2000);
  float h = dht.readHumidity(); //read humidity
  float t = dht.readTemperature(); //read temperature (C)
  hs = analogRead(sensor_pin);
  hs = map(hs,550,0,0,100);
  // check if returns are valid
  if (isnan(t) || isnan(h) || isnan(hs)) {
    Serial.println("Failed to read from DHT or HS");
  } else {  //if it read correctly
    Serial.print(h);     //humidity
    Serial.print(" \t"); //tab
    Serial.print(t);   //temperature (C)
    Serial.print(" \t"); //tab
    Serial.println(hs);
    }
}


