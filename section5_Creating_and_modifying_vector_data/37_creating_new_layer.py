lyr = QgsVectorLayer("point", "new_layer", "memory")
lyr.setCrs(QgsCoordinateReferenceSystem(26913))
QgsProject.instance().addMapLayer(lyr)

