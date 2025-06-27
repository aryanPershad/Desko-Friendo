#include <LiquidCrystal.h>

// LCD pin configuration: RS, E, D4, D5, D6, D7
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  // All LCD pins unchanged

// Pin definitions
const int led1 = 13;  // Built-in LED
const int led2 = 9;   // Second LED
const int buzzer = 8; // Buzzer moved to pin 8

String incomingMessage = "";

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Desko Friendo :)");

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n') {
      // === Display message on LCD ===
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print(incomingMessage.substring(0, 16));
      lcd.setCursor(0, 1);
      if (incomingMessage.length() > 16) {
        lcd.print(incomingMessage.substring(16, 32));
      }

      // === Blink LEDs ===
      digitalWrite(led1, HIGH);
      digitalWrite(led2, HIGH);

      // === Beep the buzzer ===
      tone(buzzer, 1000, 300);  // 1000 Hz for 300 ms
      delay(300);
      noTone(buzzer);

      // === Turn off LEDs ===
      digitalWrite(led1, LOW);
      digitalWrite(led2, LOW);

      // Clear message buffer
      incomingMessage = "";

    } else {
      incomingMessage += c;
    }
  }
}


