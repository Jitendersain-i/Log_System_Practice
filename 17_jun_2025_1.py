from typing import List, Dict
from collections import defaultdict, deque
class LogSystem:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.logs_p_user = defaultdict(list)
        self.recent_logs = deque(maxlen=capacity)
        self.log_levels_count = defaultdict(int)
        self.all_logs = []

    def add_log(self, line:str) -> None:
        try:
            timestamp_part, rest = line.split("] ", 1)
            timestamp = timestamp_part.strip("[")
            level, rest = rest.split(" ", 1)
            user_id, message = rest.split(": ", 1)


            log_entry = {
                "timestamp": timestamp,
                "level": level,
                "user_id": user_id,
                "message": message
            }
            self.logs_p_user[user_id].append(log_entry)
            self.recent_logs.append(log_entry)
            self.log_levels_count[level] += 1
            self.all_logs.append(log_entry)
        except:
            pass

    def get_user_logs(self, user_id: str) -> List[Dict]:
        return self.logs_p_user.get(user_id, [])

    def count_levels(self) -> Dict[str, int]:
        return dict(self.log_levels_count)

    def filter_logs(self, keyword: str) -> List[Dict]:
        keyword_lower = keyword.lower()
        return [log for log in self.all_logs if keyword_lower in log["message"].lower()]


    def get_recent_logs(self) -> List[Dict]:
        return list(self.recent_logs)
logs = [
    "[2025-06-16T10:00:00] INFO user1: Started process",
    "[2025-06-16T10:00:01] ERROR user1: Failed to connect",
    "[2025-06-16T10:00:02] INFO user2: Login successful",
    "[2025-06-16T10:00:03] WARN user3: Low memory",
    "[2025-06-16T10:00:04] ERROR user2: Timeout occurred",
    "[2025-06-16T10:00:05] INFO user1: Retrying connection"
]


log_manager = LogSystem(capacity=10)

for log in logs:
    log_manager.add_log(log)

print("Logs of user1:", log_manager.get_user_logs("user1"))
print("Level counts:", log_manager.count_levels())
print("Logs with 'timeout':", log_manager.filter_logs("timeout"))
print("Recent logs:", log_manager.get_recent_logs())


