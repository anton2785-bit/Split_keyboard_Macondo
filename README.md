# Split_keyboard_Macondo
---
## What is this project
* This is a split keyboard. That means that it has 2 separarate parts that are conected to the PC via bluethooth. This allows them to have separate layouts and to have the opportunity to be in different places whiie typing.
---
## Why i made this project
* I wanted to have a small portable keyboard that I can still use for typing and to be compact.
---
## Images 

--- 
* This is an image of the schematic:
<img width="1200" height="745" alt="Schematic" src="https://github.com/user-attachments/assets/1e5c0fc4-e47a-48fe-87a7-9698a969a610" />



* This is the PCB:

<img width="839" height="931" alt="PCB" src="https://github.com/user-attachments/assets/686f4ba6-bd9a-4c47-9dbf-4ec15b9084a9" />


* The 3D model of the PCB:

<img width="1637" height="1225" alt="PCB 3D model" src="https://github.com/user-attachments/assets/61d0b656-377a-4aa6-8b79-5a1351718b7c" />

* This is an image of the PCB with the frame: 
<img width="1494" height="867" alt="Case with PCB" src="https://github.com/user-attachments/assets/86c1ba9b-2f0e-4c7c-8009-a05e1d9c2a25" />


---
## Assembly
* Firt you need to soulder the components on the top and bottom side of the PCB (I preffer to soulder the small ones first then the big ones).
* Then I put the cables for the 4 motors trough the small holes and soulder them to the PCB.
* After that I put the motor into their motor mounts.
* Then you put the top cap on.
* And last you strap the battery with zipties to the body. 
---
## BOM
| Name | Purpose | Quantity | Total Cost (USD) | Distributor |
|------|---------|----------|-----------------|-------------|
| [nRF52840](https://www.seeedstudio.com/Seeed-XIAO-BLE-nRF52840-p-5201.html) | Connects to the PC and gets the signals from the switches | 2 | $33.50 | Seeedstudio |
| PCB | A place for all of the components | 1 | $35.00 | JLCPCB |
| [Keycaps](https://www.aliexpress.com/item/1005010777462878.html) | Make it easier to type | 4 | $22.00 | AliExpress |
| [Diodes](https://www.aliexpress.com/item/1005007160563285.html) | Stops the current in one direction | 1 | $2.10 | AliExpress |
| [Switches](https://www.gateron.com/products/gateron-ks-33-low-profile-red-silent-20-mechanical-switches-set?VariantsId=11584) | A switch | 2 | $21.28 | Gateron |
| [Hotswap modules](https://www.gateron.com/products/gateron-low-profile-switch-hot-swap-pcb-socket?VariantsId=10234) | Makes the keys easier to remove | 1 | $8.80 | Gateron |


**Total Estimated Cost: ~$73.77**

---
## Side note 
* I will change the body of the drone. This one if only for demonstration and I think it wont be the strongest and will bend.
* Also the motor mounts are not the best way to secure them and easiest to place after assembly step 3.
* There will be firmware for a phone and the ESP, but I cant make it now due to the lack of materials to test it. I have added one that will be like a blueprint and I will modify it. 
## Credits

* Designed and built by *(Anton/ Anton-2785-bit)
* Inspired by open‑source mechanical keyboard and hackpad communities (https://macondo.hackclub.com/).
