class SecurityAgent:
    def __init__(self, agent_id, name, status):
        self.agent_id = agent_id
        self.name = name
        self.status = status

    def displayInfo(self):
        print (f"Agent ID: {self.agent_id}")
        print (f"Name: {self.name}")
        print (f"Status: {self.status}")


class FirewallAgent(SecurityAgent):
    def monitor_traffic(self):
        print (f"{self.name} is monitoring network traffic.\n")
    
    def displayInfo(self):
        super().displayInfo()

class MalwareDetectionAgent(SecurityAgent):
    def scan_files(self):
        print (f"{self.name} is scanning files for malware.\n")
        
    def displayInfo(self):
        super().displayInfo()

class AutomationAgent(SecurityAgent):
    def run_automation(self):
        print (f"{self.name} is running automated security tasks.\n")

    def displayInfo(self):
        super().displayInfo()

a1 = FirewallAgent(1, "Firewall Agent 1", "active")
a2 = MalwareDetectionAgent(2, "Malware Detection Agent 1", "active")
a3 = AutomationAgent(3, "Automation Agent 1", "inactive")

a1.displayInfo()
a1.monitor_traffic()
a2.displayInfo()
a2.scan_files()
a3.displayInfo()
a3.run_automation()





