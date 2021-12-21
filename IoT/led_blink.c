#include <wiringPi.h>
#define RLED_PIN 3
#define YLED_PIN 4
#define GLED_PIN 5
int main (void)
{
  wiringPiSetup () ;
  pinMode (RLED_PIN, OUTPUT) ;
  pinMode (YLED_PIN, OUTPUT) ;
  pinMode (GLED_PIN, OUTPUT) ;
  for (int i=0; i<5; i++)
  {
    digitalWrite (RLED_PIN, HIGH) ; delay (1000) ;
    digitalWrite (RLED_PIN,  LOW) ;
    digitalWrite (YLED_PIN, HIGH) ; delay (1000) ;
    digitalWrite (YLED_PIN,  LOW) ;
    digitalWrite (GLED_PIN, HIGH) ; delay (1000) ;
    digitalWrite (GLED_PIN,  LOW) ;
  }
  return 0 ;
}