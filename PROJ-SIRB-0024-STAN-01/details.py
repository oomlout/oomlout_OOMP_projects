import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SIRB"
oColor = "0024"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR24"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','ATTinyX16 SirTiny')
newPart.addTag('gitRepo','https://github.com/sirboard/SirTiny')
newPart.addTag('gitName','SirTiny')
newPart.addTag('kicadBoard','ATTinyX16/ATTinyX16.kicad_pcb')
newPart.addTag('kicadSchem','ATTinyX16/ATTinyX16.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
