from agent_base import BaseAgent, Event, EventType

class DecisionAgent(BaseAgent):
    def can_handle(self, event):
        return event.type == EventType.ANALYSIS

    def handle(self, event):
        action = "扩容" if event.data["cause"] == "流量突增" else "观察"
        print(f"[Decision] 决策结果: {action}")
        self.bus.publish(Event(
            type=EventType.DECISION,
            data={"action": action, **event.data},
            source=self.name
        ))