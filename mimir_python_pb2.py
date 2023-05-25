# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mimir_python.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12mimir_python.proto\x12\x08\x63ortexpb\"\xdd\x01\n\x0cWriteRequest\x12(\n\ntimeseries\x18\x01 \x03(\x0b\x32\x14.cortexpb.TimeSeries\x12\x31\n\x06Source\x18\x02 \x01(\x0e\x32!.cortexpb.WriteRequest.SourceEnum\x12*\n\x08metadata\x18\x03 \x03(\x0b\x32\x18.cortexpb.MetricMetadata\x12#\n\x1askip_label_name_validation\x18\xe8\x07 \x01(\x08\"\x1f\n\nSourceEnum\x12\x07\n\x03\x41PI\x10\x00\x12\x08\n\x04RULE\x10\x01\"\x0f\n\rWriteResponse\"\xa4\x01\n\nTimeSeries\x12#\n\x06labels\x18\x01 \x03(\x0b\x32\x13.cortexpb.LabelPair\x12!\n\x07samples\x18\x02 \x03(\x0b\x32\x10.cortexpb.Sample\x12%\n\texemplars\x18\x03 \x03(\x0b\x32\x12.cortexpb.Exemplar\x12\'\n\nhistograms\x18\x04 \x03(\x0b\x32\x13.cortexpb.Histogram\"(\n\tLabelPair\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"-\n\x06Sample\x12\x14\n\x0ctimestamp_ms\x18\x02 \x01(\x03\x12\r\n\x05value\x18\x01 \x01(\x01\"\xf6\x01\n\x0eMetricMetadata\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32#.cortexpb.MetricMetadata.MetricType\x12\x1a\n\x12metric_family_name\x18\x02 \x01(\t\x12\x0c\n\x04help\x18\x04 \x01(\t\x12\x0c\n\x04unit\x18\x05 \x01(\t\"y\n\nMetricType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x43OUNTER\x10\x01\x12\t\n\x05GAUGE\x10\x02\x12\r\n\tHISTOGRAM\x10\x03\x12\x12\n\x0eGAUGEHISTOGRAM\x10\x04\x12\x0b\n\x07SUMMARY\x10\x05\x12\x08\n\x04INFO\x10\x06\x12\x0c\n\x08STATESET\x10\x07\"-\n\x06Metric\x12#\n\x06labels\x18\x01 \x03(\x0b\x32\x13.cortexpb.LabelPair\"T\n\x08\x45xemplar\x12#\n\x06labels\x18\x01 \x03(\x0b\x32\x13.cortexpb.LabelPair\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x14\n\x0ctimestamp_ms\x18\x03 \x01(\x03\"\xf5\x03\n\tHistogram\x12\x13\n\tcount_int\x18\x01 \x01(\x04H\x00\x12\x15\n\x0b\x63ount_float\x18\x02 \x01(\x01H\x00\x12\x0b\n\x03sum\x18\x03 \x01(\x01\x12\x0e\n\x06schema\x18\x04 \x01(\x11\x12\x16\n\x0ezero_threshold\x18\x05 \x01(\x01\x12\x18\n\x0ezero_count_int\x18\x06 \x01(\x04H\x01\x12\x1a\n\x10zero_count_float\x18\x07 \x01(\x01H\x01\x12,\n\x0enegative_spans\x18\x08 \x03(\x0b\x32\x14.cortexpb.BucketSpan\x12\x17\n\x0fnegative_deltas\x18\t \x03(\x12\x12\x17\n\x0fnegative_counts\x18\n \x03(\x01\x12,\n\x0epositive_spans\x18\x0b \x03(\x0b\x32\x14.cortexpb.BucketSpan\x12\x17\n\x0fpositive_deltas\x18\x0c \x03(\x12\x12\x17\n\x0fpositive_counts\x18\r \x03(\x01\x12\x31\n\nreset_hint\x18\x0e \x01(\x0e\x32\x1d.cortexpb.Histogram.ResetHint\x12\x11\n\ttimestamp\x18\x0f \x01(\x03\"4\n\tResetHint\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03YES\x10\x01\x12\x06\n\x02NO\x10\x02\x12\t\n\x05GAUGE\x10\x03\x42\x07\n\x05\x63ountB\x0c\n\nzero_count\"\xfa\x02\n\x0e\x46loatHistogram\x12\x1a\n\x12\x63ounter_reset_hint\x18\x0e \x01(\r\x12\x0e\n\x06schema\x18\x04 \x01(\x11\x12\x16\n\x0ezero_threshold\x18\x05 \x01(\x01\x12\x12\n\nzero_count\x18\x07 \x01(\x01\x12\r\n\x05\x63ount\x18\x02 \x01(\x01\x12\x0b\n\x03sum\x18\x03 \x01(\x01\x12,\n\x0epositive_spans\x18\x0b \x03(\x0b\x32\x14.cortexpb.BucketSpan\x12,\n\x0enegative_spans\x18\x08 \x03(\x0b\x32\x14.cortexpb.BucketSpan\x12\x18\n\x10positive_buckets\x18\r \x03(\x01\x12\x18\n\x10negative_buckets\x18\n \x03(\x01J\x04\x08\x01\x10\x02J\x04\x08\x06\x10\x07J\x04\x08\t\x10\nJ\x04\x08\x0c\x10\rJ\x04\x08\x0f\x10\x10R\tcount_intR\x0ezero_count_intR\x0fnegative_deltasR\x0fpositive_deltasR\ttimestamp\",\n\nBucketSpan\x12\x0e\n\x06offset\x18\x01 \x01(\x11\x12\x0e\n\x06length\x18\x02 \x01(\r\"W\n\x12\x46loatHistogramPair\x12\x14\n\x0ctimestamp_ms\x18\x02 \x01(\x03\x12+\n\thistogram\x18\x01 \x01(\x0b\x32\x18.cortexpb.FloatHistogram\"Y\n\x0fSampleHistogram\x12\r\n\x05\x63ount\x18\x01 \x01(\x01\x12\x0b\n\x03sum\x18\x02 \x01(\x01\x12*\n\x07\x62uckets\x18\x03 \x03(\x0b\x32\x19.cortexpb.HistogramBucket\"R\n\x0fHistogramBucket\x12\x12\n\nboundaries\x18\x01 \x01(\x05\x12\r\n\x05lower\x18\x02 \x01(\x01\x12\r\n\x05upper\x18\x03 \x01(\x01\x12\r\n\x05\x63ount\x18\x04 \x01(\x01\"V\n\x13SampleHistogramPair\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12,\n\thistogram\x18\x01 \x01(\x0b\x32\x19.cortexpb.SampleHistogram\"\xe1\x03\n\rQueryResponse\x12.\n\x06status\x18\x01 \x01(\x0e\x32\x1e.cortexpb.QueryResponse.Status\x12\x35\n\nerror_type\x18\x02 \x01(\x0e\x32!.cortexpb.QueryResponse.ErrorType\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12&\n\x06string\x18\x04 \x01(\x0b\x32\x14.cortexpb.StringDataH\x00\x12&\n\x06vector\x18\x05 \x01(\x0b\x32\x14.cortexpb.VectorDataH\x00\x12&\n\x06scalar\x18\x06 \x01(\x0b\x32\x14.cortexpb.ScalarDataH\x00\x12&\n\x06matrix\x18\x07 \x01(\x0b\x32\x14.cortexpb.MatrixDataH\x00\" \n\x06Status\x12\t\n\x05\x45RROR\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\"\x8f\x01\n\tErrorType\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07TIMEOUT\x10\x01\x12\x0c\n\x08\x43\x41NCELED\x10\x02\x12\r\n\tEXECUTION\x10\x03\x12\x0c\n\x08\x42\x41\x44_DATA\x10\x04\x12\x0c\n\x08INTERNAL\x10\x05\x12\x0f\n\x0bUNAVAILABLE\x10\x06\x12\r\n\tNOT_FOUND\x10\x07\x12\x12\n\x0eNOT_ACCEPTABLE\x10\x08\x42\x06\n\x04\x64\x61ta\"1\n\nStringData\x12\r\n\x05value\x18\x01 \x01(\t\x12\x14\n\x0ctimestamp_ms\x18\x02 \x01(\x03\"d\n\nVectorData\x12\'\n\x07samples\x18\x01 \x03(\x0b\x32\x16.cortexpb.VectorSample\x12-\n\nhistograms\x18\x02 \x03(\x0b\x32\x19.cortexpb.VectorHistogram\"C\n\x0cVectorSample\x12\x0e\n\x06metric\x18\x01 \x03(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x14\n\x0ctimestamp_ms\x18\x03 \x01(\x03\"d\n\x0fVectorHistogram\x12\x0e\n\x06metric\x18\x01 \x03(\t\x12+\n\thistogram\x18\x02 \x01(\x0b\x32\x18.cortexpb.FloatHistogram\x12\x14\n\x0ctimestamp_ms\x18\x03 \x01(\x03\"1\n\nScalarData\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x14\n\x0ctimestamp_ms\x18\x02 \x01(\x03\"4\n\nMatrixData\x12&\n\x06series\x18\x01 \x03(\x0b\x32\x16.cortexpb.MatrixSeries\"s\n\x0cMatrixSeries\x12\x0e\n\x06metric\x18\x01 \x03(\t\x12!\n\x07samples\x18\x02 \x03(\x0b\x32\x10.cortexpb.Sample\x12\x30\n\nhistograms\x18\x03 \x03(\x0b\x32\x1c.cortexpb.FloatHistogramPairB\tZ\x07mimirpbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mimir_python_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\007mimirpb'
  _WRITEREQUEST._serialized_start=33
  _WRITEREQUEST._serialized_end=254
  _WRITEREQUEST_SOURCEENUM._serialized_start=223
  _WRITEREQUEST_SOURCEENUM._serialized_end=254
  _WRITERESPONSE._serialized_start=256
  _WRITERESPONSE._serialized_end=271
  _TIMESERIES._serialized_start=274
  _TIMESERIES._serialized_end=438
  _LABELPAIR._serialized_start=440
  _LABELPAIR._serialized_end=480
  _SAMPLE._serialized_start=482
  _SAMPLE._serialized_end=527
  _METRICMETADATA._serialized_start=530
  _METRICMETADATA._serialized_end=776
  _METRICMETADATA_METRICTYPE._serialized_start=655
  _METRICMETADATA_METRICTYPE._serialized_end=776
  _METRIC._serialized_start=778
  _METRIC._serialized_end=823
  _EXEMPLAR._serialized_start=825
  _EXEMPLAR._serialized_end=909
  _HISTOGRAM._serialized_start=912
  _HISTOGRAM._serialized_end=1413
  _HISTOGRAM_RESETHINT._serialized_start=1338
  _HISTOGRAM_RESETHINT._serialized_end=1390
  _FLOATHISTOGRAM._serialized_start=1416
  _FLOATHISTOGRAM._serialized_end=1794
  _BUCKETSPAN._serialized_start=1796
  _BUCKETSPAN._serialized_end=1840
  _FLOATHISTOGRAMPAIR._serialized_start=1842
  _FLOATHISTOGRAMPAIR._serialized_end=1929
  _SAMPLEHISTOGRAM._serialized_start=1931
  _SAMPLEHISTOGRAM._serialized_end=2020
  _HISTOGRAMBUCKET._serialized_start=2022
  _HISTOGRAMBUCKET._serialized_end=2104
  _SAMPLEHISTOGRAMPAIR._serialized_start=2106
  _SAMPLEHISTOGRAMPAIR._serialized_end=2192
  _QUERYRESPONSE._serialized_start=2195
  _QUERYRESPONSE._serialized_end=2676
  _QUERYRESPONSE_STATUS._serialized_start=2490
  _QUERYRESPONSE_STATUS._serialized_end=2522
  _QUERYRESPONSE_ERRORTYPE._serialized_start=2525
  _QUERYRESPONSE_ERRORTYPE._serialized_end=2668
  _STRINGDATA._serialized_start=2678
  _STRINGDATA._serialized_end=2727
  _VECTORDATA._serialized_start=2729
  _VECTORDATA._serialized_end=2829
  _VECTORSAMPLE._serialized_start=2831
  _VECTORSAMPLE._serialized_end=2898
  _VECTORHISTOGRAM._serialized_start=2900
  _VECTORHISTOGRAM._serialized_end=3000
  _SCALARDATA._serialized_start=3002
  _SCALARDATA._serialized_end=3051
  _MATRIXDATA._serialized_start=3053
  _MATRIXDATA._serialized_end=3105
  _MATRIXSERIES._serialized_start=3107
  _MATRIXSERIES._serialized_end=3222
# @@protoc_insertion_point(module_scope)
