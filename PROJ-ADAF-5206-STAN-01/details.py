###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRA5206")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "ADAF")
newPart.addTag("oompColor", "5206")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Adafruit 1.69in 280x240 Round Rectangle TFT PCB")

newPart.addTag("sources", "All source files from https://github.com/adafruit/Adafruit-1.69in-280x240-Round-Rectangle-TFT-PCB (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "http://www.adafruit.com/products/5206")

OOMP.parts.append(newPart)