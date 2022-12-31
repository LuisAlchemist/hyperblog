#include <Arduino.h>
#include <DHT.h>
#include <DHT_U.h>
#include <Ticker.h>
#include <Servo.h>


#define PIN_POT (A0)
#define PIN_LED 4
#define PIN_MOT 5

Servo mot;

int value_pot,value_mot = 0, value_led= 0;
int SENSOR = 2;
int TEMPERATURA;
int HUMEDAD;

DHT dht(SENSOR, DHT11);

void fnTemperatura(){
  TEMPERATURA = dht.readTemperature();
  Serial.println("Temp:" + String(TEMPERATURA));
}


void fnPotenciometro(){
  int pot= -1;
  value_pot = analogRead(PIN_POT);

  if(pot != value_pot){

    pot = value_pot;
    Serial.println("Pot:" + String(value_pot));

  }
  
}

void fnHumedad(){
  HUMEDAD = dht.readHumidity();
  Serial.println("HUM:" + String(HUMEDAD));

}

void fnMotor(String cad){
  int pos;
  String label, value;
  cad.trim();
  cad.toLowerCase();
  pos = cad.indexOf(':');
  label= cad.substring(0,pos);
  value = cad.substring(pos+1);

  if(label.equals("mot")){
    if (value_mot != value.toInt())
    {
      value_mot = value.toInt();
      mot.write(value.toInt());
    }
  }

  if(label.equals("led")){
    if (value_led != value.toInt())
    {
      value_led = value.toInt();
      digitalWrite(PIN_LED, value_led);
    }
  }
  
  
  }

Ticker ticTemperatura(fnTemperatura,600);
Ticker ticPotenciometro(fnPotenciometro,100);
Ticker ticHumedad(fnHumedad,800);


void setup() {

  Serial.begin(9600);
  dht.begin();
  delay(30);
  mot.attach(PIN_MOT);
  mot.write(value_mot);
  digitalWrite(PIN_LED,value_led);
  ticTemperatura.start();
  ticPotenciometro.start();
  ticHumedad.start();

}


void loop() {

  if(Serial.available()){

    fnMotor(Serial.readString());


  }
  ticTemperatura.update();
  ticPotenciometro.update();
  ticHumedad.update();
  delay(500); 
}
