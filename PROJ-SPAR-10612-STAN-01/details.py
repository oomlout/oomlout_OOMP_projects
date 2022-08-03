###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS10612")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "10612")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Tri-Axis Gyro Breakout-L3G4200D")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/Tri-Axis_Gyro_Breakout-L3G4200D (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://github.com/sparkfun/10612")

OOMP.parts.append(newPart)