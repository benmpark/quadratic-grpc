# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: quadratic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fquadratic.proto\x12\tquadratic\"/\n\x0c\x43oefficients\x12\t\n\x01\x61\x18\x01 \x01(\x02\x12\t\n\x01\x62\x18\x02 \x01(\x02\x12\t\n\x01\x63\x18\x03 \x01(\x02\"\xd1\x01\n\x11QuadraticSolution\x12+\n#positive_discriminant_solution_real\x18\x01 \x01(\x01\x12\x30\n(positive_discriminant_solution_imaginary\x18\x02 \x01(\x01\x12+\n#negative_discriminant_solution_real\x18\x03 \x01(\x01\x12\x30\n(negative_discriminant_solution_imaginary\x18\x04 \x01(\x01\x32V\n\tQuadratic\x12I\n\x0eSolveQuadratic\x12\x17.quadratic.Coefficients\x1a\x1c.quadratic.QuadraticSolution\"\x00\x42\x33\n\x19\x63om.bmpark.grpc.quadraticB\x0eQuadraticProtoP\x01\xa2\x02\x03QUAb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'quadratic_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\031com.bmpark.grpc.quadraticB\016QuadraticProtoP\001\242\002\003QUA'
    _globals['_COEFFICIENTS']._serialized_start = 30
    _globals['_COEFFICIENTS']._serialized_end = 77
    _globals['_QUADRATICSOLUTION']._serialized_start = 80
    _globals['_QUADRATICSOLUTION']._serialized_end = 289
    _globals['_QUADRATIC']._serialized_start = 291
    _globals['_QUADRATIC']._serialized_end = 377
# @@protoc_insertion_point(module_scope)
