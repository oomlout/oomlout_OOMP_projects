import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SIRB"
oColor = "0003"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR3"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','ESP-12F Breakout Board (sirboard)')
newPart.addTag('gitRepo','https://github.com/sirboard/BreakoutBoards')
newPart.addTag('gitName','BreakoutBoards')
newPart.addTag('kicadBoard','ESP-12F/ESP-12F.kicad_pcb')
newPart.addTag('kicadSchem','ESP-12F/ESP-12F.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
