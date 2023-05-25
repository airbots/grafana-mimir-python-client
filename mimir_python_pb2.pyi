from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BucketSpan(_message.Message):
    __slots__ = ["length", "offset"]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    length: int
    offset: int
    def __init__(self, offset: _Optional[int] = ..., length: _Optional[int] = ...) -> None: ...

class Exemplar(_message.Message):
    __slots__ = ["labels", "timestamp_ms", "value"]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[LabelPair]
    timestamp_ms: int
    value: float
    def __init__(self, labels: _Optional[_Iterable[_Union[LabelPair, _Mapping]]] = ..., value: _Optional[float] = ..., timestamp_ms: _Optional[int] = ...) -> None: ...

class FloatHistogram(_message.Message):
    __slots__ = ["count", "counter_reset_hint", "negative_buckets", "negative_spans", "positive_buckets", "positive_spans", "schema", "sum", "zero_count", "zero_threshold"]
    COUNTER_RESET_HINT_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_SPANS_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_SPANS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    ZERO_COUNT_FIELD_NUMBER: _ClassVar[int]
    ZERO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    count: float
    counter_reset_hint: int
    negative_buckets: _containers.RepeatedScalarFieldContainer[float]
    negative_spans: _containers.RepeatedCompositeFieldContainer[BucketSpan]
    positive_buckets: _containers.RepeatedScalarFieldContainer[float]
    positive_spans: _containers.RepeatedCompositeFieldContainer[BucketSpan]
    schema: int
    sum: float
    zero_count: float
    zero_threshold: float
    def __init__(self, counter_reset_hint: _Optional[int] = ..., schema: _Optional[int] = ..., zero_threshold: _Optional[float] = ..., zero_count: _Optional[float] = ..., count: _Optional[float] = ..., sum: _Optional[float] = ..., positive_spans: _Optional[_Iterable[_Union[BucketSpan, _Mapping]]] = ..., negative_spans: _Optional[_Iterable[_Union[BucketSpan, _Mapping]]] = ..., positive_buckets: _Optional[_Iterable[float]] = ..., negative_buckets: _Optional[_Iterable[float]] = ...) -> None: ...

class FloatHistogramPair(_message.Message):
    __slots__ = ["histogram", "timestamp_ms"]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    histogram: FloatHistogram
    timestamp_ms: int
    def __init__(self, timestamp_ms: _Optional[int] = ..., histogram: _Optional[_Union[FloatHistogram, _Mapping]] = ...) -> None: ...

class Histogram(_message.Message):
    __slots__ = ["count_float", "count_int", "negative_counts", "negative_deltas", "negative_spans", "positive_counts", "positive_deltas", "positive_spans", "reset_hint", "schema", "sum", "timestamp", "zero_count_float", "zero_count_int", "zero_threshold"]
    class ResetHint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    COUNT_FLOAT_FIELD_NUMBER: _ClassVar[int]
    COUNT_INT_FIELD_NUMBER: _ClassVar[int]
    GAUGE: Histogram.ResetHint
    NEGATIVE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_DELTAS_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_SPANS_FIELD_NUMBER: _ClassVar[int]
    NO: Histogram.ResetHint
    POSITIVE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_DELTAS_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_SPANS_FIELD_NUMBER: _ClassVar[int]
    RESET_HINT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: Histogram.ResetHint
    YES: Histogram.ResetHint
    ZERO_COUNT_FLOAT_FIELD_NUMBER: _ClassVar[int]
    ZERO_COUNT_INT_FIELD_NUMBER: _ClassVar[int]
    ZERO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    count_float: float
    count_int: int
    negative_counts: _containers.RepeatedScalarFieldContainer[float]
    negative_deltas: _containers.RepeatedScalarFieldContainer[int]
    negative_spans: _containers.RepeatedCompositeFieldContainer[BucketSpan]
    positive_counts: _containers.RepeatedScalarFieldContainer[float]
    positive_deltas: _containers.RepeatedScalarFieldContainer[int]
    positive_spans: _containers.RepeatedCompositeFieldContainer[BucketSpan]
    reset_hint: Histogram.ResetHint
    schema: int
    sum: float
    timestamp: int
    zero_count_float: float
    zero_count_int: int
    zero_threshold: float
    def __init__(self, count_int: _Optional[int] = ..., count_float: _Optional[float] = ..., sum: _Optional[float] = ..., schema: _Optional[int] = ..., zero_threshold: _Optional[float] = ..., zero_count_int: _Optional[int] = ..., zero_count_float: _Optional[float] = ..., negative_spans: _Optional[_Iterable[_Union[BucketSpan, _Mapping]]] = ..., negative_deltas: _Optional[_Iterable[int]] = ..., negative_counts: _Optional[_Iterable[float]] = ..., positive_spans: _Optional[_Iterable[_Union[BucketSpan, _Mapping]]] = ..., positive_deltas: _Optional[_Iterable[int]] = ..., positive_counts: _Optional[_Iterable[float]] = ..., reset_hint: _Optional[_Union[Histogram.ResetHint, str]] = ..., timestamp: _Optional[int] = ...) -> None: ...

