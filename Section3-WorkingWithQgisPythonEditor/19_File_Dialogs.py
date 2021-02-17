parent = iface.mainWindow()

fn, fnOK = QFileDialog.getOpenFileName(parent, "Shap file to work with", QgsProject.instance().homePath(),"DXF files (*.dxf);;GeoJSON Files (*.geojson)")
if fnOK:
    QMessageBox.information(parent, "Success", "Opening {} ...".format(fn))
    iface.addVectorLayer(fn, "New Layer", "ogr")
else:
    QMessageBox.warning(parent, "Warning", "No File selected")
    
