import numpy as np

class MathUtility:
    def rotate_points(points:np.ndarray, angle:float, pivot:np.ndarray) -> np.ndarray:
        theta:float = np.radians(angle)
        c, s:float = np.cos(theta), np.sin(theta)
        R:np.ndarray = np.array(((c, -s), (s, c)))
        return ((points - pivot) @ R.T) + pivot

    def rotate_points(points:np.ndarray, rotation_matrix:np.ndarray, pivot:np.ndarray) -> np.ndarray:
        return ((points - pivot) @ rotation_matrix.T) + pivot

    def rotate_points_origin(points:np.ndarray, rotation_matrix:np.ndarray) -> np.ndarray:
        return points @ rotation_matrix.T