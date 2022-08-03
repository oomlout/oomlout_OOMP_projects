###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS9322")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "9322")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Photo Interrupter Breakout")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/Photo_Interrupter_Breakout (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://www.sparkfun.com/products/9322")

OOMP.parts.append(newPart)