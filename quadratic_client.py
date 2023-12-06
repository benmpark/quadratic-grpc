# CSC6304 Week 2 Assignment
# Benjamin Park
# November 8, 2023

"""The Python implementation of the gRPC quadratic solver client."""

from __future__ import print_function

import logging

import grpc
import quadratic_pb2
import quadratic_pb2_grpc


def get_user_float(prompt: str) -> float:
    """
    Simple function to get a float from the user.

    Checks to see if the user input is numerical and keeps prompting
    until this condition has been satisfied.

    Parameters
    ----------
    prompt
        text to be displayed to the user when asking for the float

    Returns
    -------
    float
        the accepted user float
    """
    while True:
        try:
            user_response = float(input(prompt))
            break
        except ValueError:
            print("Your input should be numerical; "
                  + "please check your input and try again.")
    return user_response


def get_user_coefficients() -> (int, int, int):
    """
    Helper function to get three coefficients from a quadratic equation.

    Returns
    -------
    a : int
        the coefficient of the x^2 term
    b : int
        the coefficient of the x term
    c : int
        the constant
    """
    print("In your quadratic equation...")
    a = get_user_float("...what is the coefficient of the x^2 term? ")
    b = get_user_float("...what is the coefficient of the x term? ")
    c = get_user_float("...and what is the constant term? ")
    return a, b, c


def print_complex(real: float, imag: float) -> None:
    """
    Function to print a complex number.

    Differentiates between a complex number with both real and imaginary parts
    and one with only an imaginary component. (I.e., with real and imaginary
    parts the formatting would be '1 - i', whereas a purely imaginary number
    would have no space between the negative sign and the i, such as '-i'.)

    Parameters
    ----------
    real
        the real component of the complex number, the 'a' in 'a + bi'
    imag
        the iamginary component of the complex number, the 'b' in 'a + bi'

    Returns
    -------
    None
    """
    output = ""
    if real:
        output += f"{real} "
        output = output + f"+ {imag}i" if imag > 0 \
            else output + f"- {abs(imag)}i"
    else:
        output = "" if imag > 0 else "-"
        output = output + f"{imag}i" if imag > 0 else output + f"{abs(imag)}i"
    return output


def print_solutions(
    real1: float,
    imag1: float,
    real2: float,
    imag2: float
) -> None:
    """
    Helper function to print the quadratic solutions received from the server.

    Parameters
    ----------
    real1
        the real component of the first (positive discriminant) solution
    imag1
        the imaginary component of the first (positive discriminant) solution
    real2
        the real component of the second (negative discriminant) solution
    imag2
        the imaginary component of the second (negative discriminant) solution

    Returns
    -------
    None
    """
    if real1 == real2 and imag1 == 0:
        print("Your quadratic equation has exactly one (real) solution:\n")
        print(f"x = {real1}")
    elif imag1 == 0:
        print("Your quadratic equation has two real solutions:\n")
        print(f"x = {real1} or x = {real2}")
    else:
        print("Your quadratic equation has two complex solutions:\n")
        print(f"x = {print_complex(real1, imag1)} or "
              + f"x = {print_complex(real2, imag2)}")
    print("\nHave a nice day!")


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    a, b, c = get_user_coefficients()
    print("\nWill try to do high school algebra...\n")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = quadratic_pb2_grpc.QuadraticStub(channel)
        coefficients = quadratic_pb2.Coefficients(a=a, b=b, c=c)
        response = stub.SolveQuadratic(coefficients)
        print_solutions(
            response.positive_discriminant_solution_real,
            response.positive_discriminant_solution_imaginary,
            response.negative_discriminant_solution_real,
            response.negative_discriminant_solution_imaginary
        )


if __name__ == "__main__":
    logging.basicConfig()
    run()
