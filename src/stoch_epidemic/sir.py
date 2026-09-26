"""Continuous-time Markov chain SIR (measles-style) simulator."""

from __future__ import annotations

from typing import Optional

import numpy as np


def simulate_sir_ctmc(
    S0: int,
    I0: int,
    R0: int,
    beta: float,
    gamma: float,
    t_max: float,
    rng: Optional[np.random.Generator] = None,
) -> dict:
    """Gillespie-style CTMC for SIR until t_max or I=0."""
    rng = rng or np.random.default_rng()
    N = S0 + I0 + R0
    t = 0.0
    S, I, R = S0, I0, R0
    times = [0.0]
    Ss, Is, Rs = [S], [I], [R]

    while t < t_max and I > 0:
        rate_inf = beta * S * I / N if N > 0 else 0.0
        rate_rec = gamma * I
        rate_total = rate_inf + rate_rec
        if rate_total <= 0:
            break
        dt = rng.exponential(1.0 / rate_total)
        t += dt
        if t > t_max:
            break
        if rng.random() < rate_inf / rate_total:
            S -= 1
            I += 1
        else:
            I -= 1
            R += 1
        times.append(t)
        Ss.append(S)
        Is.append(I)
        Rs.append(R)

    return {
        "times": np.array(times),
        "S": np.array(Ss),
        "I": np.array(Is),
        "R": np.array(Rs),
        "N": N,
        "peak_I": int(max(Is)),
        "peak_time": float(times[int(np.argmax(Is))]),
        "final_size": int(Rs[-1] - R0),
    }


def summarize_epidemic(paths: list[dict]) -> dict:
    peaks = np.array([p["peak_I"] for p in paths], dtype=float)
    finals = np.array([p["final_size"] for p in paths], dtype=float)
    tpeaks = np.array([p["peak_time"] for p in paths], dtype=float)
    return {
        "n_runs": len(paths),
        "peak_I_mean": float(peaks.mean()),
        "peak_I_std": float(peaks.std()),
        "final_size_mean": float(finals.mean()),
        "final_size_std": float(finals.std()),
        "peak_time_mean": float(tpeaks.mean()),
    }


def vaccination_experiment(
    N: int = 1000,
    I0: int = 50,
    beta: float = 0.5,
    gamma: float = 0.1,
    t_max: float = 300.0,
    vaccinated: int = 0,
    n_sims: int = 100,
    seed: int = 0,
) -> dict:
    rng = np.random.default_rng(seed)
    S0 = N - I0 - vaccinated
    R0 = vaccinated
    paths = [
        simulate_sir_ctmc(S0, I0, R0, beta, gamma, t_max, rng=rng)
        for _ in range(n_sims)
    ]
    return summarize_epidemic(paths)
