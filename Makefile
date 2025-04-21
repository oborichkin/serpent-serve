DEV_MARKER=.dev-venv-initialized

.PHONY: proto test

proto: serpent_serve/serpent.proto
	$(VENV)/python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. --pyi_out=. serpent_serve/serpent.proto

dev-venv: $(DEV_MARKER)

$(DEV_MARKER): pyproject.toml | venv
	$(VENV)/pip install -e .[dev]
	touch $(DEV_MARKER)

test: dev-venv
	$(VENV)/pytest
