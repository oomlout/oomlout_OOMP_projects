import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "ELLA"
oColor = "0008"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR8"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','pic16-usb-module')
newPart.addTag('gitRepo','https://github.com/electrolama/pic16-usb-module/')
newPart.addTag('gitName','pic16-usb-module/')
newPart.addTag('eagleBoard','pum.brd')
newPart.addTag('eagleSchem','pum.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
