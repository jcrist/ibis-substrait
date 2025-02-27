"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
from ... import substrait
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class FunctionSignature(google.protobuf.message.Message):
    """List of function signatures available."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class FinalArgVariadic(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _ParameterConsistency:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _ParameterConsistencyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FunctionSignature.FinalArgVariadic._ParameterConsistency.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            PARAMETER_CONSISTENCY_UNSPECIFIED: FunctionSignature.FinalArgVariadic._ParameterConsistency.ValueType
            PARAMETER_CONSISTENCY_CONSISTENT: FunctionSignature.FinalArgVariadic._ParameterConsistency.ValueType
            'All argument must be the same concrete type.'
            PARAMETER_CONSISTENCY_INCONSISTENT: FunctionSignature.FinalArgVariadic._ParameterConsistency.ValueType
            'Each argument can be any possible concrete type afforded by the bounds\n            of any parameter defined in the arguments specification.\n            '

        class ParameterConsistency(_ParameterConsistency, metaclass=_ParameterConsistencyEnumTypeWrapper):
            pass
        PARAMETER_CONSISTENCY_UNSPECIFIED: FunctionSignature.FinalArgVariadic.ParameterConsistency.ValueType
        PARAMETER_CONSISTENCY_CONSISTENT: FunctionSignature.FinalArgVariadic.ParameterConsistency.ValueType
        'All argument must be the same concrete type.'
        PARAMETER_CONSISTENCY_INCONSISTENT: FunctionSignature.FinalArgVariadic.ParameterConsistency.ValueType
        'Each argument can be any possible concrete type afforded by the bounds\n        of any parameter defined in the arguments specification.\n        '
        MIN_ARGS_FIELD_NUMBER: builtins.int
        MAX_ARGS_FIELD_NUMBER: builtins.int
        CONSISTENCY_FIELD_NUMBER: builtins.int
        min_args: builtins.int
        'the minimum number of arguments allowed for the list of final arguments\n        (inclusive).\n        '
        max_args: builtins.int
        'the maximum number of arguments allowed for the list of final arguments\n        (exclusive)\n        '
        consistency: global___FunctionSignature.FinalArgVariadic.ParameterConsistency.ValueType
        'the type of parameterized type consistency'

        def __init__(self, *, min_args: builtins.int=..., max_args: builtins.int=..., consistency: global___FunctionSignature.FinalArgVariadic.ParameterConsistency.ValueType=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['consistency', b'consistency', 'max_args', b'max_args', 'min_args', b'min_args']) -> None:
            ...

    class FinalArgNormal(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        def __init__(self) -> None:
            ...

    class Scalar(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ARGUMENTS_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        DESCRIPTION_FIELD_NUMBER: builtins.int
        DETERMINISTIC_FIELD_NUMBER: builtins.int
        SESSION_DEPENDENT_FIELD_NUMBER: builtins.int
        OUTPUT_TYPE_FIELD_NUMBER: builtins.int
        VARIADIC_FIELD_NUMBER: builtins.int
        NORMAL_FIELD_NUMBER: builtins.int
        IMPLEMENTATIONS_FIELD_NUMBER: builtins.int

        @property
        def arguments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FunctionSignature.Argument]:
            ...

        @property
        def name(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            ...

        @property
        def description(self) -> global___FunctionSignature.Description:
            ...
        deterministic: builtins.bool
        session_dependent: builtins.bool

        @property
        def output_type(self) -> substrait.ibis.type_expressions_pb2.DerivationExpression:
            ...

        @property
        def variadic(self) -> global___FunctionSignature.FinalArgVariadic:
            ...

        @property
        def normal(self) -> global___FunctionSignature.FinalArgNormal:
            ...

        @property
        def implementations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FunctionSignature.Implementation]:
            ...

        def __init__(self, *, arguments: typing.Optional[typing.Iterable[global___FunctionSignature.Argument]]=..., name: typing.Optional[typing.Iterable[typing.Text]]=..., description: typing.Optional[global___FunctionSignature.Description]=..., deterministic: builtins.bool=..., session_dependent: builtins.bool=..., output_type: typing.Optional[substrait.ibis.type_expressions_pb2.DerivationExpression]=..., variadic: typing.Optional[global___FunctionSignature.FinalArgVariadic]=..., normal: typing.Optional[global___FunctionSignature.FinalArgNormal]=..., implementations: typing.Optional[typing.Iterable[global___FunctionSignature.Implementation]]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['description', b'description', 'final_variable_behavior', b'final_variable_behavior', 'normal', b'normal', 'output_type', b'output_type', 'variadic', b'variadic']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['arguments', b'arguments', 'description', b'description', 'deterministic', b'deterministic', 'final_variable_behavior', b'final_variable_behavior', 'implementations', b'implementations', 'name', b'name', 'normal', b'normal', 'output_type', b'output_type', 'session_dependent', b'session_dependent', 'variadic', b'variadic']) -> None:
            ...

        def WhichOneof(self, oneof_group: typing_extensions.Literal['final_variable_behavior', b'final_variable_behavior']) -> typing.Optional[typing_extensions.Literal['variadic', 'normal']]:
            ...

    class Aggregate(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        ARGUMENTS_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        DESCRIPTION_FIELD_NUMBER: builtins.int
        DETERMINISTIC_FIELD_NUMBER: builtins.int
        SESSION_DEPENDENT_FIELD_NUMBER: builtins.int
        OUTPUT_TYPE_FIELD_NUMBER: builtins.int
        VARIADIC_FIELD_NUMBER: builtins.int
        NORMAL_FIELD_NUMBER: builtins.int
        ORDERED_FIELD_NUMBER: builtins.int
        MAX_SET_FIELD_NUMBER: builtins.int
        INTERMEDIATE_TYPE_FIELD_NUMBER: builtins.int
        IMPLEMENTATIONS_FIELD_NUMBER: builtins.int

        @property
        def arguments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FunctionSignature.Argument]:
            ...
        name: typing.Text

        @property
        def description(self) -> global___FunctionSignature.Description:
            ...
        deterministic: builtins.bool
        session_dependent: builtins.bool

        @property
        def output_type(self) -> substrait.ibis.type_expressions_pb2.DerivationExpression:
            ...

        @property
        def variadic(self) -> global___FunctionSignature.FinalArgVariadic:
            ...

        @property
        def normal(self) -> global___FunctionSignature.FinalArgNormal:
            ...
        ordered: builtins.bool
        max_set: builtins.int

        @property
        def intermediate_type(self) -> substrait.ibis.type_pb2.Type:
            ...

        @property
        def implementations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FunctionSignature.Implementation]:
            ...

        def __init__(self, *, arguments: typing.Optional[typing.Iterable[global___FunctionSignature.Argument]]=..., name: typing.Text=..., description: typing.Optional[global___FunctionSignature.Description]=..., deterministic: builtins.bool=..., session_dependent: builtins.bool=..., output_type: typing.Optional[substrait.ibis.type_expressions_pb2.DerivationExpression]=..., variadic: typing.Optional[global___FunctionSignature.FinalArgVariadic]=..., normal: typing.Optional[global___FunctionSignature.FinalArgNormal]=..., ordered: builtins.bool=..., max_set: builtins.int=..., intermediate_type: typing.Optional[substrait.ibis.type_pb2.Type]=..., implementations: typing.Optional[typing.Iterable[global___FunctionSignature.Implementation]]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['description', b'description', 'final_variable_behavior', b'final_variable_behavior', 'intermediate_type', b'intermediate_type', 'normal', b'normal', 'output_type', b'output_type', 'variadic', b'variadic']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['arguments', b'arguments', 'description', b'description', 'deterministic', b'deterministic', 'final_variable_behavior', b'final_variable_behavior', 'implementations', b'implementations', 'intermediate_type', b'intermediate_type', 'max_set', b'max_set', 'name', b'name', 'normal', b'normal', 'ordered', b'ordered', 'output_type', b'output_type', 'session_dependent', b'session_dependent', 'variadic', b'variadic']) -> None:
            ...

        def WhichOneof(self, oneof_group: typing_extensions.Literal['final_variable_behavior', b'final_variable_behavior']) -> typing.Optional[typing_extensions.Literal['variadic', 'normal']]:
            ...

    class Window(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _WindowType:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _WindowTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FunctionSignature.Window._WindowType.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            WINDOW_TYPE_UNSPECIFIED: FunctionSignature.Window._WindowType.ValueType
            WINDOW_TYPE_STREAMING: FunctionSignature.Window._WindowType.ValueType
            WINDOW_TYPE_PARTITION: FunctionSignature.Window._WindowType.ValueType

        class WindowType(_WindowType, metaclass=_WindowTypeEnumTypeWrapper):
            pass
        WINDOW_TYPE_UNSPECIFIED: FunctionSignature.Window.WindowType.ValueType
        WINDOW_TYPE_STREAMING: FunctionSignature.Window.WindowType.ValueType
        WINDOW_TYPE_PARTITION: FunctionSignature.Window.WindowType.ValueType
        ARGUMENTS_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        DESCRIPTION_FIELD_NUMBER: builtins.int
        DETERMINISTIC_FIELD_NUMBER: builtins.int
        SESSION_DEPENDENT_FIELD_NUMBER: builtins.int
        INTERMEDIATE_TYPE_FIELD_NUMBER: builtins.int
        OUTPUT_TYPE_FIELD_NUMBER: builtins.int
        VARIADIC_FIELD_NUMBER: builtins.int
        NORMAL_FIELD_NUMBER: builtins.int
        ORDERED_FIELD_NUMBER: builtins.int
        MAX_SET_FIELD_NUMBER: builtins.int
        WINDOW_TYPE_FIELD_NUMBER: builtins.int
        IMPLEMENTATIONS_FIELD_NUMBER: builtins.int

        @property
        def arguments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FunctionSignature.Argument]:
            ...

        @property
        def name(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
            ...

        @property
        def description(self) -> global___FunctionSignature.Description:
            ...
        deterministic: builtins.bool
        session_dependent: builtins.bool

        @property
        def intermediate_type(self) -> substrait.ibis.type_expressions_pb2.DerivationExpression:
            ...

        @property
        def output_type(self) -> substrait.ibis.type_expressions_pb2.DerivationExpression:
            ...

        @property
        def variadic(self) -> global___FunctionSignature.FinalArgVariadic:
            ...

        @property
        def normal(self) -> global___FunctionSignature.FinalArgNormal:
            ...
        ordered: builtins.bool
        max_set: builtins.int
        window_type: global___FunctionSignature.Window.WindowType.ValueType

        @property
        def implementations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FunctionSignature.Implementation]:
            ...

        def __init__(self, *, arguments: typing.Optional[typing.Iterable[global___FunctionSignature.Argument]]=..., name: typing.Optional[typing.Iterable[typing.Text]]=..., description: typing.Optional[global___FunctionSignature.Description]=..., deterministic: builtins.bool=..., session_dependent: builtins.bool=..., intermediate_type: typing.Optional[substrait.ibis.type_expressions_pb2.DerivationExpression]=..., output_type: typing.Optional[substrait.ibis.type_expressions_pb2.DerivationExpression]=..., variadic: typing.Optional[global___FunctionSignature.FinalArgVariadic]=..., normal: typing.Optional[global___FunctionSignature.FinalArgNormal]=..., ordered: builtins.bool=..., max_set: builtins.int=..., window_type: global___FunctionSignature.Window.WindowType.ValueType=..., implementations: typing.Optional[typing.Iterable[global___FunctionSignature.Implementation]]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['description', b'description', 'final_variable_behavior', b'final_variable_behavior', 'intermediate_type', b'intermediate_type', 'normal', b'normal', 'output_type', b'output_type', 'variadic', b'variadic']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['arguments', b'arguments', 'description', b'description', 'deterministic', b'deterministic', 'final_variable_behavior', b'final_variable_behavior', 'implementations', b'implementations', 'intermediate_type', b'intermediate_type', 'max_set', b'max_set', 'name', b'name', 'normal', b'normal', 'ordered', b'ordered', 'output_type', b'output_type', 'session_dependent', b'session_dependent', 'variadic', b'variadic', 'window_type', b'window_type']) -> None:
            ...

        def WhichOneof(self, oneof_group: typing_extensions.Literal['final_variable_behavior', b'final_variable_behavior']) -> typing.Optional[typing_extensions.Literal['variadic', 'normal']]:
            ...

    class Description(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor
        LANGUAGE_FIELD_NUMBER: builtins.int
        BODY_FIELD_NUMBER: builtins.int
        language: typing.Text
        body: typing.Text

        def __init__(self, *, language: typing.Text=..., body: typing.Text=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['body', b'body', 'language', b'language']) -> None:
            ...

    class Implementation(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _Type:
            ValueType = typing.NewType('ValueType', builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FunctionSignature.Implementation._Type.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            TYPE_UNSPECIFIED: FunctionSignature.Implementation._Type.ValueType
            TYPE_WEB_ASSEMBLY: FunctionSignature.Implementation._Type.ValueType
            TYPE_TRINO_JAR: FunctionSignature.Implementation._Type.ValueType

        class Type(_Type, metaclass=_TypeEnumTypeWrapper):
            pass
        TYPE_UNSPECIFIED: FunctionSignature.Implementation.Type.ValueType
        TYPE_WEB_ASSEMBLY: FunctionSignature.Implementation.Type.ValueType
        TYPE_TRINO_JAR: FunctionSignature.Implementation.Type.ValueType
        TYPE_FIELD_NUMBER: builtins.int
        URI_FIELD_NUMBER: builtins.int
        type: global___FunctionSignature.Implementation.Type.ValueType
        uri: typing.Text

        def __init__(self, *, type: global___FunctionSignature.Implementation.Type.ValueType=..., uri: typing.Text=...) -> None:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['type', b'type', 'uri', b'uri']) -> None:
            ...

    class Argument(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class ValueArgument(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            TYPE_FIELD_NUMBER: builtins.int
            CONSTANT_FIELD_NUMBER: builtins.int

            @property
            def type(self) -> substrait.ibis.parameterized_types_pb2.ParameterizedType:
                ...
            constant: builtins.bool

            def __init__(self, *, type: typing.Optional[substrait.ibis.parameterized_types_pb2.ParameterizedType]=..., constant: builtins.bool=...) -> None:
                ...

            def HasField(self, field_name: typing_extensions.Literal['type', b'type']) -> builtins.bool:
                ...

            def ClearField(self, field_name: typing_extensions.Literal['constant', b'constant', 'type', b'type']) -> None:
                ...

        class TypeArgument(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            TYPE_FIELD_NUMBER: builtins.int

            @property
            def type(self) -> substrait.ibis.parameterized_types_pb2.ParameterizedType:
                ...

            def __init__(self, *, type: typing.Optional[substrait.ibis.parameterized_types_pb2.ParameterizedType]=...) -> None:
                ...

            def HasField(self, field_name: typing_extensions.Literal['type', b'type']) -> builtins.bool:
                ...

            def ClearField(self, field_name: typing_extensions.Literal['type', b'type']) -> None:
                ...

        class EnumArgument(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor
            OPTIONS_FIELD_NUMBER: builtins.int
            OPTIONAL_FIELD_NUMBER: builtins.int

            @property
            def options(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
                ...
            optional: builtins.bool

            def __init__(self, *, options: typing.Optional[typing.Iterable[typing.Text]]=..., optional: builtins.bool=...) -> None:
                ...

            def ClearField(self, field_name: typing_extensions.Literal['optional', b'optional', 'options', b'options']) -> None:
                ...
        NAME_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        TYPE_FIELD_NUMBER: builtins.int
        ENUM_FIELD_NUMBER: builtins.int
        name: typing.Text

        @property
        def value(self) -> global___FunctionSignature.Argument.ValueArgument:
            ...

        @property
        def type(self) -> global___FunctionSignature.Argument.TypeArgument:
            ...

        @property
        def enum(self) -> global___FunctionSignature.Argument.EnumArgument:
            ...

        def __init__(self, *, name: typing.Text=..., value: typing.Optional[global___FunctionSignature.Argument.ValueArgument]=..., type: typing.Optional[global___FunctionSignature.Argument.TypeArgument]=..., enum: typing.Optional[global___FunctionSignature.Argument.EnumArgument]=...) -> None:
            ...

        def HasField(self, field_name: typing_extensions.Literal['argument_kind', b'argument_kind', 'enum', b'enum', 'type', b'type', 'value', b'value']) -> builtins.bool:
            ...

        def ClearField(self, field_name: typing_extensions.Literal['argument_kind', b'argument_kind', 'enum', b'enum', 'name', b'name', 'type', b'type', 'value', b'value']) -> None:
            ...

        def WhichOneof(self, oneof_group: typing_extensions.Literal['argument_kind', b'argument_kind']) -> typing.Optional[typing_extensions.Literal['value', 'type', 'enum']]:
            ...

    def __init__(self) -> None:
        ...
global___FunctionSignature = FunctionSignature