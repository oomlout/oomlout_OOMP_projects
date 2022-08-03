###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS13262")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "13262")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "CAN-Bus Shield")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/CAN-Bus_Shield (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://github.com/sparkfun/13262")

OOMP.parts.append(newPart)