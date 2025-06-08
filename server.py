import grpc
from concurrent import futures
import time

import service_pb2
import service_pb2_grpc

class Greeter(service_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        name = request.name
        message = f"Salom, {name}!"
        return service_pb2.HelloReply(message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server ishga tushdi: localhost:50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
    