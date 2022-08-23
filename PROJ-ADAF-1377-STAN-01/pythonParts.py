import OOMP
newPart = OOMP.getPartByID("PROJ-ADAF-1377-STAN-01")

newPart.addTag("oompPart","HEAD-I01-X-PI4-01, JP1, -3.8099999999999996, 0.0, 270")
newPart.addTag("oompPart","HEAD-I01-X-PI4-01, JP2, 3.8099999999999996, 0.0, 90")
newPart.addTag("oompPart","UNMATCHED-UNMATCHED-X-UNMATCHED-01, U$1, 0.0, 0.0, 0")
newPart.addTag("oompPart","UNMATCHED-UNMATCHED-X-UNMATCHED-01, U$2, 0.0, 0.0, M180")
newPart.addTag("rawPart","JP1, HEADER1X4, boogie, (-0.15, 0), R270")
newPart.addTag("rawPart","JP2, HEADER1X4, boogie, (0.15, 0), R90")
newPart.addTag("rawPart","U$1, SO-8, SO-08NMW, boogie, (0, 0), R0")
newPart.addTag("rawPart","U$2, TSSOP-8, TSSOP-8NM, boogie, (0, 0), MR180")
