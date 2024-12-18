def compute_uniformity_taylor(d=16.8, w=8.5, h=8.5):
    x_min, x_max = -d / 2, d / 2
    y_min, y_max = 0, w
    positions = [(0, 0), (-d, 0), (d, 0), (0, h), (0, -h)]
    total_light = dblquad(lambda x, y: E_total(x, y, positions), x_min, x_max, lambda x: y_min, lambda x: y_max)[0]
    total_area = (x_max - x_min) * (y_max - y_min)
    E_avg = total_light / total_area
    corner_points = [(x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max)]
    E_min = min(E_total(x, y, positions) for x, y in corner_points)
    U = E_min / E_avg
    return U, E_avg, E_min

U, E_avg, E_min = compute_uniformity_taylor()
print(f"任务二 - 泰森多边形均匀度 U = {U:.2f}, 平均照度 E_avg = {E_avg:.2f}, 最低照度 E_min = {E_min:.2f}")
