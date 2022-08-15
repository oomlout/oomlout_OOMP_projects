###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRA3133")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "ADAF")
newPart.addTag("oompColor", "3133")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Adafruit Ultimate GPS FeatherWing PCB")

newPart.addTag("sources", "All source files from https://github.com/adafruit/Adafruit-Ultimate-GPS-FeatherWing-PCB (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "http://www.adafruit.com/products/3133")

OOMP.parts.append(newPart)