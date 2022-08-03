###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS12708")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "12708")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "RTC-Module")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/RTC-Module (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://github.com/sparkfun/12708")

OOMP.parts.append(newPart)