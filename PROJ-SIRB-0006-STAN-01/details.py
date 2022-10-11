import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SIRB"
oColor = "0006"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR6"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','MicroUSB Breakout Board (sirboard)')
newPart.addTag('gitRepo','https://github.com/sirboard/BreakoutBoards')
newPart.addTag('gitName','BreakoutBoards')
newPart.addTag('kicadBoard','MicroUSB/MicroUSB.kicad_pcb')
newPart.addTag('kicadSchem','MicroUSB/MicroUSB.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
