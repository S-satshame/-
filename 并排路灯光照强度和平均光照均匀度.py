import numpy as np
from scipy.integrate import dblquad

C, n, A = 6161.68, 3.25, 305.39

def E_single(x, y, x0, y0):
    r = np.sqrt((x - x0)**2 + (y - y0)**2)
    return C / (r**n + A)

def E_total(x, y, positions):
    return sum(E_single(x, y, x0, y0) for x0, y0 in positions)

def compute_uniformity_rectangle(w=4.25, l=16.8):
    x_min, x_max = -l / 2, l / 2
    y_min, y_max = 0, w
    positions = [(0, 0), (-16.8, 0), (16.8, 0)]
    total_light = dblquad(lambda x, y: E_total(x, y, positions), x_min, x_max, lambda x: y_min, lambda x: y_max)[0]
    total_area = (x_max - x_min) * (y_max - y_min)
    E_avg = total_light / total_area
    corner_points = [(x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max)]
    E_min = min(E_total(x, y, positions) for x, y in corner_points)
    U = E_min / E_avg
    return U, E_avg, E_min

U, E_avg, E_min = compute_uniformity_rectangle()
print(f"任务一 - 均匀度 U = {U:.2f}, 平均照度 E_avg = {E_avg:.2f}, 最低照度 E_min = {E_min:.2f}")
