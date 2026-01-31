class ResponseAgent:
    def execute_response(self):
        print("This is base agent")

class AlertAgent(ResponseAgent):
    def execute_response(self):
        print("The user has been notified")

class BlockAgent(ResponseAgent):
    def execute_response(self):
        print("The threat has been blocked")

class RecoverAgent(ResponseAgent):
    def execute_response(self):
        print("The effected system has been restored")

a1 = AlertAgent()
a1.execute_response()
a2 = BlockAgent()
a2.execute_response()
a3 = RecoverAgent()
a3.execute_response()

