/* ESP32 AWS IoT
 *  
 * Simplest possible example (that I could come up with) of using an ESP32 with AWS IoT.
 *  
 * Author: Anthony Elder 
 * License: Apache License v2
 * Sketch Modified by Tarun Bharani
 * Add in Char buffer utilizing sprintf to dispatch JSON data to AWS IoT Core
 * Use and replace your own SID, PW, AWS Account Endpoint, Client cert, private cert, x.509 CA root Cert
 */
#include <WiFiClientSecure.h>
#include <PubSubClient.h> // install with Library Manager, I used v2.6.0
#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT22 
/*
//Used the Below Liberary
//https://github.com/knolleary/pubsubclient

//Enter Your Wifi Name or HotSpot Name i.e. SSID
const char* ssid = "<YOUR-SSID>";
const char* password = "<YOUR-PASSWORD>";

const char* awsEndpoint = "<YOUR-ACCOUNT>-ats.iot.<YOUR-REGION>.amazonaws.com";
*/
const char* ssid = "MOB_016";
const char* password = "123456789";
//1. Sever Address
const char* awsEndpoint = "a31sbnnu6j2qjz-ats.iot.us-west-2.amazonaws.com";

// Update the certificate & Private Key strings below. Paste in the text of your AWS 
// device certificate and private key. 

// Device Certificate
static const char certificatePemCrt[] PROGMEM = R"KEY(
-----BEGIN CERTIFICATE-----
MIIDWTCCAkGgAwIBAgIUGG/onw3xTQIseKhPk3SgLgeZ0s8wDQYJKoZIhvcNAQEL
BQAwTTFLMEkGA1UECwxCQW1hem9uIFdlYiBTZXJ2aWNlcyBPPUFtYXpvbi5jb20g
SW5jLiBMPVNlYXR0bGUgU1Q9V2FzaGluZ3RvbiBDPVVTMB4XDTIyMDYyMjAzMTMw
M1oXDTQ5MTIzMTIzNTk1OVowHjEcMBoGA1UEAwwTQVdTIElvVCBDZXJ0aWZpY2F0
ZTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOc7v7F+c9BxzEpMtS1z
T8Xh436pMo/e6TUoioeGRhfSWxdJXwlEnA6nmV414FT84NBv8dTMFZhsf5cprIfX
7BzyT4sLm7tzlrRc6Lc5lV3MfhlI6FXi7QZFaRRj8Qte/eFnPy+p9FOYRNiaDmxf
EB9+3XTUjq/M+thah1RHOtJ/wgBMKSAY7AoB0QjJFdErdpPApl5K1qDLSucY4o21
UhgUyuwdYR6rzEuPhPByxgRsz2CMKPigxDu/RyGLbQSqvmPQWO2cBgud/pY8KQOK
eH64eDRIkec+cpWUZCU50T2y/zk73g8FCgUh8nhtv4jhgg2fvavvArXdiMXXB1St
z3ECAwEAAaNgMF4wHwYDVR0jBBgwFoAUeLkT+3mbGnnWZxSAJHkIRgxhUqYwHQYD
VR0OBBYEFG2irFfZaXhHrJG1ul2WzOwvfcc5MAwGA1UdEwEB/wQCMAAwDgYDVR0P
AQH/BAQDAgeAMA0GCSqGSIb3DQEBCwUAA4IBAQDXetSFFspb1DGl4xFHUTuzmxVW
zjKo9AZlokwEeATiTLkajS9Wm1ZSptEKnKFGzKI2DC7T6uzNZmopKVEjRW0BTIfs
PHiFjVNbJQ4HIVslc16J58wQvBYdDm4TAh4fQ7xMw0vhOISBppjzIq70EqQ3UTDC
15mjBFe2uTZeCANh3+eyzVQcMJRlYKE5QgNZpS4Z7MM6gcO7iajBoZ4tbzFW7oyr
mLFslMRauL5FpV7DRflORSqCLhbrp8pVm6xIXBSTnL1rnaPjszBHq7aiyjKEh69j
AFK0qOy4OFpydPZKGWUpVvTbaYqx1SbbMpP8NBc/OzE7arDWkTsIDglizLI/
-----END CERTIFICATE-----
)KEY";