class HistogramBucket(_message.Message):
    __slots__ = ["boundaries", "count", "lower", "upper"]
    BOUNDARIES_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    LOWER_FIELD_NUMBER: _ClassVar[int]
    UPPER_FIELD_NUMBER: _ClassVar[int]
    boundaries: int
    count: float
    lower: float
    upper: float
    def __init__(self, boundaries: _Optional[int] = ..., lower: _Optional[float] = ..., upper: _Optional[float] = ..., count: _Optional[float] = ...) -> None: ...

class LabelPair(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: bytes
    value: bytes
    def __init__(self, name: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class MatrixData(_message.Message):
    __slots__ = ["series"]
    SERIES_FIELD_NUMBER: _ClassVar[int]
    series: _containers.RepeatedCompositeFieldContainer[MatrixSeries]
    def __init__(self, series: _Optional[_Iterable[_Union[MatrixSeries, _Mapping]]] = ...) -> None: ...

class MatrixSeries(_message.Message):
    __slots__ = ["histograms", "metric", "samples"]
    HISTOGRAMS_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    histograms: _containers.RepeatedCompositeFieldContainer[FloatHistogramPair]
    metric: _containers.RepeatedScalarFieldContainer[str]
    samples: _containers.RepeatedCompositeFieldContainer[Sample]
    def __init__(self, metric: _Optional[_Iterable[str]] = ..., samples: _Optional[_Iterable[_Union[Sample, _Mapping]]] = ..., histograms: _Optional[_Iterable[_Union[FloatHistogramPair, _Mapping]]] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ["labels"]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    labels: _containers.RepeatedCompositeFieldContainer[LabelPair]
    def __init__(self, labels: _Optional[_Iterable[_Union[LabelPair, _Mapping]]] = ...) -> None: ...

class MetricMetadata(_message.Message):
    __slots__ = ["help", "metric_family_name", "type", "unit"]
    class MetricType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    COUNTER: MetricMetadata.MetricType
    GAUGE: MetricMetadata.MetricType
    GAUGEHISTOGRAM: MetricMetadata.MetricType
    HELP_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAM: MetricMetadata.MetricType
    INFO: MetricMetadata.MetricType
    METRIC_FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATESET: MetricMetadata.MetricType
    SUMMARY: MetricMetadata.MetricType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: MetricMetadata.MetricType
    help: str
    metric_family_name: str
    type: MetricMetadata.MetricType
    unit: str
    def __init__(self, type: _Optional[_Union[MetricMetadata.MetricType, str]] = ..., metric_family_name: _Optional[str] = ..., help: _Optional[str] = ..., unit: _Optional[str] = ...) -> None: ...

class QueryResponse(_message.Message):
    __slots__ = ["error", "error_type", "matrix", "scalar", "status", "string", "vector"]
    class ErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BAD_DATA: QueryResponse.ErrorType
    CANCELED: QueryResponse.ErrorType
    ERROR: QueryResponse.Status
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION: QueryResponse.ErrorType
    INTERNAL: QueryResponse.ErrorType
    MATRIX_FIELD_NUMBER: _ClassVar[int]
    NONE: QueryResponse.ErrorType
    NOT_ACCEPTABLE: QueryResponse.ErrorType
    NOT_FOUND: QueryResponse.ErrorType
    SCALAR_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STRING_FIELD_NUMBER: _ClassVar[int]
    SUCCESS: QueryResponse.Status
    TIMEOUT: QueryResponse.ErrorType
    UNAVAILABLE: QueryResponse.ErrorType
    VECTOR_FIELD_NUMBER: _ClassVar[int]
    error: str
    error_type: QueryResponse.ErrorType
    matrix: MatrixData
    scalar: ScalarData
    status: QueryResponse.Status
    string: StringData
    vector: VectorData
    def __init__(self, status: _Optional[_Union[QueryResponse.Status, str]] = ..., error_type: _Optional[_Union[QueryResponse.ErrorType, str]] = ..., error: _Optional[str] = ..., string: _Optional[_Union[StringData, _Mapping]] = ..., vector: _Optional[_Union[VectorData, _Mapping]] = ..., scalar: _Optional[_Union[ScalarData, _Mapping]] = ..., matrix: _Optional[_Union[MatrixData, _Mapping]] = ...) -> None: ...

class Sample(_message.Message):
    __slots__ = ["timestamp_ms", "value"]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp_ms: int
    value: float
    def __init__(self, timestamp_ms: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...

class SampleHistogram(_message.Message):
    __slots__ = ["buckets", "count", "sum"]
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SUM_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[HistogramBucket]
    count: float
    sum: float
    def __init__(self, count: _Optional[float] = ..., sum: _Optional[float] = ..., buckets: _Optional[_Iterable[_Union[HistogramBucket, _Mapping]]] = ...) -> None: ...

class SampleHistogramPair(_message.Message):
    __slots__ = ["histogram", "timestamp"]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    histogram: SampleHistogram
    timestamp: int
    def __init__(self, timestamp: _Optional[int] = ..., histogram: _Optional[_Union[SampleHistogram, _Mapping]] = ...) -> None: ...

class ScalarData(_message.Message):
    __slots__ = ["timestamp_ms", "value"]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp_ms: int
    value: float
    def __init__(self, value: _Optional[float] = ..., timestamp_ms: _Optional[int] = ...) -> None: ...

class StringData(_message.Message):
    __slots__ = ["timestamp_ms", "value"]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    timestamp_ms: int
    value: str
    def __init__(self, value: _Optional[str] = ..., timestamp_ms: _Optional[int] = ...) -> None: ...

class TimeSeries(_message.Message):
    __slots__ = ["exemplars", "histograms", "labels", "samples"]
    EXEMPLARS_FIELD_NUMBER: _ClassVar[int]
    HISTOGRAMS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    exemplars: _containers.RepeatedCompositeFieldContainer[Exemplar]
    histograms: _containers.RepeatedCompositeFieldContainer[Histogram]
    labels: _containers.RepeatedCompositeFieldContainer[LabelPair]
    samples: _containers.RepeatedCompositeFieldContainer[Sample]
    def __init__(self, labels: _Optional[_Iterable[_Union[LabelPair, _Mapping]]] = ..., samples: _Optional[_Iterable[_Union[Sample, _Mapping]]] = ..., exemplars: _Optional[_Iterable[_Union[Exemplar, _Mapping]]] = ..., histograms: _Optional[_Iterable[_Union[Histogram, _Mapping]]] = ...) -> None: ...

class VectorData(_message.Message):
    __slots__ = ["histograms", "samples"]
    HISTOGRAMS_FIELD_NUMBER: _ClassVar[int]
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    histograms: _containers.RepeatedCompositeFieldContainer[VectorHistogram]
    samples: _containers.RepeatedCompositeFieldContainer[VectorSample]
    def __init__(self, samples: _Optional[_Iterable[_Union[VectorSample, _Mapping]]] = ..., histograms: _Optional[_Iterable[_Union[VectorHistogram, _Mapping]]] = ...) -> None: ...

class VectorHistogram(_message.Message):
    __slots__ = ["histogram", "metric", "timestamp_ms"]
    HISTOGRAM_FIELD_NUMBER: _ClassVar[int]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    histogram: FloatHistogram
    metric: _containers.RepeatedScalarFieldContainer[str]
    timestamp_ms: int
    def __init__(self, metric: _Optional[_Iterable[str]] = ..., histogram: _Optional[_Union[FloatHistogram, _Mapping]] = ..., timestamp_ms: _Optional[int] = ...) -> None: ...

class VectorSample(_message.Message):
    __slots__ = ["metric", "timestamp_ms", "value"]
    METRIC_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    metric: _containers.RepeatedScalarFieldContainer[str]
    timestamp_ms: int
    value: float
    def __init__(self, metric: _Optional[_Iterable[str]] = ..., value: _Optional[float] = ..., timestamp_ms: _Optional[int] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ["Source", "metadata", "skip_label_name_validation", "timeseries"]
    class SourceEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    API: WriteRequest.SourceEnum
    METADATA_FIELD_NUMBER: _ClassVar[int]
    RULE: WriteRequest.SourceEnum
    SKIP_LABEL_NAME_VALIDATION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    Source: WriteRequest.SourceEnum
    TIMESERIES_FIELD_NUMBER: _ClassVar[int]
    metadata: _containers.RepeatedCompositeFieldContainer[MetricMetadata]
    skip_label_name_validation: bool
    timeseries: _containers.RepeatedCompositeFieldContainer[TimeSeries]
    def __init__(self, timeseries: _Optional[_Iterable[_Union[TimeSeries, _Mapping]]] = ..., Source: _Optional[_Union[WriteRequest.SourceEnum, str]] = ..., metadata: _Optional[_Iterable[_Union[MetricMetadata, _Mapping]]] = ..., skip_label_name_validation: bool = ...) -> None: ...

class WriteResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
