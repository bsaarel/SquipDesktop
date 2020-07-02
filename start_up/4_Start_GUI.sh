#!/bin/bash
# source virtualenvwrapper.sh
workon 'labrad'
cd /home/sqip/LabRAD/common/abstractdevices/SD_tracker/
python SD_tracker.py
cd /home/sqip/LabRAD/sqip/clients/
python SqipGUI.py
