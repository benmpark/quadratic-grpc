# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import quadratic_pb2 as quadratic__pb2


class QuadraticStub(object):
    """The quadratic service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SolveQuadratic = channel.unary_unary(
            '/quadratic.Quadratic/SolveQuadratic',
            request_serializer=quadratic__pb2.Coefficients.SerializeToString,
            response_deserializer=quadratic__pb2.QuadraticSolution.FromString,
        )


class QuadraticServicer(object):
    """The quadratic service definition
    """

    def SolveQuadratic(self, request, context):
        """Sends the three coefficients in a quadratic equation
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QuadraticServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SolveQuadratic': grpc.unary_unary_rpc_method_handler(
            servicer.SolveQuadratic,
            request_deserializer=quadratic__pb2.Coefficients.FromString,
            response_serializer=quadratic__pb2.QuadraticSolution.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'quadratic.Quadratic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

 # This class is part of an EXPERIMENTAL API.


class Quadratic(object):
    """The quadratic service definition
    """

    @staticmethod
    def SolveQuadratic(request,
                       target,
                       options=(),
                       channel_credentials=None,
                       call_credentials=None,
                       insecure=False,
                       compression=None,
                       wait_for_ready=None,
                       timeout=None,
                       metadata=None):
        return grpc.experimental.unary_unary(request, target, '/quadratic.Quadratic/SolveQuadratic',
                                             quadratic__pb2.Coefficients.SerializeToString,
                                             quadratic__pb2.QuadraticSolution.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)