import ciw
N = ciw.create_network(
   arrival_distributions=[ciw.dists.Exponential(rate=6.0)],
   service_distributions=[ciw.dists.Exponential(rate=5.0)],
   routing=[[0.5]],
   number_of_servers=[1],
   queue_capacities=[3]
)
ciw.seed(1)
Q = ciw.Simulation(N,
    deadlock_detector=ciw.deadlock.StateDigraph(),
    tracker=ciw.trackers.NaiveBlocking()
)
Q.simulate_until_deadlock()
imp=Q.times_to_deadlock 
print(imp)