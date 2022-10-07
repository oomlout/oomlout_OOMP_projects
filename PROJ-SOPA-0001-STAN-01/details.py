import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SOPA"
oColor = "0001"
oDesc = "STAN"
oIndex = "01"
hexId = "PRSO1"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','RP2040 Stamp1')
newPart.addTag('gitRepo','https://github.com/solderparty/rp2040_stamp_hw')
newPart.addTag('gitName','rp2040_stamp_hw')
newPart.addTag('kicadBoard','rp2040_stamp.kicad_pcb')
newPart.addTag('kicadSchem','rp2040_stamp.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
