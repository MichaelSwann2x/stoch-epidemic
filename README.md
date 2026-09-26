# Stoch Epidemic (improved)

Gillespie CTMC SIR simulator inspired by the measles exercises in
[mirkovicdev/stokmod](https://github.com/mirkovicdev/stokmod).

**New:** vaccination experiment helper, multi-run summary stats, pure NumPy package + tests.

```python
from stoch_epidemic import simulate_sir_ctmc, vaccination_experiment
path = simulate_sir_ctmc(950, 50, 0, beta=0.5, gamma=0.1, t_max=200)
print(vaccination_experiment(vaccinated=100, n_sims=50))
```

MIT.
