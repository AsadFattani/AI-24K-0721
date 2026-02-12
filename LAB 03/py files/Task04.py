import random

class SecurityEnvironment:
    def __init__(self):
        self.components = ['A','B','C','D','E','F','G','H','I']
        self.states = ['Safe', 'Low Risk Vulnerable', 'High Risk Vulnerable']
        self.system = {c: random.choice(self.states) for c in self.components}

    def display_system(self, title):
        print(f"\n{title}")
        for c in self.components:
            print(f"Component {c}: {self.system[c]}")

    def patch_low_risk(self):
        for c in self.components:
            if self.system[c] == 'Low Risk Vulnerable':
                self.system[c] = 'Safe'

class UtilityBasedSecurityAgent:
    def scan_and_patch(self, env):
        for c in env.components:
            state = env.system[c]
            if state == 'Safe':
                print(f"[OK] Component {c} is Safe.")
            elif state == 'Low Risk Vulnerable':
                print(f"[!] Component {c} has Low Risk Vulnerability. Patching...")
            elif state == 'High Risk Vulnerable':
                print(f"[!!] Component {c} has High Risk Vulnerability. Premium service required.")

        env.patch_low_risk()

env = SecurityEnvironment()
env.display_system("Initial System State")

agent = UtilityBasedSecurityAgent()
print("\n--- System Scan & Patching ---")
agent.scan_and_patch(env)

env.display_system("Final System State")
