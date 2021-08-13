import grpc
import ProtoFile1_pb2
import ProtoFile1_pb2_grpc

channel = grpc.insecure_channel('localhost:50050')
stub = ProtoFile1_pb2_grpc.TestingStub(channel)

req = ProtoFile1_pb2.TestReq(user_name = "Shoaib", user_id=12345)
resp = stub.TestService(req)
print(resp)