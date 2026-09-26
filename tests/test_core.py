from stoch_epidemic import simulate_sir_ctmc, vaccination_experiment, summarize_epidemic

def test_sim_runs():
    out = simulate_sir_ctmc(950, 50, 0, beta=0.5, gamma=0.1, t_max=50)
    assert out["peak_I"] >= 50
    assert len(out["times"]) > 1

def test_vax_reduces_peak():
    base = vaccination_experiment(vaccinated=0, n_sims=20, seed=1)
    vax = vaccination_experiment(vaccinated=200, n_sims=20, seed=1)
    assert vax["peak_I_mean"] <= base["peak_I_mean"] + 5

def test_summarize():
    paths = [simulate_sir_ctmc(100, 5, 0, 0.3, 0.2, 20) for _ in range(5)]
    s = summarize_epidemic(paths)
    assert s["n_runs"] == 5
