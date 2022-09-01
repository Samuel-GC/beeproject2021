//ENVIO DE DATOS DE LA COLMENA_1-------------------------------------------------
void EnvioData(){
  Serial.println("");
  Serial.println("**************************Envio de data**********************************");

  /********************GSM Communication Starts********************/

    myserial.println("AT");
  delay(3000);

  myserial.println("AT+SAPBR=3,1,\"Contype\",\"GPRS\"");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=3,1,\"APN\",\"entel.pe\"");//APN
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=0,1");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=1,1");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=2,1");
  delay(6000);
  ShowSerialData();


  myserial.println("AT+HTTPINIT");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+HTTPPARA=\"CID\",1");
  delay(6000);
  ShowSerialData();

  StaticJsonDocument<200> doc;
  doc["nombre"] = "colmena_1";
  doc["local"]  = "Wayllapampa";
  doc["clima"]  = clima;
  doc["t_ext"]  = TemPT();
  doc["t_int"]  = Tdht22();
  doc["humedad"]= Hdht22();
  doc["peso"]   = galga();
  doc["comida"] = nivelcomida();
  doc["piquera"]= posicion; //este valor no fue definido asi que se se tiene que revisar
  //doc["revision"] = fecha;
  serializeJson(doc, output);
  delay(4000);

  myserial.println("AT+HTTPPARA=\"URL\",\"http://beeproject2021.pythonanywhere.com/add_data/cs/\""); //Server address
  delay(4000);
  ShowSerialData();

  myserial.println("AT+HTTPPARA=\"USERDATA\",\"Authorization: token c964678467cd53d0d79ca131f3463bba776d17d8\"");
  delay(4000);
  ShowSerialData();
  myserial.println("AT+HTTPPARA=\"CONTENT\",\"application/json\"");
  delay(4000);
  ShowSerialData();


  myserial.println("AT+HTTPDATA=" + String(output.length()) + ",100000");
  Serial.println(output);
  delay(6000);
  ShowSerialData();

  delay(6000);
  myserial.println(output);
  delay(6000);
  ShowSerialData;

  myserial.println("AT+HTTPACTION=1");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+HTTPREAD");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+HTTPTERM");
  delay(10000);
  ShowSerialData;
  output="";
  /********************GSM Communication Stops********************/
}

//ENVIO DE FECHA DE REVISIONZZ<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
void revision(){
    rev=1;
  }
void EnvioRev(){
   DateTime now = rtc.now();
   valorActual = now.day();// aca valorActual tiene el dia
   //Hrev=Henvio+5;
   //lo primero es dejar en claro que rev es 0 y cambia a uno al suceder la interrupcion
  if(rev==1 && ((now.minute()<(Henvio-5) || now.minute()>(Henvio+2))&&(now.minute()<(Henvio2-5) || now.minute()>(Henvio2+5)))){
    if (valorActual != valorAnterior){ 
       Serial.println("Son distintos enviando revision");
       valorAnterior = valorActual;

  Serial.println("");
  Serial.println("*************************Envio de revision***********************************");

  /********************GSM Communication Starts********************/

    myserial.println("AT");
  delay(3000);

  myserial.println("AT+SAPBR=3,1,\"Contype\",\"GPRS\"");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=3,1,\"APN\",\"entel.pe\"");//APN
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=0,1");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=1,1");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=2,1");
  delay(6000);
  ShowSerialData();


  myserial.println("AT+HTTPINIT");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+HTTPPARA=\"CID\",1");
  delay(6000);
  ShowSerialData();

  StaticJsonDocument<200> doc;
  doc["nombre"] = "colmena_1";

  serializeJson(doc, output);
  delay(4000);

  myserial.println("AT+HTTPPARA=\"URL\",\"http://beeproject2021.pythonanywhere.com/add_data/revision/\""); //Server address
  delay(20000);
  ShowSerialData();

  myserial.println("AT+HTTPPARA=\"USERDATA\",\"Authorization: token c964678467cd53d0d79ca131f3463bba776d17d8\"");
  delay(4000);
  ShowSerialData();
  myserial.println("AT+HTTPPARA=\"CONTENT\",\"application/json\"");
  delay(4000);
  ShowSerialData();


  myserial.println("AT+HTTPDATA=" + String(output.length()) + ",100000");
  Serial.println(output);
  delay(6000);
  ShowSerialData();

  delay(6000);
  myserial.println(output);
  delay(6000);
  ShowSerialData;

  myserial.println("AT+HTTPACTION=1");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+HTTPREAD");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+HTTPTERM");
  delay(10000);
  ShowSerialData;
  output="";
  /********************GSM Communication Stops********************/
  rev=0;//manda rev a 0 para que pueda activarese de nuevo 
 Serial.println("---------------------------------------------------------------");
 
}  
    }
    }

