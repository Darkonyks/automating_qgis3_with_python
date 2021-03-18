mc =iface.mapCanvas()
lyr = mc.currentLayer()
flds = lyr.fields()
pr = lyr.dataProvider()
#dodavanje novih polja

#fld1 = QgsField("test_name", QVariant.String, len=5)
#fld2 = QgsField("test_count", QVariant.Int)
#pr.addAttributes([fld1, fld2])

#brisanje kolona 
pr.deleteAttributes([flds.indexOf("test_name"), flds.indexOf("test_count")])
lyr.updateFields()
