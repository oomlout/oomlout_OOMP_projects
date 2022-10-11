import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SIRB"
oColor = "0023"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR23"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','ATTinyX14 SirTiny')
newPart.addTag('gitRepo','https://github.com/sirboard/SirTiny')
newPart.addTag('gitName','SirTiny')
newPart.addTag('kicadBoard','ATTinyX14/ATTinyX14.kicad_pcb')
newPart.addTag('kicadSchem','ATTinyX14/ATTinyX14.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
