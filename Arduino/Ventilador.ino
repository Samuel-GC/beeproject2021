void VentiladorON() {
  analogWrite(ventilador, 150);        // el valor de velocidad y aplica a ENA2
  venti="encendido";
  return venti;
}
void VentiladorOFF() {
   analogWrite(ventilador, LOW);        // el valor de velocidad y aplica a ENA2
   venti="apagado";
  return venti;
}
