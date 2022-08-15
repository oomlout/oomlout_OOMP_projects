###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRA2821")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "ADAF")
newPart.addTag("oompColor", "2821")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Adafruit Feather ESP8266 HUZZAH PCB")

newPart.addTag("sources", "All source files from https://github.com/adafruit/Adafruit-Feather-ESP8266-HUZZAH-PCB (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "http://www.adafruit.com/products/2821")

OOMP.parts.append(newPart)