#! /bin/bash
export LOG_LEVEL=DEBUG
export LOG_FILE_PATH=/tmp/raw-monitor.log
python3 main.py monitor&
