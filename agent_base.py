import threading
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, Any

class EventType(Enum):
    ALERT = auto()
    ANALYSIS = auto()
    DECISION = auto()
    ACTION = auto()
    REPORT = auto()

@dataclass
class Event:
    type: EventType
    data: Dict[str, Any]
    source: str
    timestamp: float = field(default_factory=time.time)

class BaseAgent(threading.Thread, ABC):
    def __init__(self, name: str, bus):
        super().__init__(daemon=True)
        self.name = name
        self.bus = bus
        self.running = True

    def run(self):
        while self.running:
            try:
                event = self.bus.consume()
                if self.can_handle(event):
                    self.handle(event)
            except Exception as e:
                print(f"[{self.name}] Error: {e}")

    @abstractmethod
    def can_handle(self, event):
        pass

    @abstractmethod
    def handle(self, event):
        pass

    def stop(self):
        self.running = False