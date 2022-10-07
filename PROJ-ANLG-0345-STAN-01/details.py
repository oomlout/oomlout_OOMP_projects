import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "ANLG"
oColor = "0345"
oDesc = "STAN"
oIndex = "01"
hexId = "PRAN1"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','EVAL-ADXL345Z')
#newPart.addTag('gitRepo','')
#newPart.addTag('gitName','zig-a-zig-ah')
#newPart.addTag('eagleBoard','')
#newPart.addTag('eagleSchem','')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
