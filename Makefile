default: help

INFO = "\033[32m[INFO]\033[0m"

#❓ help: @ Displays all commands and tooling
help:
	@grep -E '[a-zA-Z\.\-]+:.*?@ .*$$' $(MAKEFILE_LIST)| tr -d '#'  | awk 'BEGIN {FS = ":.*?@ "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}'

clean:
	@echo $(INFO) "Cleaning project..."
	@rm -rf node_modules
	@rm package-lock.json
	@echo $(INFO) "Complete. Run 'make setup' to install dependencies"

setup:
	@echo $(INFO) "Installing NPM dependencies..."
	@npm i
	@echo $(INFO) "Complete. Run 'make start' to start server"

# Helper for running dev mode
start:
	@flask run --debug

lint:
	@echo $(INFO) "Formatting Js/CSS"
	@npm run format
	@echo $(INFO) "Linting Js"
	@npm run lint
	@echo $(INFO) "Complete"

check:
	@echo $(INFO) "Typechecking Js"
	@npm run typecheck

