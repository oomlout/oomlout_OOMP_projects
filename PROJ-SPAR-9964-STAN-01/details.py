###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS9964")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "9964")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Electret Microphone Breakout")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/Electret_Microphone_Breakout (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://www.sparkfun.com/products/9964")

OOMP.parts.append(newPart)