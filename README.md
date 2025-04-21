# 🐍 Serpent-Serve

A lightweight gRPC-based library for remote method invocation and attribute access in Python.

## ✨ Features

- **Remote Method Calls**: Call methods on remote objects as if they were local
- **Attribute Access**: Get/set attributes on remote objects
- **Dynamic Client**: Automatically mirrors remote object's methods and attributes
- **Error Handling**: Propagates exceptions with full stack traces

## 🚀 Installation

```bash
pip install serpent-serve
```

## 🛠️ Usage

### Server Side

```python
from serpent_serve import SerpentServicer

class MyService:

    def __init__(self):
        value = 42

    def greet(self, name):
        return f"Hello, {name}!"

# Create gRPC server and add servicer
server = grpc.server(...)
serpent_servicer = SerpentServicer(MyService())
serpent_pb2_grpc.add_SerpentServicer_to_server(serpent_servicer, server)
```

### Client Side

```python
from serpent_serve import SerpentClient

channel = grpc.insecure_channel('localhost:50051')
client = SerpentClient(channel)

# Call remote methods
print(client.greet("World"))  # "Hello, World!"

# Access remote attributes
print(client.value)  # 42
client.value = 100
```

## 📚 API

### Server
- `SerpentServicer(inner)`: Wraps your object to serve its methods/attributes

### Client
- `SerpentClient(channel)`: Creates a client that mirrors the remote object
  - Automatically discovers all methods/attributes
  - Provides transparent access via Python properties and methods

## ⚠️ Limitations
- Only JSON-serializable objects can be returned/set
- Methods must be callable with JSON-serializable arguments
