import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "DANP"
oColor = "0001"
oDesc = "STAN"
oIndex = "1A"
hexId = "PRPR1"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','Bus Pirate Ultra 1A')
newPart.addTag('gitRepo','https://github.com/DangerousPrototypes/BusPirateUltraHardware')
newPart.addTag('gitName','BusPirateUltraHardware')
newPart.addTag('eagleBoard','BPUv1a/BusPirate-ultra.v1.0a.brd')
newPart.addTag('eagleSchem','BPUv1a/BusPirate-ultra.v1.0a.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
