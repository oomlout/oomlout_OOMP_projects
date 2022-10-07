import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "ADAF"
oColor = "1231"
oDesc = "STAN"
oIndex = "0C"
hexId = "PRA1231C"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','ADXL345 - Triple-Axis Accelerometer (+-2g/4g/8g/16g) Rev C')
newPart.addTag('gitRepo','https://github.com/adafruit/Adafruit_ADXL345_PCB')
newPart.addTag('gitName','Adafruit_ADXL345_PCB')
newPart.addTag('eagleBoard','ADXL345 STEMMA QT.brd')
newPart.addTag('eagleSchem','ADXL345 STEMMA QT.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
