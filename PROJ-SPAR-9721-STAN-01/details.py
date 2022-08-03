###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS9721")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "9721")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Barometric Pressure Sensor Breakout-MPL115A1")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/Barometric_Pressure_Sensor_Breakout-MPL115A1 (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://github.com/sparkfun/9721")

OOMP.parts.append(newPart)