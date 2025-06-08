import grpc
import service_pb2
import service_pb2_grpc

def run():
    print(f"Client ishga tushdi... {grpc}")
    channel = grpc.insecure_channel('localhost:50051')
    stub = service_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(service_pb2.HelloRequest(name='Olam'))
    print("Server javobi:", response.message)

if __name__ == '__main__':
    run()
