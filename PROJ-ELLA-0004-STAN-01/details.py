import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "ELLA"
oColor = "0004"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR4"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','riscystick')
newPart.addTag('gitRepo','https://github.com/electrolama/riscystick')
newPart.addTag('gitName','riscystick')
newPart.addTag('eagleBoard','hardware/Revision A1/riscystick-RevA1.brd')
newPart.addTag('eagleSchem','hardware/Revision A1/riscystick-RevA1.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
