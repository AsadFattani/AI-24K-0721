import random

class Server:
    def __init__(self, name):
        self.name = name
        self.load = random.choice(["Underloaded", "Balanced", "Overloaded"])

class DataCenter:
    def __init__(self):
        self.servers = [Server(f"Server {i+1}") for i in range(5)]

    def show_status(self, title):
        print(f"\n{title}")
        for s in self.servers:
            print(f"{s.name}: {s.load}")

class LoadBalancerAgent:
    def __init__(self, datacenter):
        self.datacenter = datacenter

    def balance_load(self):
        overloaded = [s for s in self.datacenter.servers if s.load == "Overloaded"]
        underloaded = [s for s in self.datacenter.servers if s.load == "Underloaded"]

        print("\nBalancing Loads:")
        while overloaded and underloaded:
            o = overloaded.pop()
            u = underloaded.pop()
            print(f"Moving tasks from {o.name} to {u.name}.")
            o.load = "Balanced"
            u.load = "Balanced"

datacenter = DataCenter()
agent = LoadBalancerAgent(datacenter)

datacenter.show_status("Initial Server Load Status:")
agent.balance_load()
datacenter.show_status("Updated Server Load Status:")
