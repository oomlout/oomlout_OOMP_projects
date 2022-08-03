###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS705")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "705")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Transceiver Breakout-nRF24L01 RP-SMA")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/Transceiver_Breakout-nRF24L01_RP-SMA (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://www.sparkfun.com/products/705")

OOMP.parts.append(newPart)