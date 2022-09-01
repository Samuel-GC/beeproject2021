 //El programa dura 2:19 en completarse
//en el ensayo 7 vamos con las condiciones para envios de alertas y accionar los actuadores
//------------------Librerias-----------------------------------
//---------------------------------------------------------------
//Clock
#include <DS3231.h>
//#include<Wire.h>
#include "RTClib.h"
//Galgas<<<<<<<<<<<<<<<<<<<<<<<
#include "HX711.h"
#define DEBUG_HX711
//#define CALIBRACION -29390.0  //valor de calibracion referencial
#define CALIBRACION   -31450.0 // valor de calibracion actual
HX711 bascula;
//Ultrasonido<<<<<<<<<<<<<<<<<<
//:Ninguna libreria
//PT100
#include <OneWire.h>
#include <DallasTemperature.h>
//DHT22
#include "DHT.h"
#define DHTTYPE1 DHT22
//Puerta
// :Ninguna libreria

//Envio de Datos<<<<<<<<<<<<<<<
#include <SoftwareSerial.h>
#include <ArduinoJson.h>


//-------------------Pines----------------------------------------
//-----------------------------------------------------------------
//Galga<<<<<<<<<<<<<<<<<<<<<<<
byte pinData = 3;
byte pinClk = 2;
float kg;
float kganterior;
//Ultrasonido<<<<<<<<<<<<<<<<<
const int Trigger = 8;
const int Echo = 9;
int dis;
//PT100<<<<<<<<<<<<<<<<<<<<<<<
OneWire ourWire(16);                //Se establece el pin 16  como bus OneWire
DallasTemperature sensors(&ourWire); //Se declara una variable u objeto para nuestro sensor
float tpt;
//DHT22<<<<<<<<<<<<<<<<<<<<<<<<
const int DHTPin1 = 4;
DHT dht1(DHTPin1, DHTTYPE1);
float h1;
float t1;
//Puerta<<<<<<<<<<<<<<<<<<<<<<<<
int IN3 = 31;      // IN3 de L298N deveria ser siempre LOW
int ENA = 29;      // ENA2 de L298N esto descativa y activa el servo
int servo = 46;      // ENA de L298N
char *posicion;//<<<<<<<<<<<<<<<<<<<<<<<< ESTO SE TIENE QUE REVISAR FALTARIA HACER 2 SOLDADURAS EN LA PLACA
int posi;
float pausa;
int potenciometro;
int poten;
const int angulo = A3;
//Ventilador<<<<<<<<<<<<<<<
int ventilador = 28;
char *venti;
//Clock<<<<<<<<<<<<<<<<<<<<<<<<
RTC_DS3231 rtc;
//DS3231  rtc(SDA, SCL);//20/21
int horas;
int minutos;

//Envio de Datos<<<<<<<<<<<<<<<
SoftwareSerial myserial(10, 11); // RX: 10, TX:11
String output;
int Henvio;
int Henvio2;
int Hrev;
char *alerta;
int flagantiguo;
int flag;
//Sensor de Lluvia<<<<<<<<<<<<<<<
int lluviaa = 24;
char *clima;
int cli;
//revision<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
int rev;
int valorAnterior = 0;
int valorActual;
//Alertas<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
int evioHUM = 0;
int evioPES = 0;
int evioALI = 0;
int evioPUE = 0;
int anomaliaHUM = 0;
int anomaliaPES = 0;
int anomaliaALI = 0;
int anomaliaPUE = 0;
int caso = 0;
int rango_p;
int rango_n;
int minutoanterior;
//--------------------Setup-----------------------------------------------------}
//--------------------------------------------------------
void setup() {

  //Galga<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#ifdef DEBUG_HX711
  Serial.begin(9600);
#endif
  bascula.begin(pinData, pinClk);
  bascula.set_scale(CALIBRACION);
  //Ultrasonido<<<<<<<<<<<<<<<<<<<<<<<<<<
  pinMode(Trigger, OUTPUT);
  pinMode(Echo, INPUT);
  digitalWrite(Trigger, LOW);
  pinMode(34, OUTPUT);
  dis = nivelcomida();
  //PT100<<<<<<<<<<<<<<<<<<<<<<<
  sensors.begin();   //Se inicia el sensor
  //DHT22<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  dht1.begin();
  //Puerta<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  pinMode(IN3, OUTPUT);   //
  pinMode(ENA, OUTPUT);   //
  pinMode(servo, OUTPUT);   //
  pinMode(angulo, INPUT);
  //Ventilador<<<<<<<<<<<<<<<
  pinMode(ventilador, OUTPUT);
  //Puerta<<<<<<<<<<<<<<<
  digitalWrite(IN3, LOW);
  //posicion="Cerrada";
  Puertacerrada();
  //Switch<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  pinMode(19, INPUT);
  //Clock<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  Wire.begin();
  rtc.begin();
  if (! rtc.begin()) {
    Serial.println("Couldn't find RTC");
    }
  //Envio de Datos<<<<<<<<<<<<<<<<<<<<<<<<
  myserial.begin(9600);        // the GPRS baud rate
  Serial.println("Initializing..........");
  DynamicJsonDocument doc(1024);
  delay(2000);
  //Interrupcion de Revision<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  attachInterrupt(digitalPinToInterrupt(19), revision, CHANGE);
  rev = 0;

}
//---------------------Loop-----------------------------------------------------------------------
//------------------------------------------------------------------------------------------------

