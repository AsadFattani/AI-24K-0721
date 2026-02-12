import random

class Servers:
    def __init__ (self, name):
        self.name = name
        self.status = random.choice(["Completed", "Failed"])
    

class BackupManagementAgent:
    def __init__ (self, servers):
        self.servers = servers

    def show_status(self, title):
        print(f"\n{title}")
        for s in self.servers:
            print(f"{s.name}: {s.status}")
    
    def backup(self):
        print()
        for s in self.servers:
            if s.status == "Failed":
                print(f"Trying to backup {s.name}...")
                s.status = "Completed"

servers = [Servers(f"Server {i+1}") for i in range(5)]
agent = BackupManagementAgent(servers)
agent.show_status("Initial Backup Status:")
agent.backup()
agent.show_status("Updated Backup Status:")



