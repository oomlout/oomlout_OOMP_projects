###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRA3028")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "ADAF")
newPart.addTag("oompColor", "3028")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "Adafruit DS3231 Precision RTC FeatherWing PCB")

newPart.addTag("sources", "All source files from https://github.com/adafruit/Adafruit-DS3231-Precision-RTC-FeatherWing-PCB (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "http://www.adafruit.com/products/3028")

OOMP.parts.append(newPart)