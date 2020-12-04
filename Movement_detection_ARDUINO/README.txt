==================================
From the previous datas, I found a classification library with the NanoEdgeAI Studio (by Cartesiam) :
	- 90% Accuracy
	- 90% Confidence
	- 2(+1.5) kB Ram
==================================

This folder contains a zip file an Arduino code and a subfolder :
  - libneai_RAH.zip : contains the NanoEdgeAI Studio library (libneai.a) FOR AN ARM CORTEX M4 PROCESSOR (like an Arduino Nano 33BLE card) with his headers (NanoEdge.h and knowledge.h), emulators allowing us to try the lib on PC with some datas (like these in ../Dataset_traite/test/dataset_studio) and some documentation about the library use.
  - Project_RAH.ino : an Arduino code I wrote to test the library on an Arduino Nano 33BLE card with his bluetooth module and his accelerometer integrated.
  - NanoEdgeAI : the library that must be integrated to the code to work correctly.
  
To use the code, you have to download the Arduino IDE : https://www.arduino.cc/
Then, you have to download the "ArduinoBLE" and "Arduino_LSM9DS1" libraries to your work project, and add the NanoEdgeAI folder (library) to the IDE Arduino libraries that already exist.

  !! The Arduino code can only work on an Arduino Nano 33BLE, because the libraries used are specific to this card (especially ArduinoBLE) !!