//ENVIO DE ALERTAS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
void EnvioAler(){
   //lo primero es dejar en claro que rev es 0 y cambia a uno al suceder la interrupcion
   DateTime now = rtc.now();
   valorActual = now.day();
  if((anomaliaHUM==1||anomaliaALI==1||anomaliaPES==1 || anomaliaPUE==1)&& ((now.minute()<(Henvio-5) || now.minute()>(Henvio+2))&&(now.minute()<(Henvio2-5) || now.minute()>(Henvio2+2)))){
    
 if(anomaliaHUM==1){
  alerta = "Exceso de humedad posible inundación";
  caso=1;
  }
 if(anomaliaALI==1){
  alerta ="Poca comida en el alimentador" ;
  caso=2;
  }
 if(anomaliaPES==1){
  alerta = "Anomalía de Peso posible caida o enjambrazón";
  caso=3;
  }
 if(anomaliaPUE==1){
  alerta = "Obstrucción en la puerta de la piquera o apertura accidental";
  caso=4;
  }
  Serial.print("ALERTA: ");
  Serial.println(alerta); 
  Serial.println("");
  Serial.println("*************************Envio de alerta***********************************");

  /********************GSM Communication Starts********************/

    myserial.println("AT");
  delay(3000);

  myserial.println("AT+SAPBR=3,1,\"Contype\",\"GPRS\"");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=3,1,\"APN\",\"entel.pe\"");//APN
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=0,1");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=1,1");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+SAPBR=2,1");
  delay(6000);
  ShowSerialData();


  myserial.println("AT+HTTPINIT");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+HTTPPARA=\"CID\",1");
  delay(6000);
  ShowSerialData();

  StaticJsonDocument<200> doc;
  doc["error"] = alerta;

  serializeJson(doc, output);
  delay(4000);

  myserial.println("AT+HTTPPARA=\"URL\",\"http://beeproject2021.pythonanywhere.com/add_error/\""); //Server address
  delay(20000);
  ShowSerialData();

  myserial.println("AT+HTTPPARA=\"USERDATA\",\"Authorization: token c964678467cd53d0d79ca131f3463bba776d17d8\"");
  delay(4000);
  ShowSerialData();
  myserial.println("AT+HTTPPARA=\"CONTENT\",\"application/json\"");
  delay(4000);
  ShowSerialData();

  myserial.println("AT+HTTPDATA=" + String(output.length()) + ",100000");
  Serial.println(output);
  delay(6000);
  ShowSerialData();

  delay(6000);
  myserial.println(output);
  delay(6000);
  ShowSerialData;

  myserial.println("AT+HTTPACTION=1");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+HTTPREAD");
  delay(6000);
  ShowSerialData();

  myserial.println("AT+HTTPTERM");
  delay(10000);
  ShowSerialData;
  output="";
  /********************GSM Communication Stops********************/
if(caso==1){
  evioHUM=valorActual;
  anomaliaHUM=0;}
if(caso==2){
  evioALI=valorActual;
  anomaliaALI=0;}
if(caso==3){
  evioPES=valorActual;
  anomaliaPES=0;}
  if(caso==4){
  evioPUE=valorActual;
  anomaliaPUE=0;}
    Serial.println(alerta);  
    Serial.println("---------------------------------------------------------------");
    }
   }


void ShowSerialData()
{
  while (myserial.available() != 0)
    Serial.write(myserial.read());
  delay(1000);}
