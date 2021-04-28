import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
#Connection to the AWS IoT Core with Root CA certificate and unique device credentials (keys and certificate) previously retrieved
def helloworld(self,params,packet):
        print('Received message from aws iot core')
        print('Topic: '+ packet.topic)
        print("payload:",(packet.payload))
# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("raspberrpiClientID")
# For TLS mutual authentication
myMQTTClient.configureEndpoint("a3it4w1ulk1j71-ats.iot.us-east-2.amazonaws.com", 8883) #Provide your AWS IoT Core endpoint (Example: "abcdef12345-ats.iot.us-east-1.amazo$
myMQTTClient.configureCredentials("/home/pi/AWSIoT/root-ca.pem", "/home/pi/AWSIoT/private.pem.key", "/home/pi/AWSIoT/certificate.pem.crt") #Set path for Root CA and uniq$
myMQTTClient.configureOfflinePublishQueueing(-1)
myMQTTClient.configureDrainingFrequency(2)
myMQTTClient.configureConnectDisconnectTimeout(10)
myMQTTClient.configureMQTTOperationTimeout(5)
print("Connecting...to mqtt...client...")
myMQTTClient.connect()
#myMQTTClient.subscribe("/home/hellworld",1,helloworld)
print("publishing the message to aws consoler")
while True:
        myMQTTClient.publish(
                topic="home/helloworld",
                QoS=1,
                payload="{'Message':'Message by rpi'}"
)
#while True:
#       time.sleep(5)
