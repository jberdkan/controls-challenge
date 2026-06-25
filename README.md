Started from the stock PID baseline and made two targeted improvements:

Integral anti-windup clamp (±20) — the stock PID had an unbounded integral that caused divergence on segments with sustained lateral offset, producing high-cost outliers. Clamping the integral prevents runaway windup while preserving normal integral action.
Future plan target smoothing — used the available 5-second lookahead (future_plan.lataccel) to smooth the target signal, blending 30% current target with 70% near-term average (3-step horizon). This reduces lataccel tracking error by anticipating trajectory changes rather than reacting to them.

Result: total cost 83.03 vs baseline 110.3 on 5000 segments (~25% improvement).
