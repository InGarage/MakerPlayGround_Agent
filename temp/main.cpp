#include <Arduino.h>
#include <MP_Delay.h>

#ifndef LED_BUILTIN
#define LED_BUILTIN 12
#endif

MP_Delay s ;
void setup()
{
  // initialize LED digital pin as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  // turn the LED on (HIGH is the voltage level)
  digitalWrite(LED_BUILTIN, HIGH);

  // wait for a second
  s.delayFn("0",1000,"0") ;

  // turn the LED off by making the voltage LOW
  digitalWrite(LED_BUILTIN, LOW);

   // wait for a second
  delay(1000);
}