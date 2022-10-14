import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "SPAR"
oColor = "17001"
oDesc = "STAN"
oIndex = "01"
hexId = "PRPR17001"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','Qwiic BMP388 Pressure Sensor')
newPart.addTag('gitRepo','https://github.com/sparkfunX/Qwiic_BMP388_Pressure_Sensor')
newPart.addTag('gitName','Qwiic_BMP388_Pressure_Sensor')
newPart.addTag('eagleBoard','Hardware/Qwiic_BMP388_Pressure_Sensor.brd')
newPart.addTag('eagleSchem','Hardware/Qwiic_BMP388_Pressure_Sensor.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
