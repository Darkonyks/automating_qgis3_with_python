# open QGIS project python_base from /home/darko/Desktop/qgis_scripting_data/
import time
tmStart = time.time()
parent = iface.mainWindow()


layers = QgsProject.instance().mapLayersByName("Countries")
if len(layers) > 0:
    countries = layers[0]
    if countries.isValid():
        lCntry_name = []
        request = QgsFeatureRequest()
        nmClause = QgsFeatureRequest.OrderByClause('NAME')
        orderBy = QgsFeatureRequest.OrderBy([nmClause])
        request.setOrderBy(orderBy)
        for cntry in countries.getFeatures(request):
            lCntry_name.append(cntry['NAME'])

        sCntry, bOk = QInputDialog.getItem(
            parent, "City Names", "Select Country: ", lCntry_name)
        if bOk:
            for cntry in countries.getFeatures():
                if cntry['NAME'] == sCntry:
                    geomCntry = cntry.geometry()

            layers = QgsProject.instance().mapLayersByName("ne_10m_populated_places")
            if len(layers) > 0:
                cities = layers[0]
                if cities.isValid():
                    lIds = []
                    sStr = "" 
                    request = QgsFeatureRequest()
                    popClause = QgsFeatureRequest.OrderByClause(
                        "POP_MAX", ascending=False)
                    orderBy = QgsFeatureRequest.OrderBy([popClause])
                    request.setOrderBy(orderBy)

                    for city in cities.getFeatures(request):
                        if city.geometry().within(geomCntry):
                            lIds.append(city.id())
                            sStr += "{0:15}{1:10} \n".format(
                                city['NAME'], city['POP_MAX'])
                else:
                    print("'Cities' is not valid layer")
            else:
                print("Cities was not found")
        else:
            QMessageBox.warning(parent, "Cities", "User canceled")
    else:
        print("'Countries' is not valid layer")
else:
    print("Countries was not found")

if bOk:
    tmEnd = time.time()
    cities.selectByIds(lIds)
    iface.mapCanvas().zoomToSelected()
    if iface.mapCanvas().scale() < 5000000:
        iface.mapCanvas().zoomScale(5000000)
    sStr = "Run time = {0:.3f} seconds\n\n".format(tmEnd-tmStart) + sStr
    QMessageBox.information(parent, "Cities in {}".format(sCntry), sStr)
