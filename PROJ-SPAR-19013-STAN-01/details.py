###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS19013")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "19013")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "SparkFun Qwiic ToF Imager VL53L5CX-Mini")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/SparkFun_Qwiic_ToF_Imager_VL53L5CX-Mini (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://www.sparkfun.com/products/19013")

OOMP.parts.append(newPart)