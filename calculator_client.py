from __future__ import print_function
import grpc
import calculator_pb2
import calculator_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        a = int(input("Enter first value  :"))
        b = int(input("Enter second value :"))
        response = stub.add(calculator_pb2.addRequest(a=a, b=b))

    print("Addition of first value & second value :" + response.result)


if __name__ == '__main__':
    run()