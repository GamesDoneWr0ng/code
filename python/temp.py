import pickle
timesteps = {'main': 2749520}

with open('python/pong/policies/timesteps.pkl', 'wb') as f:
    pickle.dump(timesteps, f)
