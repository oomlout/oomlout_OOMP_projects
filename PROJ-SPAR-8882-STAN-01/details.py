###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS8882")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "8882")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Hall-Effect Current Sensor Breakout-ACS712")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/Hall-Effect_Current_Sensor_Breakout-ACS712 (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://www.sparkfun.com/products/8882")

OOMP.parts.append(newPart)