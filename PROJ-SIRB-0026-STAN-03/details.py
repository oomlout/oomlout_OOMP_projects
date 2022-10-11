import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SIRB"
oColor = "0026"
oDesc = "STAN"
oIndex = "03"
hexId = "PRPR26"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','SirNanoV3 SirNano')
newPart.addTag('gitRepo','https://github.com/sirboard/SirNano')
newPart.addTag('gitName','SirNano')
newPart.addTag('kicadBoard','SirNanoV3/SirNanoV3.kicad_pcb')
newPart.addTag('kicadSchem','SirNanoV3/SirNanoV3.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