// Device Private Key
static const char privatePemKey[] PROGMEM = R"KEY(
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA5zu/sX5z0HHMSky1LXNPxeHjfqkyj97pNSiKh4ZGF9JbF0lf
CUScDqeZXjXgVPzg0G/x1MwVmGx/lymsh9fsHPJPiwubu3OWtFzotzmVXcx+GUjo
VeLtBkVpFGPxC1794Wc/L6n0U5hE2JoObF8QH37ddNSOr8z62FqHVEc60n/CAEwp
IBjsCgHRCMkV0St2k8CmXkrWoMtK5xjijbVSGBTK7B1hHqvMS4+E8HLGBGzPYIwo
+KDEO79HIYttBKq+Y9BY7ZwGC53+ljwpA4p4frh4NEiR5z5ylZRkJTnRPbL/OTve
DwUKBSHyeG2/iOGCDZ+9q+8Ctd2IxdcHVK3PcQIDAQABAoIBAB+7wWj4c6htlZ20
vUCJjK8ZewEM81VvQA39jFVhBgmK4tllRledRNV2BsQ5HJpNQgUY99U+VNBgQ3pZ
S8YwycSHNIdehnbJPCtwfLd4fZkr0TpjGQ+AXwr3R552wMPQu4LNioxeBJvcT8Zy
DfytZycLYBUCfrp9pQdAFUZpqBbvEsIVKcSVtEQMMHfPb7m1UUuQ+2kkOgEJmJwb
ISIbbEBzGUUcXb2a0z2So+52HmfUNguxP/4QOcuWt1Zu4TxHop2Q8vnjtpCyfQvF
LT8ozJegq73ThKIu0xAVcIi45BCTN+e/blITf8277MABSfkFBC2FENnXoUaW5Lmo
4AK/qGkCgYEA+TJ2v0U2rQsQDWLPqqZ9BSgSLfF/24LjPZKdFwVfv1FvZKxjw4zZ
jvol2wCT3ic1l5i3QZ6xkl3zVIFK+WkfIPmFmGWWLfDcb7SeJq6cxGNTXc/ftgpZ
bAGKn4y3XWh1o718XUa4e/qex5m9cr56tvQR7w9xWepNLry38+Q3YUMCgYEA7Yu+
a1egITrurO896jHhpg2EQoMBMxjLXvi5lRNG4EHMHh3dK6jq3WKNFh+hg49+NZAt
YILbyWkyKXiCuU9aO92GOaXVNzezrN/YnWQR2/GTHjEyT1GqwQt01GqzKNGPUX5i
tdot3+x2dYDCHmLv8/VBkkzHk1PXh55H9XMXNzsCgYEAlYxFWzAMSfjTn1TnT4Au
kwOjNVMy6ec4vGDaSVB+T3BtqzsRe+9xOK7CPRWxp6ZcMSgDAixcYHxlZRdaiSce
+UkFdZmxcMyVXaxFJO2xQuJgy3HOzY6Ub47VRD7MZBAmWSeEFO42FKEo3JxU5yGM
v3LluFPKMK29uAilVIZm/cUCgYEAsoxTOIPIjLGrLLk2pI2Ruip2uzeU8z8zvdLe
SzsODwnlzs1LrMFup7Cns3VbBXQZvVD9iolRgnZbiehW+cq3XEAJ39LSDIsFtm8a
dlL9SYCuwAbiddRAsJFX40HAIHJDc1G4CFBSIvmtoGyDfCuJiKlT/A9SA18FpZ5H
ICq9zHkCgYBHOsUvgHpRsbVXSvsJU79C4ymAnHL/a0L1iM8tWxyEhLvwFX3iCykL
TXKVzmJFyRw5RhkwBSiNr71BTQzX0cLznKLrlcKE9JJO8SuLPbo6GedBTQpny3A4
lo8afFmtau/+/9LI4Wo5T3fGHjbVk6f0631iLsOFgykiwIA3IX1PJw==
-----END RSA PRIVATE KEY-----
)KEY";


