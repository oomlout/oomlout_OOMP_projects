###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS15805")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "15805")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "SparkFun High Precision Temperature Sensor TMP117 Qwiic")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/SparkFun_High_Precision_Temperature_Sensor_TMP117_Qwiic (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://github.com/sparkfun/15805")

OOMP.parts.append(newPart)