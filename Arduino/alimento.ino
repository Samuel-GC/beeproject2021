int nivelcomida()
{
  float t; //timepo que demora en llegar el eco
  float x;
  //  long t; //timepo que demora en llegar el eco
  //  long x;
  float d; //distancia en centimetros
  int a = 0;
  float dis;
  float dx = 0;
  float valormin = 21.5;
  float valormax = 6.5;
  digitalWrite(34, HIGH); // activo el voltaje
  delay(100);// cambie de 1.5s

  digitalWrite(Trigger, HIGH);
  delayMicroseconds(10);          //Enviamos un pulso de 10us
  digitalWrite(Trigger, LOW);
  t = pulseIn(Echo, HIGH); //obtenemos el ancho del pulso
  x = t / 59;           //escalamos el tiempo a una distancia en cm
  digitalWrite(Echo, LOW);
  digitalWrite(34, LOW); //desactivamos el voltaje
  d = (-100 / (valormin - valormax)) * (x - valormax) + 100 ;
  delay(500);
  //d= map(x, 3.5, 22, 100, 0);

  //    if (d <= 0 && d >= -5) {
  //      d = 1;
  //    }
  if (d >= 103) {
    d = -50;
  }

  // ---------------------------------------------------- prueba--------------------
  //  float valormin = 21;
  //  float valormax = 6.5;
  //  for (a=0 ; a <= 2; a++) {
  //    digitalWrite(Trigger, HIGH);
  //    delayMicroseconds(10);          //Enviamos un pulso de 10us
  //    digitalWrite(Trigger, LOW);
  //    t = pulseIn(Echo, HIGH);        //obtenemos el ancho del pulso
  //    digitalWrite(Echo, LOW);
  //    x = t / 59;
  //    dis = (-100/(valormin - valormax))*(x-valormax)+100 ;
  //    //if(dx==0){dx=dis;}
  //    Serial.println(dis);
  //    dx=dx+dis;
  //    Serial.println(dx);
  //    delay(500);
  //  }
  //
  //  d=dx/3;
  //---------------------------------------------------------
  digitalWrite(34, LOW); //desactivamos el voltaje
  //Serial.println(d);
  //Serial.println(x); //distancia en centimetro
  return d;
}
