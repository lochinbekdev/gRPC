#!/bin/bash

python client.py --server_ip=127.0.0.1 --server_port=50051 --phone_number=555-0001 &
python client.py --server_ip=127.0.0.1 --server_port=50051 --phone_number=555-0002 &
python client.py --server_ip=127.0.0.1 --server_port=50051 --phone_number=555-0003 &


wait