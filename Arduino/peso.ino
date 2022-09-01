float galga(){
  float kilo;
    #ifdef DEBUG_HX711
    kilo=bascula.get_units();
    //Serial.println(kilo);
    #endif
    return kilo;
}
