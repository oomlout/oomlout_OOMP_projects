###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS20170")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "20170")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "SparkFun Qwiic Pressure Sensor BMP581")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/SparkFun_Qwiic_Pressure_Sensor_BMP581 (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://www.sparkfun.com/products/20170")

OOMP.parts.append(newPart)