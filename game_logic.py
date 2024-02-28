import math

def rotate_triangle(center, scale, mouse_pos):
    dx = mouse_pos[0] - center[0]
    dy = mouse_pos[1] - center[1]
    len = math.sqrt(dx * dx + dy * dy)

    dx, dy = (dx * scale / len, dy * scale / len) if len > 0 else (1, 0)

    pts = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
    pts = [(center[0] + p[0] * dx + p[1] * dy, center[1] + p[0] * dy - p[1] * dx) for p in pts]
    return pts
# Function to calculate angle between two vectors
def angle_between_vectors(dx1, dy1, dx2, dy2):
    dot_product = dx1 * dx2 + dy1 * dy2
    magnitude1 = math.sqrt(dx1**2 + dy1**2) + 0.0001
    magnitude2 = math.sqrt(dx2**2 + dy2**2) + 0.0001
    angle_rad = math.acos(dot_product / (magnitude1 * magnitude2))
    return math.degrees(angle_rad)
# Function to check if boid is within cone of vision
def within_cone_of_vision(dx_heading, dy_heading, dx_other, dy_other, cone_angle):
    angle = angle_between_vectors(dx_heading, dy_heading, dx_other, dy_other)
    return abs(angle) <= cone_angle / 2