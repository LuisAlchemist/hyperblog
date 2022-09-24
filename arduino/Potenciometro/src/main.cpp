#include <Arduino.h>
#include <DHT.h>
#include <DHT_U.h>
#include <Ticker.h>


#define PIN_POT (A0)

int value_pot;
int SENSOR = 2;
int TEMPERATURA;
int HUMEDAD;

DHT dht(SENSOR, DHT11);

void fnTemperatura(){
  TEMPERATURA = dht.readTemperature();
  Serial.println("Temp: " + String(TEMPERATURA));
}

int pot= -1;
void fnPotenciometro(){
  value_pot = analogRead(PIN_POT);

  if(pot != value_pot){

    pot = value_pot;
    Serial.println("Pot: " + String(value_pot));

  }
  
}

//int hum = -1;
void fnHumedad(){
  HUMEDAD = dht.readHumidity();

  //if (hum != HUMEDAD) {
    //hum = HUMEDAD;
    Serial.println("HUM: " + String(HUMEDAD));
  //}
}

Ticker ticTemperatura(fnTemperatura,600);
Ticker ticPotenciometro(fnPotenciometro,100);
Ticker ticHumedad(fnHumedad,800);


void setup() {

  Serial.begin(9600);
  dht.begin();
  delay(30);
  ticTemperatura.start();
  ticPotenciometro.start();
  ticHumedad.start();

}


void loop() {

  ticTemperatura.update();
  ticPotenciometro.update();
  ticHumedad.update();
  delay(500); 

  if (value_pot >= 500){
    digitalWrite(4, HIGH);
  }
  else {
    digitalWrite(4, LOW );
  }
}
