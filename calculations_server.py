import time
import grpc
from concurrent import futures
import calculations_pb2_grpc
import calculations_pb2


class Calculations(calculations_pb2_grpc.CalculationsServiceServicer):

    def Area(self, request, context):
        area = request.width * request.length
        message = '{} area calculated'.format(request.shape_name)
        return calculations_pb2.CalculationsResponse(message=message, calculated_value=area)

    def Volume(self, request, context):
        volume = request.width * request.length * request.height
        message = '{} volume calculated'.format(request.shape_name)
        return calculations_pb2.CalculationsResponse(message=message, calculated_value=volume)


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculations_pb2_grpc.add_CalculationsServiceServicer_to_server(Calculations(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
