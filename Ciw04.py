import ciw
N = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=0.3),
                           ciw.dists.Exponential(rate=0.2),
                           ciw.dists.NoArrivals()],
    service_distributions=[ciw.dists.Exponential(rate=1.0),
                           ciw.dists.Exponential(rate=0.4),
                           ciw.dists.Exponential(rate=0.5)],
    routing=[[0.0, 0.3, 0.7],
             [0.0, 0.0, 1.0],
             [0.0, 0.0, 0.0]],
    number_of_servers=[1, 2, 2]
)

completed_custs = []
for trial in range(10):
    ciw.seed(trial)
    Q = ciw.Simulation(N)
    Q.simulate_until_max_time(200)
    recs = Q.get_all_records()
    num_completed = len([r for r in recs if r.node==3 and r.arrival_date < 180])
    completed_custs.append(num_completed)
print(sum(completed_custs) / len(completed_custs))