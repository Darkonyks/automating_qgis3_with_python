mc = iface.mapCanvas()
lyr = mc.currentLayer()
print(lyr.sourceName())
iGeomType = lyr.geometryType()
sGeomType = QgsWkbTypes.geometryDisplayString(iGeomType)
print("Geometry type {} - '{}'".format(iGeomType, sGeomType))
iWkbType = lyr.wkbType()
sWkbType = QgsWkbTypes.displayString(iWkbType)
print ("WKB type {} - '{}'".format(iWkbType, sWkbType))

lName = mc.layers()
for lyr in lName:
    #print(lyr)
    #print only vector layers
    if isinstance(lyr, QgsVectorLayer):
        print("Layer: {}, Geometry type: {}".format(lyr.sourceName(),QgsWkbTypes.displayString(lyr.wkbType())))
