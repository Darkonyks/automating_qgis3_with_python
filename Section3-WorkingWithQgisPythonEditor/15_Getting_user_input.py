from PyQt5.QtWidgets import QMessageBox
parent = iface.mainWindow()
mc = iface.mapCanvas()

#getText example
sStr, bOK = QInputDialog.getText(parent, "Get Layer", "Please input layer name:", text=mc.currentLayer().sourceName())        
if bOK:
    print("User entered:{}".format(sStr))
else:
    print("User canceled")
#get Int example
iInt, bOK = QInputDialog.getInt(parent, "Title", "Prompt", 7, 1, 10, 1)
if bOK:
    print(iInt)
else:
    print("Canceled")
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    QMessageBox.about(parent, "Title", "User canceled")
    
#get double example
dDbl, bOK = QInputDialog.getDouble(parent, "Title", "Prompt", 7.5, 1, 10, 2)
if bOK:
    QMessageBox.about(parent, "Title", "Prompt " + str(dDbl))
else:
    QMessageBox.about(parent, "Title", "User canceled")
    
# example of dropDown meny from the list
lSpecies = ['RTHA', 'SWHA', 'BTHA', 'HAHA']
sStr, bOK = QInputDialog.getItem(parent, "Species of Hawk", "What species?", lSpecies, editable=False)
if bOK:
    print(sStr)
else:
    print("Canceled")

    


