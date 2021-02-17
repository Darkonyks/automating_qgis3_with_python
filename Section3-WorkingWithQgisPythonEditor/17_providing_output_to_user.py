parent = iface.mainWindow()

res = QMessageBox.question(parent, "Title of box", "Message")
print("Result: {}".format(res))

while res != QMessageBox.Cancel:
    res = QMessageBox.information(parent, "Title of Box", "Message", QMessageBox.Cancel | QMessageBox.Yes | QMessageBox.No | QMessageBox.Abort | QMessageBox.Apply | QMessageBox.No | QMessageBox.NoToAll)
    print ("Result: {}".format(res))
    
#QGIS push message
iface.messageBar().pushMessage("Woohoo", "It worked!!!", level=Qgis.Success)
iface.messageBar().pushMessage("Just to let you know...", "Still working...", level=Qgis.Info, duration=5)
iface.messageBar().pushMessage("Oops", "Error", level=Qgis.Warning, duration=1)
iface.messageBar().pushMessage("Crap", "Not working", level=Qgis.Critical)

result = QMessageBox.question(parent, "Title of box", "Show your message in the status bar")
if result == QMessageBox.Yes:
    iface.mainWindow().statusBar().showMessage("Your message goes here")
    
QgsMessageLog.logMessage("Not working", "Calculation", level=Qgis.Warning)