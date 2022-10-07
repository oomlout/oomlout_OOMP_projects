import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "ADAF"
oColor = "1231"
oDesc = "STAN"
oIndex = "0B"
hexId = "PRA1231B"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','ADXL345 - Triple-Axis Accelerometer (+-2g/4g/8g/16g) Rev B')
newPart.addTag('gitRepo','https://github.com/adafruit/Adafruit_ADXL345_PCB')
newPart.addTag('gitName','Adafruit_ADXL345_PCB')
newPart.addTag('eagleBoard','Adafruit ADXL345 Triple-Axis Accelerometer.brd')
newPart.addTag('eagleSchem','Adafruit ADXL345 Triple-Axis Accelerometer.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
