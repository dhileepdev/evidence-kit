.DEFAULT_GOAL := help

.PHONY: help test audit

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

test: ## Run the test suite
	pytest tests/ -v

audit: ## Build an evidence pack for a run directory
	python -m evidence audit --run-dir ./run --policy-results ./run/policy-results.json
