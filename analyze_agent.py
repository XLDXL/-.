from agent_base import BaseAgent, Event, EventType

class AnalyzeAgent(BaseAgent):
    def can_handle(self, event):
        return event.type == EventType.ALERT

    def handle(self, event):
        cause = "流量突增" if event.data["cpu"] > 90 else "正常波动"
        print(f"[Analyze] 原因判定: {cause}")
        self.bus.publish(Event(
            type=EventType.ANALYSIS,
            data={"cause": cause, **event.data},
            source=self.name
        ))