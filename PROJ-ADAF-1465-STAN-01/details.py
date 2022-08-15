###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRA1465")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "ADAF")
newPart.addTag("oompColor", "1465")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Adafruit ISP SWD and JTAG Breakout PCBs")

newPart.addTag("sources", "All source files from https://github.com/adafruit/Adafruit-ISP-SWD-and-JTAG-Breakout-PCBs (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "http://www.adafruit.com/products/1465")

OOMP.parts.append(newPart)