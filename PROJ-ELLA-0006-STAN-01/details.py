import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "ELLA"
oColor = "0006"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR6"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','disaster01')
newPart.addTag('gitRepo','https://github.com/electrolama/disaster01/')
newPart.addTag('gitName','disaster01/')
newPart.addTag('eagleBoard','disaster01.brd')
newPart.addTag('eagleSchem','disaster01.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
