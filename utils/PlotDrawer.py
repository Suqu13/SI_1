from typing import List

import matplotlib.patches as mpatches

from utils.StatisticsCalculator import Statistic

class PlotDrawer:
    def draw(self, stats: List[Statistic], plotter, canvas):
        if len(stats) > 0:
            plotter.clear()
            plotter.set_ylabel('Distance')
            plotter.set_xlabel('Generation number')
            plotter.grid()
            x = [i for i in range(0, len(stats))]
            best = [stat.best for stat in stats]
            worst = [stat.worst for stat in stats]
            avg = [stat.avg for stat in stats]
            plotter.plot(x, best)
            plotter.plot(x, worst)
            plotter.plot(x, avg)
            best_legend = mpatches.Patch(color="blue", label="Best")
            avg_legend = mpatches.Patch(color="orange", label="Worst")
            worst_legend = mpatches.Patch(color="green", label="Avg")
            plotter.legend(handles=[best_legend, avg_legend, worst_legend])
            canvas.draw()
