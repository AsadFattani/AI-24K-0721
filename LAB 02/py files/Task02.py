class ThreatIntelligence:
    def __init__(self, threat_id, name, severity):
        self.threat_id = threat_id
        self.name = name
        self.severity = severity

    def displayInfo(self):
        print(f"Threat ID: {self.threat_id}")
        print(f"Name: {self.name}")
        print(f"Severity: {self.severity}")

class PhisingThreat(ThreatIntelligence):
    def analyze_email(self):
        print(f"Analyzing email for phishing indicators in threat '{self.name}' (ID: {self.threat_id})...")

class RansomewareThreat(ThreatIntelligence):
    def scan_files(self):
        print(f"Scanning files for ransomware signatures in threat '{self.name}' (ID: {self.threat_id})...")

class BotnetThreat(ThreatIntelligence):
    def detect_traffic(self):
        print(f"Detecting suspicious network traffic for botnet activity in threat '{self.name}' (ID: {self.threat_id})...")


t1 = PhisingThreat(101, "Phishing Attack", "High")
t2 = RansomewareThreat(102, "Ransomware Attack", "Critical")
t3 = BotnetThreat(103, "Botnet Activity", "Medium")
t1.displayInfo()
t1.analyze_email()
t2.displayInfo()
t2.scan_files()
t3.displayInfo()
t3.detect_traffic()
