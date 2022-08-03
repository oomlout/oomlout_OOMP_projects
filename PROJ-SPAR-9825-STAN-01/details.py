###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS9825")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "9825")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Pocket AVR Programmer")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/Pocket_AVR_Programmer (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://www.sparkfun.com/products/9825")

OOMP.parts.append(newPart)