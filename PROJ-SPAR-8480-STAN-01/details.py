###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS8480")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "8480")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Gainer PSoC Development Board")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/Gainer_PSoC_Development_Board (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://github.com/sparkfun/8480")

OOMP.parts.append(newPart)