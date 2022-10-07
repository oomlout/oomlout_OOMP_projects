import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "ELLA"
oColor = "0002"
oDesc = "STAN"
oIndex = "0B"
hexId = "PRE2"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','Zoe Rev B')
newPart.addTag('gitRepo','https://github.com/electrolama/zoe')
newPart.addTag('gitName','zoe')
newPart.addTag('eagleBoard','/Revision B/pi-zigbee-poe-rtc.brd')
newPart.addTag('eagleSchem','/Revision B/pi-zigbee-poe-rtc.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
