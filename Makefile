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

include Makefile.venv
Makefile.venv:
	curl \
		-o Makefile.fetched \
		-L "https://github.com/sio/Makefile.venv/raw/v2023.04.17/Makefile.venv"
	echo "fb48375ed1fd19e41e0cdcf51a4a0c6d1010dfe03b672ffc4c26a91878544f82 *Makefile.fetched" \
		| sha256sum --check - \
		&& mv Makefile.fetched Makefile.venv
