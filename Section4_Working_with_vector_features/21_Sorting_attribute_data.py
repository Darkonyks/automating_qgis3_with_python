import time
tmStart = time.time()

layers = QgsProject.instance().mapLayersByName("Countries")
if len(layers)>0:
    countries = layers[0]
    sResult = ""
    if countries.isValid():
        request = QgsFeatureRequest()
        request.setFilterExpression("\"POP_EST\" > 100000")
        nameClause = QgsFeatureRequest.OrderByClause('NAME')
        continentClause = QgsFeatureRequest.OrderByClause("CONTINENTS")
        orderby = QgsFeatureRequest.OrderBy([continentClause, nameClause])
        request.setOrderBy(orderby)
        for ftr in countries.getFeatures(request):
            if ftr['POP_EST'] > 100000000:
                pop_cat = "large"
            elif ftr['POP_EST'] < 10000000:
                pop_cat = "small"
            else:
                pop_cat = "moderate"
                
            sResult += "{} is in {} and has a {} population\n".format(ftr['NAME'], ftr['CONTINENT'], pop_cat)
        print (sResult)
    
    else:
        print("Countries is not a valid layer")

else:
    print("Countries not found")
    
tmEnd = time.time()
print ("Run time = {0:.3f} secundes".format(tmStart - tmEnd))
        
                