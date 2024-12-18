import numpy as np
from scipy.integrate import dblquad

C, n, A = 6161.68, 3.25, 305.39

def E_single(x, y, x0, y0):
    r = np.sqrt((x - x0)**2 + (y - y0)**2)
    return C / (r**n + A)

def E_total(x, y, positions):
    return sum(E_single(x, y, x0, y0) for x0, y0 in positions)

def compute_case1(d, w=8.5, h=8.5):
    x_min, x_max = -d / 2, d / 2
    y_min, y_max = 0, w
    positions = [(0, 0), (-d, 0), (d, 0), (0, h), (0, -h)]
    total_light = dblquad(lambda x, y: E_total(x, y, positions), x_min, x_max, lambda x: y_min, lambda x: y_max)[0]
    total_area = (x_max - x_min) * (y_max - y_min)
    E_avg = total_light / total_area
    corner_points = [(x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max), (0, y_max)]
    E_min = min(E_total(x, y, positions) for x, y in corner_points)
    U = E_min / E_avg
    return U, E_avg, E_min

def find_case1_uniformity(w=8.5, h=8.5):
    d_values = np.linspace(8, 20, 2000)
    for d in d_values:
        y_intercept = w / 2 * d / h
        if y_intercept > w:
            break
        U, E_avg, E_min = compute_case1(d, w, h)
        if abs(U - 0.55) < 1e-2:
            return d, U, E_avg, E_min

d_case1, U_case1, E_avg_case1, E_min_case1 = find_case1_uniformity()

print(f"五边形均匀度为 0.55: 距离 d = {d_case1:.2f}, 均匀度 U = {U_case1:.2f}, 平均照度 E_avg = {E_avg_case1:.2f}, 最低照度 E_min = {E_min_case1:.2f}")
