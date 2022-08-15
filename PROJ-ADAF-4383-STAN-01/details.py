###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRA4383")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "ADAF")
newPart.addTag("oompColor", "4383")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Adafruit 1.14 inch 240x135 TFT PCB")

newPart.addTag("sources", "All source files from https://github.com/adafruit/Adafruit-1.14-inch-240x135-TFT-PCB (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "http://www.adafruit.com/products/4383")

OOMP.parts.append(newPart)