Stasis Macropad (v1)

My first PCB, as well as first project for stasis.

A basic macropad with:
6 keys,
A rotary encoder switch,
A OLED display

This project is meant both as a useful tool for me to use (i might try using it for things like tetris or such) and a perfect learning oppertunity. I have never done hardware hackathons/projects before, so this is a really good chance for me to learn. I originally used the hackclub macropad tutorial, and then deviated from it to get to what i have now. (https://hackpad.hackclub.com/guide)

3D render of the pcb
<img width="572" height="549" alt="Screenshot_20260422_045616" src="https://github.com/user-attachments/assets/ce6af854-f952-4dcb-b8df-3655c85ffaf1" />

Schematics and layout
<img width="801" height="747" alt="Screenshot_20260426_073638" src="https://github.com/user-attachments/assets/41b7eb34-df41-4cea-9f26-3c4e7f0ce77e" />
<img width="897" height="725" alt="Screenshot_20260426_073651" src="https://github.com/user-attachments/assets/20bc1346-0fd1-4718-9b8e-e6a0ebaf10fd" />


Case
<img width="718" height="634" alt="Screenshot_20260410_131247" src="https://github.com/user-attachments/assets/4435f286-1a0f-43cd-9e82-3b5517b1bb25" />
<img width="877" height="766" alt="Screenshot_20260423_130401" src="https://github.com/user-attachments/assets/d91fae50-c254-4f5c-8e7c-f1df245dec75" />

Keys
<img width="895" height="693" alt="Screenshot_20260426_073731" src="https://github.com/user-attachments/assets/3f15b144-956f-4065-b044-f676744a2a15" />

BOM
|Name                        |Purpose                                                                   |Quantity|Total Cost (USD)|Link                                                                                 |Distributor    |
|----------------------------|--------------------------------------------------------------------------|--------|----------------|-------------------------------------------------------------------------------------|---------------|
|PCB                         |The actual pcb                                                            |1       |2               |                                                                                     |JLCPCB         |
|3d Printed Case & Keys      |The case and keys                                                         |1       |7               |                                                                                     |Printing Legion|
|Cherry MX Switch (MX1A-L1NN)|The keys of this macropad                                                 |6       |6               |https://www.mouser.com/ProductDetail/CHERRY/MX1A-L1NN?qs=F5EMLAvA7IDlALNAurZTXA%3D%3D|Mouser         |
|0.91" OLED Graphic 128x32   |The display of this macropad; im going to try to make it log recent inputs|1       |3.9             |https://www.displaymodule.com/products/0-91-inch-oled-graphic-display-128x32-with-i2c|DisplayModule  |
|SEEEDUINO XIAO              |The microcontroller of this macropad                                      |1       |5.4             |https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/102010328/11506471|Digikey        |
|1N4148                      |Preventing ghosting in the keyboard matrix                                |6       |0.6             |https://www.digikey.com/en/products/detail/onsemi/1N4148/458603                      |Digikey        |
|EC11E15244G1                |Changing volume                                                           |1       |4.63            |https://www.digikey.com/en/products/detail/alps-alpine/EC11E15244G1/21721550         |Digikey        |
