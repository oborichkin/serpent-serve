import grpc
import pytest
import socket
from concurrent import futures
from typing import Any

from serpent_serve import SerpentServicer, SerpentClient
from serpent_serve.serpent_pb2_grpc import add_SerpentServicer_to_server
from .models import GenericClass


def unused_tcp_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]


@pytest.fixture
def instance():
    return GenericClass(1, 2, 3)


@pytest.fixture
def server(unused_tcp_port: int, instance) -> grpc.Server:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SerpentServicer_to_server(SerpentServicer(instance), server)
    server.add_insecure_port(f'localhost:{unused_tcp_port}')
    server.start()
    return server, unused_tcp_port


@pytest.fixture
def client(server: tuple[grpc.Server, int]) -> GenericClass:
    server, port = server
    return SerpentClient(grpc.insecure_channel(f'localhost:{port}'))
