Stasis Macropad (v1)

My first PCB, as well as first project for forge. (Originally planned to be submitted to Stasis, hence the name)

A basic macropad with:
6 keys,
A rotary encoder switch,
A OLED display

This project is meant both as a useful tool for me to use (i might try using it for things like tetris or such) and a perfect learning oppertunity. I have never done hardware hackathons/projects before, so this is a really good chance for me to learn. I originally used the hackclub macropad tutorial, and then deviated from it to get to what i have now. (https://hackpad.hackclub.com/guide) 
The keys are arranged in a matrix, and the display and rotary encoder are wired in seprately (from the matrix). The microcontroller im using ([XIAO-SEEEDUINO](https://wiki.seeedstudio.com/Seeeduino-XIAO/)) has USB-C connection for power. The firmware is written in python with KMK. 

3D render of the pcb
<img width="590" height="556" alt="Screenshot_20260518_123826" src="https://github.com/user-attachments/assets/2f21e1a7-3dea-4f72-90b7-37a05b850e93" />

Schematics and layout
<img width="753" height="731" alt="Screenshot_20260422_045628" src="https://github.com/user-attachments/assets/e5d9cc30-3aba-4b55-bddf-f7bedcafc28f" />
<img width="1150" height="524" alt="Screenshot_20260408_122429" src="https://github.com/user-attachments/assets/e2feafab-5365-4f10-aa40-a9d5405c9b16" />

Case
<img width="801" height="747" alt="Screenshot_20260426_073638" src="https://github.com/user-attachments/assets/41b7eb34-df41-4cea-9f26-3c4e7f0ce77e" />
<img width="897" height="725" alt="Screenshot_20260426_073651" src="https://github.com/user-attachments/assets/20bc1346-0fd1-4718-9b8e-e6a0ebaf10fd" />

Keys
<img width="895" height="693" alt="Screenshot_20260426_073731" src="https://github.com/user-attachments/assets/3f15b144-956f-4065-b044-f676744a2a15" />

BOM
|Name                        |Purpose                                                                   |Quantity|Total Cost (USD)|Link                                                                                 |Distributor    |
|----------------------------|--------------------------------------------------------------------------|--------|----------------|-------------------------------------------------------------------------------------|---------------|
|PCB                         |The actual pcb                                                            |1       |2               |                                                                                     |JLCPCB         |
|3d Printed Case & Keys      |The case and keys                                                         |1       |7               |                                                                                     |Printing Legion|
|Cherry MX Switch (MX1A-L1NN)|The keys of this macropad                                                 |6       |6               |https://www.mouser.com/ProductDetail/CHERRY/MX1A-L1NN?qs=F5EMLAvA7IDlALNAurZTXA%3D%3D|Mouser         |
|0.91" OLED Graphic 128x32   |The display of this macropad; im going to try to make it log recent inputs|1       |3.9            |https://www.amazon.com/gp/product/B079BN2J8V/ref=ox_sc_act_title_1?smid=A1N6DLY3NQK2VM&psc=1|Amazon  |
|SEEEDUINO XIAO              |The microcontroller of this macropad                                      |1       |5.4             |https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/102010328/11506471|Digikey        |
|1N4148                      |Preventing ghosting in the keyboard matrix                                |6       |0.6             |https://www.digikey.com/en/products/detail/onsemi/1N4148/458603                      |Digikey        |
|EC11E15244G1                |Changing volume                                                           |1       |4.63            |https://www.digikey.com/en/products/detail/alps-alpine/EC11E15244G1/21721550         |Digikey        |
