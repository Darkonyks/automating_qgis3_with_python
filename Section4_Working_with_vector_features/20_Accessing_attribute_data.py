# open QGIS project python_base from /home/darko/Desktop/qgis_scripting_data/
import time
tmStart = time.time()

layers = QgsProject.instance().mapLayersByName("Countries")
if len(layers)>0:
    countries = layers[0]
    if countries.isValid():
        sStr = ""
        request = QgsFeatureRequest()
        request.setFilterExpression("\"POP_EST\">100000")
        for ftr in countries.getFeatures(request):
#            if ftr['POP_EST']>100000:
                if ftr['POP_EST']>100000000:
                    pop_cat = "large"
                elif ftr['POP_EST']<10000000:
                    pop_cat = "small"
                else:
                    pop_cat = "moderate"
                    
                print("{} has a {} population".format(ftr['NAME'], pop_cat))
                QgsMessageLog.logMessage("{} has a {} population".format(ftr['NAME'], pop_cat))
        print(sStr)
    else:
        print("Countries is not a valid layer")
else:
    print("Countries not found")

tmEnd = time.time()
print("Run time = {0:.3f} seconds".format(tmEnd-tmStart))