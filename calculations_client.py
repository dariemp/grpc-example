import grpc
import calculations_pb2_grpc
import calculations_pb2


def Area(shape_name, width, length):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculations_pb2_grpc.CalculationsServiceStub(channel)
        response = stub.Area(calculations_pb2.CalculationsRequest(
            shape_name=shape_name,
            width=width,
            length=length))
        print(response.message, ': ', response.calculated_value)


def Volume(shape_name, width, length, height):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculations_pb2_grpc.CalculationsServiceStub(channel)
        response = stub.Volume(calculations_pb2.CalculationsRequest(
            shape_name=shape_name,
            width=width,
            length=length,
            height=height))
        print(response.message, ': ', response.calculated_value)


def main():
    Area('Rectangle', 3.4, 2)
    Volume('Prism', 3.5, 20, 10)

if __name__ == "__main__":
    main()
