## This is a Grafana Python Mimir API Client for pushing metrics to Grafana Mimir

mimir.proto is copied from Grafana's mimir repo. It is using gogoproto for generating go code. However, if you don't like to use gogoproto. Simply comment all gogo lines, it should work. Steps are: 

Install grpc library, tool, and snappy for python

pip install python-snappy
python3 -m pip install grpcio
python3 -m pip install grpc-tools

Generate python code using following cmd (assume you run it in the dir where mimir.proto is located):
/>python3 -m grpc_tools.protoc -I./ --python_out=. --pyi_out=. --grpc_python_out=. ./mimir_python.proto
