def point_inside_rect_ui(point, rect):
    return point[0] > rect[0] and point[0] < rect[0] + rect[2] and point[1] > rect[1] and point[1] < rect[1] + rect[3]