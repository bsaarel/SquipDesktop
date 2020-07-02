#!/bin/bash
# source virtualenvwrapper.sh
workon labrad

python /home/sqip/LabRAD/common/abstractdevices/script_scanner/script_scanner.py &

python /home/sqip/LabRAD/common/clients/script_scanner_gui/script_scanner_gui.py &

python /home/sqip/LabRAD/common/clients/pygrapherlive/grapher.py &




