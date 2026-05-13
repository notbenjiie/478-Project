.PHONY: up down clean demo

up:
	docker compose up -d --build
	@echo "System running on http://localhost:8080"

down:
	docker compose down

clean:
	docker compose down -v
	rm -f logs/access.log
	rm -f artifacts/release/metrics.json
	rm -f artifacts/release/evidence.pcap

demo:
	@echo "Running demo..."
	sleep 5

	curl http://localhost:8080 || true
	curl http://localhost:8080/admin || true
	curl http://localhost:8080/login || true
	curl http://localhost:8080/wp-admin || true
	curl http://localhost:8080/phpmyadmin || true
	curl http://localhost:8080/test || true

	sleep 2

	@echo "---- Logs ----"
	cat logs/access.log || true
	@echo "--------------"

	python3 src/generate_metrics.py || python src/generate_metrics.py

	@echo "Demo complete."
