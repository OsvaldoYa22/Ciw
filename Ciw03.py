import ciw
N = ciw.create_network(
    arrival_distributions=[ciw.dists.Exponential(rate=0.2)],
    service_distributions=[ciw.dists.Exponential(rate=0.1)],
    number_of_servers=[4])

average_waits = []
for trial in range(10):
    ciw.seed(trial)
    Q = ciw.Simulation(N)
    Q.simulate_until_max_time(1640)
    recs = Q.get_all_records()
    waits = [r.waiting_time for r in recs if r.arrival_date > 100 and r.arrival_date < 1540]
    mean_wait = sum(waits) / len(waits)
    average_waits.append(mean_wait)
print(sum(average_waits) / len(average_waits))