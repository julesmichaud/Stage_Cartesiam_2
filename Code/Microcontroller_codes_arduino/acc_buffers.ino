/*
This code will save datas in order to create a dataset.
To start, when using the dispositif with the Arduino card,
you have to start receiving datas (with for exemple cat /dev/ttyACM0 > thing.txt on linux)
Then, prepare yourself to the collect and let's move.
By default, each buffer size is 128, the collect frequency is 119Hz and we collect 50 buffers.
You can change theses parameters in the code if necessary.
*/


/* Configuration */

#include <Arduino_LSM9DS1.h> //accelerometer functions module

#define DATA_INPUT_USER 128
#define AXIS_NUMBER 3

//Datas structures for accelerations measure
float acc_buffer[DATA_INPUT_USER * AXIS_NUMBER] = { 0 }; //Accelerations buffer
float acc_x = 0.F;
float acc_y = 0.F;
float acc_z = 0.F;


void setup() {
  //LED configuration, to notify the advancement
  pinMode(LED_BUILTIN, OUTPUT);
  
  //Serial configuration, waiting 3s in order to avoid any haste
  
  Serial.begin(9600);
  digitalWrite(LED_BUILTIN, HIGH);
  while(!Serial);
  digitalWrite(LED_BUILTIN, LOW);

  //Modules initializing verifications
  if (!IMU.begin())
  {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  delay(3000);
}


/* Loop */

void loop() {
  if (IMU.accelerationAvailable())
  {
    // Turn on the LED for 15sec to indicate the start:
    digitalWrite(LED_BUILTIN, HIGH);
    delay(5000);
    digitalWrite(LED_BUILTIN, LOW);

    //Main loop
    int counter = 0;
    long previousMillis = 0;
    while(counter < 50)
    {
        //We collect a buffer every 0.2sec. This avoids a disconnection due to a 'delay()'
        long currentMillis = millis();
        if (currentMillis - previousMillis >= 200)
        {
            fill_acc_buffer();
            get_acc_values();

            Serial.print("\n");
            counter ++;
            previousMillis = currentMillis;
        }
      
    }
    //End of datas reception
    digitalWrite(LED_BUILTIN, HIGH);
    while(1);   
  }
}

void fill_acc_buffer() {
  //Acceleration buffer, module frequency is 119Hz
     
    for (int i = 0; i < DATA_INPUT_USER; i++) {
      IMU.readAcceleration(acc_x, acc_y, acc_z);
      acc_buffer[AXIS_NUMBER * i] = acc_x;
      acc_buffer[AXIS_NUMBER * i + 1] = acc_y;
      acc_buffer[AXIS_NUMBER * i + 2] = acc_z;
    }
}

void get_acc_values() {
    //Prints the acceleration buffer's datas
    
    for (int i = 0; i < DATA_INPUT_USER; i++) 
    {
      Serial.print(acc_buffer[AXIS_NUMBER * i]);
      Serial.print(" ");
      Serial.print(acc_buffer[AXIS_NUMBER * i +1]);
      Serial.print(" ");
      Serial.print(acc_buffer[AXIS_NUMBER * i +2]);
      Serial.print(" ");
    }

}
