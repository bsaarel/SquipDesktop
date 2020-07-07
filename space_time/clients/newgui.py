def makeGUI(self):      
        self.dacDict = dict(hc.elec_dict.items() + hc.sma_dict.items())
        self.displays = {k: QtWidgets.QLCDNumber() for k in self.dacDict.keys()}
        layout = QtWidgets.QGridLayout()
        if bool(hc.sma_dict):        
            smaBox = QtWidgets.QGroupBox('SMA Out')
            smaLayout = QtWidgets.QGridLayout()
            smaBox.setLayout(smaLayout)       
        elecBox = QtWidgets.QGroupBox('Electrodes')
        elecLayout = QtWidgets.QGridLayout()
        elecLayout.setColumnStretch(1, 2)
        elecLayout.setColumnStretch(3, 2)
        elecLayout.setColumnStretch(5, 2)
        elecBox.setLayout(elecLayout)
        if bool(hc.sma_dict):
            layout.addWidget(smaBox, 0, 0)
        layout.addWidget(elecBox, 0, 1)
        
        if bool(hc.sma_dict):
            for k in hc.sma_dict:
                self.displays[k].setAutoFillBackground(True)
                smaLayout.addWidget(QtWidgets.QLabel(k), self.dacDict[k].smaOutNumber, 0)
                smaLayout.addWidget(self.displays[k], self.dacDict[k].smaOutNumber, 1)
                s = hc.sma_dict[k].smaOutNumber+1

        elecList = hc.elec_dict.keys()
        elecList.sort()
        for i,e in enumerate(elecList):
            elecLayout.addWidget(QtWidgets.GLabel(e), )
        if bool(hc.centerElectrode):
            elecList.pop(hc.centerElectrode-1)
        for i,e in enumerate(elecList):
            if bool(hc.sma_dict):            
                self.displays[k].setAutoFillBackground(True)
            if int(i) < len(elecList)/2:
                elecLayout.addWidget(QtWidgets.QLabel(e), len(elecList)/2 - int(i), 0)
                elecLayout.addWidget(self.displays[e], len(elecList)/2 - int(i), 1)
            else:
                elecLayout.addWidget(QtWidgets.QLabel(e), len(elecList) - int(i), 4)
                elecLayout.addWidget(self.displays[e], len(elecList) - int(i), 5)
        if bool(hc.centerElectrode):
            elecLayout.addWidget(QtWidgets.QLabel('CNT'), len(elecList)/2 + 1, 2)
            elecLayout.addWidget(self.displays[str(hc.centerElectrode).zfill(2)], len(elecList)/2 + 1, 3)      
          
        if bool(hc.sma_dict):
            spacer = QtWidgets.QSpacerItem(20,40,QtWidgets.QSizePolicy.Minimum,QtWidgets.QSizePolicy.MinimumExpanding)
            smaLayout.addItem(spacer, s, 0,10, 2)  

        self.setLayout(layout)
