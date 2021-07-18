from datetime import datetime

class Time:
    def __init__(self, current_time="00"):
        self.current_time = current_time

    def get_current_time(self):
        now = datetime.now()
        self.current_time = now.strftime("%H")
        return self.current_time

