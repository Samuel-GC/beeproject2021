float TemPT(){
sensors.requestTemperatures();   //Se envía el comando para leer la temperatura
float PT= sensors.getTempCByIndex(0); //Se obtiene la temperatura en ºC
return PT ;
}
