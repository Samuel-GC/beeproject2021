void Prueba() {
  DateTime now = rtc.now();
  horas = now.hour();
  minutos = now.minute();
   Serial.print("Flag Humedad: ");
  Serial.println(anomaliaHUM);
  Serial.print("Flag Peso: ");
  Serial.println(anomaliaPES);
  Serial.print("Flag Puerta: ");
  Serial.println(anomaliaPUE);
  Serial.print("Flag Alimento: ");
  Serial.println(anomaliaALI);
  Serial.print(horas);
  Serial.print(":");
  Serial.println(minutos);
  dis = nivelcomida();           //dato almacenado de distancia en la variable dis
  Serial.print("Porcentaje de comida: ");
  Serial.print(dis);
  Serial.println(" %");
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
//    //Puertaabierta();
//    Serial.print("Piquera: ");
//  Serial.println(posicion);
  PotenciometroP();
    Serial.print("revision: ");
    Serial.println(rev);
  //  delay(2000);
  //  Puertacerrada();
  //  Serial.print("Piquera: ");
  //  Serial.println(posicion);
  //PotenciometroP();
  //  delay(2000);
  //  VentiladorON();
  //  Serial.print("Ventilador: ");
  //  Serial.println(venti);
  //  delay(2000);
  //  VentiladorOFF();
  //  Serial.print("Ventilador: ");
  //  Serial.println(venti);
  //  EnvioData();
  //  EnvioRev();
  delay(2000);
  return;
}
