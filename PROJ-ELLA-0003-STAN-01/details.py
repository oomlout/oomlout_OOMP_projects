import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "ELLA"
oColor = "0003"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR3"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','mcore h616 breakout')
newPart.addTag('gitRepo','https://github.com/electrolama/mcore-h616-breakout')
newPart.addTag('gitName','mcore-h616-breakout')
newPart.addTag('eagleBoard','hardware/Revision A1/mcore-h616-breakout-RevA1.brd')
newPart.addTag('eagleSchem','hardware/Revision A1/mcore-h616-breakout-RevA1.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
