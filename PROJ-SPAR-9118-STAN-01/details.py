###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS9118")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "9118")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Opto Isolator Breakout")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/Opto_Isolator_Breakout (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://github.com/sparkfun/9118")

OOMP.parts.append(newPart)