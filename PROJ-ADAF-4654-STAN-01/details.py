###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRA4654")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "ADAF")
newPart.addTag("oompColor", "4654")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Adafruit TPS61023 PCB")

newPart.addTag("sources", "All source files from https://github.com/adafruit/Adafruit-TPS61023-PCB (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "http://www.adafruit.com/products/4654")

OOMP.parts.append(newPart)