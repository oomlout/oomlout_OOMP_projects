###### OOMP FILE  ######

import OOMP
import OOMPtags

newPart = OOMP.oompItem()

newPart.addTag("hexID", "PRS18011")
newPart.addTag("oompType", "PROJ")
newPart.addTag("oompSize", "SPAR")
newPart.addTag("oompColor", "18011")
newPart.addTag("oompDesc", "STAN")
newPart.addTag("oompIndex", "01")
newPart.addTag("oompName", "SparkFun Analog MEMS Microphone Breakout ICS-40180")

newPart.addTag("sources", "All source files from https://github.com/sparkfun/SparkFun_Analog_MEMS_Microphone_Breakout_ICS-40180 (source licence details in srcLicense.md)")
newPart.addTag("linkBuyPage", "https://github.com/sparkfun/18011")

OOMP.parts.append(newPart)