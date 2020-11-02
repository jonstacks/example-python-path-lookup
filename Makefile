docker-build:
	docker build -t python-path-lookup .

test: docker-build
	@echo "-------------------------------------------------"
	@echo "Starting Test"
	@docker run --rm -it python-path-lookup