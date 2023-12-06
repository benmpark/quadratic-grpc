from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Coefficients(_message.Message):
    __slots__ = ["a", "b", "c"]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    a: float
    b: float
    c: float
    def __init__(self, a: _Optional[float] = ..., b: _Optional[float] = ..., c: _Optional[float] = ...) -> None: ...

class QuadraticSolution(_message.Message):
    __slots__ = ["positive_discriminant_solution_real", "positive_discriminant_solution_imaginary", "negative_discriminant_solution_real", "negative_discriminant_solution_imaginary"]
    POSITIVE_DISCRIMINANT_SOLUTION_REAL_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_DISCRIMINANT_SOLUTION_IMAGINARY_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_DISCRIMINANT_SOLUTION_REAL_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_DISCRIMINANT_SOLUTION_IMAGINARY_FIELD_NUMBER: _ClassVar[int]
    positive_discriminant_solution_real: float
    positive_discriminant_solution_imaginary: float
    negative_discriminant_solution_real: float
    negative_discriminant_solution_imaginary: float
    def __init__(self, positive_discriminant_solution_real: _Optional[float] = ..., positive_discriminant_solution_imaginary: _Optional[float] = ..., negative_discriminant_solution_real: _Optional[float] = ..., negative_discriminant_solution_imaginary: _Optional[float] = ...) -> None: ...
