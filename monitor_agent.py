import random
import time
from agent_base import BaseAgent, Event, EventType
from config import MONITOR_INTERVAL, CPU_THRESHOLD

class MonitorAgent(BaseAgent):
    def __init__(self, bus):
        super().__init__("MonitorAgent", bus)

    def run(self):
        while self.running:
            cpu = random.randint(0, 100)
            if cpu > CPU_THRESHOLD:
                self.bus.publish(Event(
                    type=EventType.ALERT,
                    data={"cpu": cpu},
                    source=self.name
                ))
                print(f"[Monitor] CPU 异常: {cpu}%")
            time.sleep(MONITOR_INTERVAL)

    def can_handle(self, event):
        return False