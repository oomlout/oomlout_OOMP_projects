import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SPAR"
oColor = "16618"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR16618"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','SparkFun Qwiic Humidity AHT20')
newPart.addTag('gitRepo','https://github.com/sparkfunX/Qwiic_Humidity_AHT20')
newPart.addTag('gitName','Qwiic_Humidity_AHT20')
newPart.addTag('eagleBoard','Hardware/Qwiic EEPROM.brd')
newPart.addTag('eagleSchem','Hardware/Qwiic EEPROM.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
