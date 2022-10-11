import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SIRB"
oColor = "0029"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR29"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','CH340G SirUSB')
newPart.addTag('gitRepo','https://github.com/sirboard/SirUSB')
newPart.addTag('gitName','SirUSB')
newPart.addTag('kicadBoard','CH340G/CH340G.kicad_pcb')
newPart.addTag('kicadSchem','CH340G/CH340G.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
