#include <ESP8266WiFi.h>
#include <NTPClient.h>
#include <WiFiUdp.h>
#include <FirebaseESP8266.h>
#include "DHT.h"

#define FIREBASE_HOST "ashishfirebase-c098f-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "2GkqeCuIByyiGzVMiO3kWyvQWtKTFR708SuENztR"
#define WIFI_SSID "Avi"
#define WIFI_PASSWORD "7071955977@"

// Define NTP Client to get time
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org");

DHT dht;
FirebaseData fbdo;
FirebaseJson json;
void setup()
{
  Serial.begin(115200);
  Serial.println();
  Serial.println();
  //DHT11
  dht.setup(D1);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();
  
  // Initialize a NTPClient to get time
  timeClient.begin();
  timeClient.setTimeOffset(19800);
  
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);

  fbdo.setBSSLBufferSize(1024, 1024);
  fbdo.setResponseSize(1024);

  Serial.println("Set Timestamp test...");
}

void loop()
{
  String node;
  
  timeClient.update();
  
  //Get a time UNIX
  unsigned long epochTime = timeClient.getEpochTime();
  //Serial.print("Epoch Time: ");
  //Serial.println(epochTime);
  
  int currentTime = epochTime;
  Serial.print("currentTime");
  Serial.println(currentTime);
  
  //Get a time structure
  struct tm *ptm = gmtime ((time_t *)&epochTime); 
  int monthDay = ptm->tm_mday;
  int currentMonth = ptm->tm_mon+1;
  int currentYear = ptm->tm_year+1900;
 

  //Print complete date:
  String currentDate = String(currentYear) + "-" + String(currentMonth) + "-" + String(monthDay);
  Serial.print("Current date: ");
  Serial.println(currentDate);
  
  Serial.println("");
  
  delay(dht.getMinimumSamplingPeriod()); /* Delay of amount equal to sampling period */
  float humidity = dht.getHumidity();/* Get humidity value */
  float temperature = dht.getTemperature();/* Get temperature value */
  Serial.print(dht.getStatusString());/* Print status of communication */
  Serial.print("\t");
  Serial.print(humidity, 1);
  Serial.print("\t\t");
  Serial.print(temperature, 1);
  Serial.print("\t\t");
  float fahrenheit = dht.toFahrenheit(temperature);
  Serial.println(fahrenheit, 1);
  /* Convert temperature to Fahrenheit units */
  
  json.clear().add("F",fahrenheit);
  json.add("C",temperature);
  json.add("H",humidity);
  json.add("Time",currentTime);
  node = "Final/currentData/"+currentDate;
  Firebase.push(fbdo, node.c_str(), json);
  delay(100);
}
