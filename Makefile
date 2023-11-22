# Frontend management make
include web/Makefile

default: help

# Frontend make file context
FRONTEND_CONTEXT = make -C web frontend

INFO = "\033[32m[INFO]\033[0m"

#❓ help: @ Displays all commands and tooling
help:
	@grep -E '[a-zA-Z\.\-]+:.*?@ .*$$' $(MAKEFILE_LIST)| tr -d '#'  | awk 'BEGIN {FS = ":.*?@ "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}'

clean:
	@echo $(INFO) "Cleaning project..."
	$(FRONTEND_CONTEXT).clean
	@echo $(INFO) "Complete. Run 'make setup' to install dependencies"

setup:
	$(FRONTEND_CONTEXT).setup
	@npm i
	@pip install -r requirements.txt
	@echo $(INFO) "Complete. Run 'make start' to start server"

# Helper for running dev mode
start:
	@flask run --debug &
	@npm run browsersync

lint:
	$(FRONTEND_CONTEXT).lint
	@echo $(INFO) "Complete"

check:
	$(FRONTEND_CONTEXT).check

