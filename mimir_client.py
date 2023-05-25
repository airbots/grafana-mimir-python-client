import mimir_python_pb2
import snappy
import time
import requests

def push_to_mimir():
        label_pair = mimir_python_pb2.LabelPair(name=b"__name__", value=b"test_value")
        sample_result = mimir_python_pb2.Sample(
            timestamp_ms=round(time.time() * 1000), value=1
        )
        exemplar_result = mimir_python_pb2.Exemplar(
            labels=[label_pair], value=1, timestamp_ms=round(time.time() * 1000)
        )
        timeseries_result = mimir_python_pb2.TimeSeries(
            labels=[label_pair], samples=[sample_result], exemplars=[exemplar_result]
        )

        metric_data = mimir_python_pb2.MetricMetadata(
            type=3, metric_family_name="metric-sample"
        )

        write_result = mimir_python_pb2.WriteRequest(
            timeseries=[timeseries_result],
            metadata=[metric_data],
            skip_label_name_validation=True,
        )
        write_result_binary = write_result.SerializeToString()
        print(write_result_binary)
        print("bin")
        data_compressed = snappy.compress(write_result_binary)

        response = requests.post(
            url="your_remote_write_endpoint",
            headers={
                "X-Prometheus-Remote-Write-Version": "0.1.0",
                #"X-Mimir-SkipLabelNameValidation": "true",
                "Content-Encoding": "snappy",
                "Content-Type": "application/x-protobuf"
               },
            data=data_compressed,
            auth=('your_username', 'your_password'),
            verify=False,
        )
        print(response.text)
        print(response.status_code)
if __name__ == "__main__":
    push_to_mimir()        
