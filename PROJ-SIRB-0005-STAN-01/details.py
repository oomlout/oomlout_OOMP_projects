import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SIRB"
oColor = "0005"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR5"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','MicroSD_DualVoltage Breakout Board (sirboard)')
newPart.addTag('gitRepo','https://github.com/sirboard/BreakoutBoards')
newPart.addTag('gitName','BreakoutBoards')
newPart.addTag('kicadBoard','MicroSD_DualVoltage/MicroSD_DualVoltage.kicad_pcb')
newPart.addTag('kicadSchem','MicroSD_DualVoltage/MicroSD_DualVoltage.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
