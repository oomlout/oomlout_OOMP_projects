import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SOPA"
oColor = "0004"
oDesc = "STAN"
oIndex = "01"
hexId = "PRSO4"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','Raspberry Pi Zero Adapter for the Keyboard FeatherWing1')
newPart.addTag('gitRepo','https://github.com/solderparty/keyboard_featherwing_zero_adapter')
newPart.addTag('gitName','keyboard_featherwing_zero_adapter')
newPart.addTag('kicadBoard','kfw_rpi_adapter.kicad_pcb')
newPart.addTag('kicadSchem','kfw_rpi_adapter.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
