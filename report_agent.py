from agent_base import BaseAgent, Event, EventType

class ReportAgent(BaseAgent):
    def can_handle(self, event):
        return event.type == EventType.ACTION

    def handle(self, event):
        print(f"[Report] 运营总结:")
        print(f"  CPU: {event.data['cpu']}%")
        print(f"  原因: {event.data['cause']}")
        print(f"  决策: {event.data['action']}")
        print(f"  结果: {event.data['result']}")
        print("-" * 40)