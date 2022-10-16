import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "DANP"
oColor = "0002"
oDesc = "STAN"
oIndex = "V4E"
hexId = "PRPR2"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','Bus Pirate v4e')
newPart.addTag('gitRepo','https://github.com/DangerousPrototypes/Bus_Pirate')
newPart.addTag('gitName','Bus_Pirate')
newPart.addTag('eagleBoard','hardware/v4/BusPirate-v4e.brd')
newPart.addTag('eagleSchem','hardware/v4/BusPirate-v4e.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
