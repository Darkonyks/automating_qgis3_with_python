mc = iface.mapCanvas()
lyr = mc.currentLayer()
flds = lyr.fields()
pr = lyr.dataProvider()
lyr.selectByExpression("\"NAME\" = 'United States of America'")
if lyr.selectedFeatureCount()>0:
    fids = lyr.selectedFeatureIds()
    fid = fids[0]
    print(fid)
    pr.deleteFeatures([fid])
    lyr.triggerRepaint()