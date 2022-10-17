import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "ELLA"
oColor = "0007"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR7"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','nandcat')
newPart.addTag('gitRepo','https://github.com/electrolama/nandcat')
newPart.addTag('gitName','nandcat')
newPart.addTag('eagleBoard','Revision A/nand-cat.brd')
newPart.addTag('eagleSchem','Revision A/nand-cat.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
