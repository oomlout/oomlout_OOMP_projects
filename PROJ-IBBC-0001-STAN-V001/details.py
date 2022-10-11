import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "IBBC"
oColor = "0001"
oDesc = "STAN"
oIndex = "V001"
hexId = "PRPR1"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','ADXL345 Breakout V001')
newPart.addTag('gitRepo','https://github.com/oomlout/IBBC_0001')
newPart.addTag('gitName','IBBC_0001')
newPart.addTag('kicadBoard','IBBC_0001_V001/IBBC_0001.kicad_pcb')
newPart.addTag('kicadSchem','IBBC_0001_V001/IBBC_0001.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
