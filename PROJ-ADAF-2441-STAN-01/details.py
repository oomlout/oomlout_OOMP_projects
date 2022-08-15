###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRA2441")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "ADAF")
newPart.addTag("oompColor", "2441")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Adafruit PiTFT 3.5 Plus PCB")

newPart.addTag("sources", "All source files from https://github.com/adafruit/Adafruit-PiTFT-3.5-Plus-PCB (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "http://www.adafruit.com/products/2441")

OOMP.parts.append(newPart)