void loop() {
  //Clock<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  //---------------------------SOLO DE PRUEBA DE SENSORES----------------------------------------------

   //-Prueba();//solo descomentar para poder realizar el print de sensores movimiento de actuadores y ensayo de envios

  //--------------------------------SOLO DE PRUEBA-------------.-----------------------------
  DateTime now = rtc.now();
  //SITEMA DE ENVIO -HORARIO DE ENVIO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  //esto no se cambia
  Henvio = 6; //define el MINUTO de envio inicial y ademas el tiempo base para esperar la revision
  Henvio2 = 36;
  minutos = now.minute();
  if ((minutos == Henvio || minutos == Henvio2)  ) {

    horas = now.hour();
    minutos = now.minute();
    Serial.print(horas);
    Serial.print(":");
    Serial.println(minutos);
    dis = nivelcomida();           //dato almacenado de distancia en la variable dis
    Serial.print("Distancia: ");
    Serial.print(dis);
    Serial.println("cm");
    tpt = TemPT();
    Serial.print("PT100 Temperatura= ");
    Serial.print(tpt);
    Serial.println(" C");
    h1 = Hdht22();
    t1 = Tdht22();
    Serial.print("Dht 22 Humidity: ");
    Serial.print(h1);
    Serial.print(" %\t");
    Serial.print("Temperature: ");
    Serial.print(t1);
    Serial.println(" *C ");
    Lluvia();
    Serial.println("Peso");
    kg = galga();                  //dato almacenado del peso en la variable kg
    Serial.print(kg, 1);
    Serial.print(" Kg");
    Serial.println();
    int sensorVal = digitalRead(19);
    if (sensorVal == HIGH) {
      Serial.println("No presionado");
    }
    else {
      Serial.println("Presionado");
    }
    EnvioData();
    Serial.println("---------------------------------------------------------------");
  }
  //Envio de Revision<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  EnvioRev();

  //SISTEMA DE SUPERVISION Y ENVIO DE ALERTAS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
  minutos = now.minute();
  valorActual = now.day();
  //solo se puso el ! para hacer pruebas para el final poner ==

  if ((minutos % 5) == 0 && minutos != minutoanterior) {
    //  if ((minutos % 5)!= 0 ) {
    minutoanterior = minutos;
    valorActual = now.day();
    horas = now.hour();
    minutos = now.minute();
    tpt = TemPT();
    h1 = Hdht22();
    t1 = Tdht22();
    Lluvia();
    //    if (valorActual != evioALI) {
    //      dis = nivelcomida();
    //    }
    if (valorActual != evioPES) {
      kg = galga();
    }
    if (valorActual != evioPUE) {
      PotenciometroP();
    }
    //---------------------tipos de alarmas----------------------
    if (h1 >= 80) {
      if (valorActual != evioHUM) {
        anomaliaHUM = 1;
      }
    }
    if (kg <= 8) {
      if (valorActual != evioPES) {
        anomaliaPES = 1;
      }
    }
    if (dis <= 10 && dis > 0) {
      if (valorActual != evioALI) {
        anomaliaALI = 1;
      }
    }
    if ((poten <= 60 && posi == 1) || (poten >= 30 && posi == 0)) {
      if (valorActual != evioPUE) {
        anomaliaPUE = 1;
      }
    }
    //-------------Manejo de actuadores--------------------
    rango_p = 40;
    rango_n = 20;
    if (cli == 0) {

      // calor ext e interior muy altos
      if (tpt >= rango_p && t1 >= rango_p) {
        VentiladorON();
        if (posi != 1) {
          Puertaabierta();
        }
        Serial.println("caso1 vent ON puerta ABIERTA");
      }
      // calor ext e interior muy bajos
      else if (tpt <= rango_n && t1 <= rango_n) {
        VentiladorOFF();
        if (posi != 0) {
          Puertacerrada();

        }
        Serial.println("caso2 vent OFF puerta CERRADA");
      }

      // calor ext es baja y la interior es alta
      else if (tpt <= rango_n && t1 > rango_n) {
        VentiladorOFF();
        if (posi != 0) {
          Puertacerrada();
        }

        Serial.println("caso3 vent OFF puerta CERRADA");
      }
      // calor ext es alta y la interior es baja
      else if (tpt >= rango_p && t1 < rango_p) {
        VentiladorOFF();
        if (posi != 1) {
          Puertaabierta();
        }
        Serial.println("caso4 vent OFF puerta ABIERTA");
      }
      //else
      else {
        VentiladorOFF();
        if (posi != 1) {
          Puertaabierta();
        }
        Serial.println("caso ELSE vent OFF puerta ABIERTA");
      }
    }

    else {
      VentiladorOFF();
      if (posi != 0) {
        Puertacerrada();
      }
      Serial.println("caso5 LLUVIA vent OFF puerta CERRDA");
    }

  }
    EnvioAler();
}
