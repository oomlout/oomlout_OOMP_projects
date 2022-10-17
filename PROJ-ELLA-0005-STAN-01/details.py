import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "ELLA"
oColor = "0005"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR5"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','minik')
newPart.addTag('gitRepo','https://github.com/electrolama/minik')
newPart.addTag('gitName','minik')
newPart.addTag('eagleBoard','hardware/Revision A2/minik-RevA2.brd')
newPart.addTag('eagleSchem','hardware/Revision A2/minik-RevA2.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
