"""Stochastic epidemic models (SIR / measles CTMC)."""

from .sir import simulate_sir_ctmc, summarize_epidemic, vaccination_experiment

__version__ = "0.2.0"
__all__ = ["simulate_sir_ctmc", "summarize_epidemic", "vaccination_experiment"]
