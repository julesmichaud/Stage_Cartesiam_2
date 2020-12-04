======================================
This repertory contains documents relating to my internship at Cartesiam.
There are 4 folders, two about the datasets used during my work, two about codes I wrote. There are also two files,
a quick presentation about the machine learning (ML) and more specificly about the ML methods applied to recognition of human activities (RAH),
and also a bibliography containing all the references I used during my work.
=====================================

The objective of this work was creating a RAH application for microcontroller (Arduino Nano 33BLE),
thanks to the ML methods proposed by Cartesiam on acceleration measures.
For an acceleration measure (according to a specific buffer size and frequency), this app have to recognize a movement among theses learned upstream.
To make that, I searched in a first time datas to exploit. You can find these ones on the first folder : Dataset_brut.

Then, I had to find a library proposed by Cartesiam (especificly by the NanoEdgeAI Studio by Cartesiam), which creates classes each corresponding to a movement.
Once found, I can use it in a code for an Arduino Nano 33BLE card to complete my task (a RAH app).
But to use theses datas, I had to write them in an other format in order to use them in the NEAI Studio.
You can find theses datas in the second folder : Dataset_traite.

After my library in my pocket, I searched to write a little C code who can try to class accelerations measure using my new library directly on PC,
and who can be easily changed to work on a STM microcontroller.
However, the library is designed to be used on a microcontroller so the code doesn't work as it, but it can be used to write a new one for a STM card.
You can find this code in the third folder : Movement_detection_PC.

Finaly, I wrote an Arduino code in order to developp my app on an Arduino Nano 33BLE, the code is availible in the last folder : Movement_detection_ARDUINO.
