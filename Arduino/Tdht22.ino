float Tdht22()
{ 
   float t22 = dht1.readTemperature();
   if (isnan(t22)) {
   Serial.println("Failed to read from DHT sensor!");
   return;
   }
   return t22;
}

float Hdht22()
{ 
   float h22 = dht1.readHumidity();
   if (isnan(h22)) {
   Serial.println("Failed to read from DHT sensor!");
   return;
   }
   return h22;
}
