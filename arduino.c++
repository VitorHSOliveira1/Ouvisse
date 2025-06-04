#define NUM_BANDAS 6
int ganhos[NUM_BANDAS];

void setup() {
  Serial.begin(115200);
  Serial.println("ESP32 pronto. Envie os valores separados por vírgula.");
}

void loop() {
  if (Serial.available()) {
    String entrada = Serial.readStringUntil('\n'); // até Enter
    parseGanhos(entrada);
    aplicarGanhos();
  }
}

void parseGanhos(String dados) {
  int idx = 0;
  int inicio = 0;
  for (int i = 0; i < dados.length() && idx < NUM_BANDAS; i++) {
    if (dados.charAt(i) == ',' || i == dados.length() - 1) {
      String valorStr = dados.substring(inicio, i + 1);
      ganhos[idx] = valorStr.toInt();
      idx++;
      inicio = i + 1;
    }
  }
}

void aplicarGanhos() {
  Serial.println("Ganho recebido:");
  for (int i = 0; i < NUM_BANDAS; i++) {
    Serial.print("Banda ");
    Serial.print(i);
    Serial.print(": ");
    Serial.print(ganhos[i]);
    Serial.println(" dB");
    
    // Ajustar o amp
  }
}