// This is the AWS IoT CA Certificate from: 
// https://docs.aws.amazon.com/iot/latest/developerguide/managing-device-certs.html#server-authentication
// This one in here is the 'RSA 2048 bit key: Amazon Root CA 1' which is valid 
// until January 16, 2038 so unless it gets revoked you can leave this as is:
// Amazon Root CA 1
static const char rootCA[] PROGMEM = R"EOF(
-----BEGIN CERTIFICATE-----
MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF
ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6
b24gUm9vdCBDQSAxMB4XDTE1MDUyNjAwMDAwMFoXDTM4MDExNzAwMDAwMFowOTEL
MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEZMBcGA1UEAxMQQW1hem9uIFJv
b3QgQ0EgMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALJ4gHHKeNXj
ca9HgFB0fW7Y14h29Jlo91ghYPl0hAEvrAIthtOgQ3pOsqTQNroBvo3bSMgHFzZM
9O6II8c+6zf1tRn4SWiw3te5djgdYZ6k/oI2peVKVuRF4fn9tBb6dNqcmzU5L/qw
IFAGbHrQgLKm+a/sRxmPUDgH3KKHOVj4utWp+UhnMJbulHheb4mjUcAwhmahRWa6
VOujw5H5SNz/0egwLX0tdHA114gk957EWW67c4cX8jJGKLhD+rcdqsq08p8kDi1L
93FcXmn/6pUCyziKrlA4b9v7LWIbxcceVOF34GfID5yHI9Y/QCB/IIDEgEw+OyQm
jgSubJrIqg0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMC
AYYwHQYDVR0OBBYEFIQYzIU07LwMlJQuCFmcx7IQTgoIMA0GCSqGSIb3DQEBCwUA
A4IBAQCY8jdaQZChGsV2USggNiMOruYou6r4lK5IpDB/G/wkjUu0yKGX9rbxenDI
U5PMCCjjmCXPI6T53iHTfIUJrU6adTrCC2qJeHZERxhlbI1Bjjt/msv0tadQ1wUs
N+gDS63pYaACbvXy8MWy7Vu33PqUXHeeE6V/Uq2V8viTO96LXFvKWlJbYK8U90vv
o/ufQJVtMVT8QtPHRh8jrdkPSHCa2XV4cdFyQzR1bldZwgJcJmApzyMZFo6IQ6XU
5MsI+yMRQ+hDKXJioaldXgjUkK642M4UwtBV8ob2xJNDd2ZhwLnoQdeXeGADbkpy
rqXRfboQnoZsG4q5WTP468SQvvG5
-----END CERTIFICATE-----
)EOF";


DHT dht(DHTPIN, DHTTYPE);

WiFiClientSecure wiFiClient;
void msgReceived(char* topic, byte* payload, unsigned int len);
PubSubClient pubSubClient(awsEndpoint, 8883, msgReceived, wiFiClient); 

void setup() {
  Serial.begin(115200); 
  dht.begin();
  delay(50); 
  Serial.println();
  Serial.println("ESP32 AWS IoT Example");
  Serial.printf("SDK version: %s\n", ESP.getSdkVersion());

  Serial.print("Connecting to "); Serial.print(ssid);
  WiFi.begin(ssid, password);
  WiFi.waitForConnectResult();
  Serial.print(", WiFi connected, IP address: "); Serial.println(WiFi.localIP());

  wiFiClient.setCACert(rootCA);
  wiFiClient.setCertificate(certificatePemCrt);
  wiFiClient.setPrivateKey(privatePemKey);
  
}

unsigned long lastPublish;
int msgCount;

void loop() {

  pubSubCheckConnect();

   //If you need to increase buffer size, you need to change MQTT_MAX_PACKET_SIZE in PubSubClient.h
   char fakeData[128];

  float temp =  dht.readTemperature(); //fake number range, adjust as you like
  float humi =  dht.readHumidity();
  if(isnan(temp) || isnan(humi)) {
    Serial.println(F("Failed to read data from sensor"));
  }
  else {
    sprintf(fakeData,  "{\"uptime\":%lu,\"temperature\":%f,\"humidity\":%f}", millis() / 1000, temp, humi);
  }


  if (millis() - lastPublish > 10000) {
  //String msg = String("Hello from ESP32: ") + ++msgCount;
  // boolean rc = pubSubClient.publish("demo", msg.c_str());
  boolean rc = pubSubClient.publish("demo", fakeData);
    Serial.print("Published, rc="); Serial.print( (rc ? "OK: " : "FAILED: ") );
    Serial.println(fakeData);
    lastPublish = millis();

    
  }
}

void msgReceived(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message received on "); Serial.print(topic); Serial.print(": ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void pubSubCheckConnect() {
  if ( ! pubSubClient.connected()) {
    Serial.print("PubSubClient connecting to: "); Serial.print(awsEndpoint);
    while ( ! pubSubClient.connected()) {
      Serial.print(".");
      pubSubClient.connect("ESPthingXXXX");
      delay(1000);
    }
    Serial.println(" connected");
    pubSubClient.subscribe("inTopic");
  }
  pubSubClient.loop();
}
