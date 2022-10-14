from scipy.sparse import random
from scipy import stats
from numpy.random import default_rng
rng = default_rng()
rvs = stats.poisson(25, loc=10).rvs
S = random(3, 4, density=0.25, random_state=rng, data_rvs=rvs)
S.A
print(S.A)