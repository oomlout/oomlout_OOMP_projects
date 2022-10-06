import OOMP 
import OOMPtags 

######  Auto translated oomp file

newPart = OOMP.oompItem()

oType = "PROJ"
oSize = "ELLA"
oColor = "0001"
oDesc = "STAN"
oIndex = "01"
hexId = "PRE1"

newPart.addTag('oompType',oType)
newPart.addTag('oompSize',oSize)
newPart.addTag('oompColor',oColor)
newPart.addTag('oompDesc',oDesc)
newPart.addTag('oompIndex',oIndex)
oompId = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 

newPart.addTag('name','Zig A Zig Ah')
newPart.addTag('gitRepo','https://github.com/electrolama/zig-a-zig-ah')
newPart.addTag('gitName','zig-a-zig-ah')
newPart.addTag('eagleBoard','zzh/Revision A/zzh.brd')
newPart.addTag('eagleSchem','zzh/Revision A/zzh.sch')


######  Common
newPart.addTag('hexID',hexId)

######  Housekeeping
newPart = OOMPtags.addTags(newPart,oompId)
OOMP.parts.append(newPart)
