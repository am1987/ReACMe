#!/bin/bash
python3 ./kmedoids.py DistanceGraph_input_192Logs_gamma0_100_100.csv 192
python3 ./kmedoids.py DistanceGraph_input_192Logs_gamma0_100_1015.csv 192

python3 ./kmedoids.py DistanceGraph_input_192Logs_gamma1_100_100.csv 192
python3 ./kmedoids.py DistanceGraph_input_192Logs_gamma1_1015_100.csv 192

python3 ./kmedoids.py DistanceGraph_input_192Logs_gamma05_100_100.csv 192
python3 ./kmedoids.py DistanceGraph_input_192Logs_gamma05_100_1015.csv 192
python3 ./kmedoids.py DistanceGraph_input_192Logs_gamma05_1015_100.csv 192
python3 ./kmedoids.py DistanceGraph_input_192Logs_gamma05_1015_1015.csv 192

