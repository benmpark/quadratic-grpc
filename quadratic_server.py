# CSC6304 Week 2 Assignment
# Benjamin Park
# November 8, 2023

"""The Python implementation of the gRPC quadratic solver server."""

from concurrent import futures
import logging

import grpc
import quadratic_pb2
import quadratic_pb2_grpc

import cmath


class QuadraticSolver(quadratic_pb2_grpc.QuadraticServicer):
    def SolveQuadratic(self, request, context):
        solution1 = (-request.b + cmath.sqrt(request.b *
                     request.b - 4 * request.a * request.c)) / (2 * request.a)
        solution2 = (-request.b - cmath.sqrt(request.b *
                     request.b - 4 * request.a * request.c)) / (2 * request.a)
        return quadratic_pb2.QuadraticSolution(
            positive_discriminant_solution_real=solution1.real,
            positive_discriminant_solution_imaginary=solution1.imag,
            negative_discriminant_solution_real=solution2.real,
            negative_discriminant_solution_imaginary=solution2.imag,
        )


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    quadratic_pb2_grpc.add_QuadraticServicer_to_server(
        QuadraticSolver(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, eagerly waiting to ace high-school algebra; listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
