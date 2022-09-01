//void Puertaabierta()
//{ // for (VELOCIDAD = 0; VELOCIDAD < 256; VELOCIDAD++){  // bucle que incrementa de a uno
//    //if(el sensor de temp esta a mas de 15 se abre)
//  digitalWrite(IN1, LOW);       // IN1 en 0
//  digitalWrite(IN2, HIGH);        // IN2 en 1
//  analogWrite(ENA, 70);        // el valor de velocidad y aplica a ENA
//  delay(2000);      // demora de 2 seg.
//  digitalWrite(ENA, LOW); // ENA en 0 para deshabilitar motor
//  //delay(1000);      // demora de 2 seg.
//   //}
//   return;}
//
//void Puertacerrada()
//{  //if(el sensor de temp esta bajo 15 se cierra){
//  digitalWrite(IN1, HIGH);        // IN1 en 1
//  digitalWrite(IN2, LOW);       // IN2 en 0
//  analogWrite(ENA, 70);        // el valor de velocidad y aplica a ENA
//  delay(2000);            // demora de 50 mseg. por cada iteracion
//  digitalWrite(ENA, LOW); // ENA en 0 para deshabilitar motor
//  //delay(2000);      // demora de 2 seg.
// //}
//  return;
//  }

//  void Puertaabierta()
//{
//  for(int ang=180.0;ang<=1;ang=ang-1)
//  {for(int hz=1;hz<=50;hz++)
//  {digitalWrite(ENA, HIGH);
//  pausa=(ang*2000.0/180.0)+500;
//  digitalWrite(servo,HIGH);
//  delayMicroseconds(pausa);
//  digitalWrite(servo,LOW);
//  delayMicroseconds(23000-pausa);}}
//  digitalWrite(ENA, LOW);
//
//  return;
//
//  }
//
//void Puertacerrada()
//{ for(int hz=1;hz<=50;hz++)
//  {digitalWrite(ENA, HIGH);
//  pausa=(180*2000.0/180.0)+500;
//  digitalWrite(servo,HIGH);
//  delayMicroseconds(pausa);
//  digitalWrite(servo,LOW);
//  delayMicroseconds(23000-pausa);}
//  digitalWrite(ENA, LOW);
//  return;}




void Puertaabierta()
{
  for (int ang = 180; ang >= 15; ang = ang - 1)
  { for (int hz = 0; hz <= 35; hz++)
    { digitalWrite(ENA, HIGH);
      pausa = (ang * 2000.0 / 180.0) + 500;
      digitalWrite(servo, HIGH);
      delayMicroseconds(pausa);
      digitalWrite(servo, LOW);
      delayMicroseconds(2300 - pausa);
    }
  }
  digitalWrite(ENA, LOW);
  posicion = "Abierta";
  posi = 1;
//  PotenciometroP();
//  Serial.print("Value 2= ");
//  Serial.print(potenciometro);
//  Serial.print(" Position = ");
//  Serial.println(poten);
  return posicion;
}

void Puertacerrada()
{
  for (int ang = 15; ang <= 180; ang = ang + 1)
  { for (int hz = 0; hz <= 35; hz++)
    { digitalWrite(ENA, HIGH);
      pausa = (ang * 2000.0 / 180.0) + 500;
      digitalWrite(servo, HIGH);
      delayMicroseconds(pausa);
      digitalWrite(servo, LOW);
      delayMicroseconds(2300 - pausa);
    }
  }
  digitalWrite(ENA, LOW);
  posi = 0;
  posicion = "Cerrada";
//  PotenciometroP();
//  Serial.print("Value 2= ");
//  Serial.print(potenciometro);
//  Serial.print(" Position = ");
//  Serial.println(poten);
  return posicion;
}

void PotenciometroP() {
  digitalWrite(ENA, HIGH);
  delay(100);
  potenciometro = analogRead(angulo);
  poten = map(potenciometro, 640, 270, 0, 100);
  Serial.print("Value 2= ");
  Serial.print(potenciometro);
  Serial.print(" Position = ");
  Serial.println(poten);
  digitalWrite(ENA, LOW);
  return;
}
