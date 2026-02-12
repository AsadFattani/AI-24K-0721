import random

class SecuritySystem:
    def __init__(self):
        self.components = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.state = {c: random.choice([True, False]) for c in self.components}

    def show(self, title):
        print(f"\n{title}")
        for c in self.components:
            print(f"{c}: {'Vulnerable' if self.state[c] else 'Safe'}")

class SecurityAgent:
    def __init__(self, system):
        self.system = system
        self.vulnerable_components = []

    def scan(self):
        print("\nSystem Scan:")
        self.vulnerable_components = []
        for c in self.system.components:
            if self.system.state[c]:
                print(f"WARNING: {c} is vulnerable.")
                self.vulnerable_components.append(c)
            else:
                print(f"SUCCESS: {c} is safe.")

    def patch(self):
        print("\nPatching Vulnerabilities:")
        for c in self.vulnerable_components:
            print(f"Patching {c}...")
            self.system.state[c] = False

sys = SecuritySystem()
agent = SecurityAgent(sys)

sys.show("Initial System State:")
agent.scan()
agent.patch()
sys.show("Final System State:")
