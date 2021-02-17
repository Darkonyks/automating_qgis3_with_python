parent = iface.mainWindow()

fns, fnOK = QFileDialog.getOpenFileNames(parent, "Shapefiles to open", QgsProject.instance().homePath(), "SHP files (*.shp);;GeoJSON files (*.geojson)")
if fnOK:
    QMessageBox.information(parent, "Success", "Opening  {} ...".format(fns))
    for fn in fns:
        iface.addVectorLayer(fn, "", "ogr")
else:
    QMessageBox.warning(parent, "Warning", "No files selected")