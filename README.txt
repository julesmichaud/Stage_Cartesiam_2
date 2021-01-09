======================================
This repertory contains documents relating to my internship at Cartesiam.
There are 2 folders, one about the datasets used during my work ("Dataset"), one about codes I wrote ("Code"). There is also a quick presentation about the machine learning (ML) and more specificly about the ML methods applied to recognition of human activities (RAH).
======================================

The objective of this work was creating a RAH application for microcontroller (Arduino Nano 33BLE), thanks to the ML methods proposed by Cartesiam on acceleration measures. For an acceleration measure (according to a specific buffer size and frequency), this app have to recognize a movement among theses learned upstream.

To make that, I searched in a first time datas to exploit. You can find these ones in the dataset folder : "Dataset/Dataset_online". The data found are available in the subfolder "Dataset/Dataset_online/Dataset_brut". To use them, I had to rewrite them in an other format : the rewriting codes are availible in the folder "Code/Dataset_rewriting_codes_python" ; the new dataset is available in the subfolder "Dataset/Dataset_online/Dataset_traite".

But unfortunalty this dataset coudn't be used for some reasons. That's why I did a personal dataset available in the dataset folder : "Dataset/Dataset_personal". I collected data 50 buffers by 50 buffers, the different files are available in the subfolder Dataset/Dataset_personal/Dataset_brut. The regrouped data, used as personal dataset, are available in the subfolder "Dataset/Dataset_personal/Dataset_traite".
The last subfolders, "Dataset/Dataset_personal/Dataset_test" and "Dataset/Dataset_personal/Dataset_preprocessing" contains respectively data separated by buffers number in order to make some tests and data pre-processed in order to find better results, presented later.
Data were collected thanks to an Arduino code I wrote for microntroller, the "acc_buffers.ino" one, available in the subfolder "Code/Microcontroller_codes_arduino".

Once the dataset built, I wrote an Arduino code in order to developp my app on an Arduino Nano 33BLE, "Project_RAH.ino, also available in the subfolder "Code/Microcontroller_codes_arduino". In this subfolder, you can also find "libraries", containing the libraries used in order to make the code work. The "ArduinoBLE" and "Arduino_LSM9DS1" ones are available directly via the Arduino IDE, and the "NanoEdgeAI" one must be added manually to the IDE. This last one contains the classification functions with the library founded by the Studio (93% Accuracy, 92% Confidence, 1.9+1.5kB RAM).

Finaly, I wrote a preprocessing code in order to use feature selections techniques, from machine learning, on my data in order to compare the results obtained with or without preprocessing on my app performances, available in the subfolder "Dataset/Dataset_personal/Dataset_preprocessing".
