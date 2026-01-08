import time
import uuid
from datetime import datetime, timezone

# Generate random string once at startup
RANDOM_STRING = str(uuid.uuid4())

def main():
    while True:
        timestamp = (
            datetime.now(timezone.utc)
            .isoformat(timespec="milliseconds")
            .replace("+00:00", "Z")
        )
        print(f"{timestamp}: {RANDOM_STRING}", flush=True)
        time.sleep(5)

if __name__ == "__main__":
    main()
