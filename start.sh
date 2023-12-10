#!/bin/bash
git clone https://github.com/DARKWEBAMAR/Joanna/tree/v1.0 ok && cd ok && pip3 install -U -r requirements.txt
python3 run.py && python3 -m plugins
