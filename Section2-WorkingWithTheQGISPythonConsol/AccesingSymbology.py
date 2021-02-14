fn = QgsProject.instance().homePath()
print(fn)
fn += "/Data/QGIS_scripting.gpkg"
print(fn)
fn += "|layername=airports"
lyr = iface.addVectorLayer(fn, "Airports", "ogr")
render = lyr.renderer()
print(render)
symbol = render.symbol()
print(symbol)
symbol.setSize(5)
lyr.triggerRepaint()
ltv = iface.layerTreeView()
ltv.refreshLayerSymbology(lyr.id())
symlyr1 = symbol.symbolLayers()[0]
print(symlyr1)
symlyr1.properties
lyr.triggerRepaint()
symnew = QgsMarkerSymbol.createSimple({'name': 'square', 'color': 'blue', 'size':'4', 'outline_color':'red', 'outline_width':'2','angle':'45'})
render.setSymbol(symnew)
lyr.triggerRepaint()
ltv=iface.layerTreeView()
ltv.refreshLayerSymbology(lyr.id())




