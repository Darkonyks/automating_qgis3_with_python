mc = iface.mapCanvas()
lyr = mc.currentLayer()
pr = lyr.dataProvider()

cCaps = pr.capabilities()
sCaps = pr.capabilitiesString()

print(cCaps)
print(sCaps)
print(lyr.name())

if cCaps & QgsVectorDataProvider.RenameAttributes:
    print("Can rename attributes")
else:
    "Cannot rename attributes"
if "Rename Attributes" in sCaps:
    print("Can rename Attributes")
else:
    print("Cannot rename Attributes")