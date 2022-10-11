import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SIRB"
oColor = "0028"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR28"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','CH340E SirUSB')
newPart.addTag('gitRepo','https://github.com/sirboard/SirUSB')
newPart.addTag('gitName','SirUSB')
newPart.addTag('kicadBoard','CH340E/CH340E.kicad_pcb')
newPart.addTag('kicadSchem','CH340E/CH340E.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
