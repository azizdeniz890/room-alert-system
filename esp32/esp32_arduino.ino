#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

//Bu kod, ESP32 ile OLED ekran ve buzzer kullanarak bir kişiyi tespit ettiğinde sesli uyarı verir.
// ESP32 DevKit SSD1306 OLED Ekran Buzzer (aktif)
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define BUZZER_PIN 14  // ESP32'nin D14 pinine buzzer bağlı

void setup() {
  Serial.begin(9600);
  pinMode(BUZZER_PIN, OUTPUT);

  // OLED ekran başlat
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("OLED bulunamadı");
    for(;;);
  }

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.println("Hazir...");
  display.display();
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    if (c == '1') {
      // OLED'e yaz
      display.clearDisplay();
      display.setCursor(0,0);
      display.println("Kisi Tespit Edildi!");
      display.display();

      // Buzzer çal
      digitalWrite(BUZZER_PIN, HIGH);
      delay(1000);
      digitalWrite(BUZZER_PIN, LOW);
    }
  }
}
