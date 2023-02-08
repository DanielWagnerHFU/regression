import numpy as np

class MathUtility:
    def rotate_points(points, angle, pivot) -> np.ndarray:
        theta = np.radians(angle)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))
        return ((points - pivot) @ R.T) + pivot

    #def rotate_points(points:np.ndarray, rotation_matrix:np.ndarray, pivot:np.ndarray) -> np.ndarray:
    #    return ((points - pivot) @ rotation_matrix.T) + pivot

    def rotate_points_origin(points, angle) -> np.ndarray:
        theta = np.radians(angle)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array(((c, -s), (s, c)))
        return points @ R.T