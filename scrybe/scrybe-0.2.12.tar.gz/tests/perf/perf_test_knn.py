import timeit
from tests.test_grid_cv import train_knn_model


print(timeit.timeit("train_knn_model(verbose=False)", globals=globals(), number=100))

# With Scrybe: 19.699598363
# With Scrybe (uuid1): 18.714405664
# Without Scrybe: 1.9080252570000003
