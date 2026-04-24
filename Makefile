# CECS 478 Honeypot Project Makefile

.PHONY: up demo run stop down clean logs

up:
	@echo "Building and starting honeypot environment..."
	mkdir -p logs artifacts/release/logs artifacts/release/pcaps
	docker-compose up -d --build
	@echo "Honeypot is live on http://localhost:8080"

demo:
	@echo "Running demo vertical slice..."
	@echo "Demo started at $$(date)" | tee artifacts/release/logs/demo.log
	@echo "Sending test request to honeypot..." | tee -a artifacts/release/logs/demo.log
	curl -s http://localhost:8080 || true
	@echo "\nDemo complete at $$(date)" | tee -a artifacts/release/logs/demo.log
	@echo "Demo log saved to artifacts/release/logs/demo.log"

run: up
	docker-compose logs -f

logs:
	docker-compose logs -f

stop:
	docker-compose down

down:
	docker-compose down

clean:
	docker-compose down
	rm -rf logs/* artifacts/release/*
	@echo "Environment cleaned."
