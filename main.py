import time
from coordinator import Coordinator

if __name__ == "__main__":
    coordinator = Coordinator()
    coordinator.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        coordinator.stop()