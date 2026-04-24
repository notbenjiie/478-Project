# CECS 478 Honeypot Project Makefile

.PHONY: up demo down clean logs

up:
	@echo "Starting system..."
	mkdir -p logs artifacts/release/logs artifacts/release/pcaps
	docker-compose up -d --build
	@echo "System running on http://localhost:8080"

demo:
	@echo "Running demo..."
	curl http://localhost:8080 > nul 2>&1 || true
	timeout /t 2 > nul
	@echo "---- Logs ----"
	type logs\access.log
	@echo "--------------"
	@echo "Demo complete."

logs:
	docker-compose logs

down:
	docker-compose down

clean:
	docker-compose down
	rmdir /s /q logs 2>nul || true
	rmdir /s /q artifacts 2>nul || true
	@echo "Cleaned."