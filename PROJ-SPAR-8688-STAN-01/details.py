###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS8688")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "8688")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Ambient Light Sensor Breakout-TEMT6000")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/Ambient_Light_Sensor_Breakout-TEMT6000 (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://www.sparkfun.com/products/8688")

OOMP.parts.append(newPart)