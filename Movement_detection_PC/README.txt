==================================
From the previous datas, I found a classification library with the NanoEdgeAI Studio (by Cartesiam) :
	- 90% Accuracy
	- 90% Confidence
	- 2(+1.5) kB Ram
==================================

This folder contains a zip file and 3 subfolders :
  - libneai_RAH.zip : contains the NanoEdgeAI Studio library (libneai.a) FOR A STM NUCLEOL432KC CARD with his headers (NanoEdge.h and knowledge.h), emulators allowing us to try the lib on PC with some datas (like these in ../Dataset_traite/test/dataset_studio) and some documentation about the library use.
  - src/, inc/, lib/ who contains a C code I wrote to test some datas with the library on PC, as an emulator, but who is easily adaptable for a STM card (especially NUCLEOL432KC) working with an accelerometer (bmi160 for example) and a bluetooth module (hc05 for example).
  !! The C code doesn't work as is, because the library is made for working on a microcontroller (especially nUCLEOL432KC for this one) !!
