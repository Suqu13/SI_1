from datetime import datetime

from typing import List

from utils.StatisticsCalculator import Statistic


class FileWriter:
    def write(self, statistics: List[Statistic], file_name: str):
        now = datetime.now()
        now_formatted = now.strftime("%d-%m-%YT%H:%M:%S")
        file = open(f"results/{file_name}-{now_formatted}.csv", "w+")
        [file.write(f"{statistic.iteration_number};{statistic.best};{statistic.avg};{statistic.worst}\n") for statistic
         in statistics]
        file.close()
