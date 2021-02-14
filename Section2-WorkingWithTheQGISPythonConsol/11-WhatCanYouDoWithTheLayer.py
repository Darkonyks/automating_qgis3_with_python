print (type (iface))
#console
#type(iface)

print(isinstance(iface, QgisInterface))
#console
#isinstance(iface, QgisInterface)

mc = iface.mapCanvas()
mc
mc.zoomIn()
mc.zoomOut()
mc.zoomOut()
mc.zoomScale(500000)

lyr = mc.currentLayer()
lyr.isValid()
print(lyr)
#console
#lyr

lyrs = mc.layers()
#console
#lyrs
print(lyrs)
#
#for lyr in lyrs():
#    print(lyr.sourceName)

for lyr in lyrs:
    if isinstance(lyr, QgsVectorLayer):
        print(lyr.sourceName())
    elif isinstance(lyr, QgsRasterLayer):
        print(lyr)
        
for lyr in lyrs:
    if isinstance(lyr, QgsVectorLayer):
        print (lyr.sourceName())
    elif isinstance(lyr, QgsRasterLayer):
        print(lyr)
        
lyrs = QgsProject.instance().mapLayersByName("Railroads")
print(lyrs)
print(type(lyrs))
rr = lyrs[0]
print(type(rr))

lyrs = QgsProject.instance().mapLayersByName("Countries")
print(type(lyrs))

cntry = lyrs[0]
cntry.isValid()
cntry.setOpacity(0.2)
cntry.triggerRepaint()
print (cntry.featureCount())

ftrs = cntry.getFeatures()
print(ftrs)
for ftr in ftrs:
    print(ftr['NAME'])
print(ftr)
ftr["NAME"]
ftr["POP_EST"]

ftrs = cntry.getFeatures()
for ftr in ftrs:
    print(ftr['NAME'], ftr['POP_EST'])
    
ftrs = cntry.selectedFeatures()
for ftr in ftrs:
    print(ftr['NAME'])

