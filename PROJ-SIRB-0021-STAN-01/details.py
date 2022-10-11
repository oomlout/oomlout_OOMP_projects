import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SIRB"
oColor = "0021"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR21"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','ATTiny85 SirTiny')
newPart.addTag('gitRepo','https://github.com/sirboard/SirTiny')
newPart.addTag('gitName','SirTiny')
newPart.addTag('kicadBoard','ATTiny85/ATTiny85.kicad_pcb')
newPart.addTag('kicadSchem','ATTiny85/ATTiny85.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
