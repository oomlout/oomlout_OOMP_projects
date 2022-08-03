###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS17506")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "17506")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "SparkFun LoRa Thing Plus expLoRaBLE")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/SparkFun_LoRa_Thing_Plus_expLoRaBLE (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://www.sparkfun.com/products/17506")

OOMP.parts.append(newPart)