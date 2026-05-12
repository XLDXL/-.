import random
from agent_base import BaseAgent, Event, EventType
from config import FAILURE_RATE

class ExecutorAgent(BaseAgent):
    def can_handle(self, event):
        return event.type == EventType.DECISION

    def handle(self, event):
        action = event.data["action"]
        result = f"{action} 成功" if random.random() > FAILURE_RATE else f"{action} 失败"
        print(f"[Executor] 执行结果: {result}")
        self.bus.publish(Event(
            type=EventType.ACTION,
            data={"result": result, **event.data},
            source=self.name
        ))