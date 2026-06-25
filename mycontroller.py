from . import BaseController
import numpy as np

class Controller(BaseController):
    def __init__(self):
        self.p = 0.195
        self.i = 0.100
        self.d = -0.053
        self.error_integral = 0
        self.prev_error = 0

    def update(self, target_lataccel, current_lataccel, state, future_plan):
        future_lataccels = future_plan.lataccel
        if future_lataccels is not None and len(future_lataccels) > 0:
            horizon = min(3, len(future_lataccels))
            smoothed_target = 0.2 * target_lataccel + 0.8 * np.mean(future_lataccels[:horizon])
        else:
            smoothed_target = target_lataccel

        error = (smoothed_target - current_lataccel)
        self.error_integral = np.clip(self.error_integral + error, -20, 20)
        error_diff = error - self.prev_error
        self.prev_error = error
        return self.p * error + self.i * self.error_integral + self.d * error_diff
