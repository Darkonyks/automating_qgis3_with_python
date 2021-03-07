# open QGIS project python_base from /home/darko/Desktop/qgis_scripting_data/
mc = iface.mapCanvas()
lyr = mc.currentLayer()
flds = lyr.fields()
print(flds.count())
print(flds.names())
fld = flds.field(2)
print(fld.name(), fld.typeName())
print(flds.indexOf("add"))
for fld in flds:
    print(flds.indexOf(fld.name()), fld.name(), fld.type(), fld.typeName(), fld.length(), fld.precision())
    