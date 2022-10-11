import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SIRB"
oColor = "0032"
oDesc = "STAN"
oIndex = "02"
hexId = "PRPR32"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','FT231V2 SirUSB')
newPart.addTag('gitRepo','https://github.com/sirboard/SirUSB')
newPart.addTag('gitName','SirUSB')
newPart.addTag('kicadBoard','FT231V2/FT231V2.kicad_pcb')
newPart.addTag('kicadSchem','FT231V2/FT231V2.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
