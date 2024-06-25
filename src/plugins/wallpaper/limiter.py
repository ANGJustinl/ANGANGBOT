from collections import defaultdict
import time


class FreqLimiter:
    def __init__(self, default_cd_seconds):
        self.next_time = defaultdict(float)
        self.default_cd = default_cd_seconds

    def check(self, key) -> bool:
        return bool(time.time() >= self.next_time[key])

    def start_cd(self, key, cd_time=0):
        self.next_time[key] = time.time() + (
            cd_time if cd_time > 0 else self.default_cd
        )

    def left_time(self, key) -> float:
        return self.next_time[key] - time.time()


cd_time = 60
limiter = FreqLimiter(cd_time)
cd = 1919810
cd_lim = FreqLimiter(cd)
