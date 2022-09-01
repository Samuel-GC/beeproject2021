void Lluvia()
{
  int value = 0;
   
  //char clima;
  value = digitalRead(lluviaa);  //lectura digital de pin
 
  if (value == LOW) {
     Serial.println("Detectada lluvia");
      cli=1;
      clima="Con Lluvia";
      return clima;
            
  }
  else{
    Serial.println("No Detectado Lluvia");
      cli=0;
      clima="Sin LLuvia";
      return clima;}
  }
