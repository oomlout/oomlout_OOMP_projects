###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS12082")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "12082")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "AD5330 Breakout")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/AD5330_Breakout (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://www.sparkfun.com/products/12082")

OOMP.parts.append(newPart)