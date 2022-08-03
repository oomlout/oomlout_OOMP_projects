###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS13035")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "13035")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Edison OLED Block")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/Edison_OLED_Block (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://github.com/sparkfun/13035")

OOMP.parts.append(newPart)