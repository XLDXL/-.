from event_bus import MessageBus
from agents.monitor_agent import MonitorAgent
from agents.analyze_agent import AnalyzeAgent
from agents.decision_agent import DecisionAgent
from agents.executor_agent import ExecutorAgent
from agents.report_agent import ReportAgent

class Coordinator:
    def __init__(self):
        self.bus = MessageBus()
        self.agents = [
            MonitorAgent(self.bus),
            AnalyzeAgent(self.bus),
            DecisionAgent(self.bus),
            ExecutorAgent(self.bus),
            ReportAgent(self.bus),
        ]

    def start(self):
        for agent in self.agents:
            agent.start()
        print("✅ 多 Agent 协同系统启动")

    def stop(self):
        for agent in self.agents:
            agent.stop()
        print("🛑 系统已停止")