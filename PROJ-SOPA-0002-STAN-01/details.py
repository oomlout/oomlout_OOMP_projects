import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SOPA"
oColor = "0002"
oDesc = "STAN"
oIndex = "01"
hexId = "PRSO2"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','BBQ20KBD1')
newPart.addTag('gitRepo','https://github.com/solderparty/bbq20kbd_hw')
newPart.addTag('gitName','bbq20kbd_hw')
newPart.addTag('kicadBoard','bbq20_keyboard.kicad_pcb')
newPart.addTag('kicadSchem','bbq20_keyboard.kicad_sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
