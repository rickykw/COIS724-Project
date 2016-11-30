import debacl as dcl
import numpy as np
import matplotlib.pyplot as plt
import os

# from sklearn.datasets import make_moons

data_count = len(os.walk('./Data/').next()[1])  # count the number of datasets
users_list = []
plt.style.use('grayscale')
total_stay_points = []
for i in range(0, int(data_count)):
    # open the folder
    file_name = './StayPoints/00' + str(i) + '.txt'
    stay_points = open(file_name, 'r')

    # handle the data as a array of numpy
    stay_points = list(stay_points)

    stay_points = [s.strip('\n').split(',') for s in stay_points]
    size = len(stay_points)
    for u in range(size):
        users_list.append(i)
    stay_points = np.asarray(stay_points, dtype='float32')
    total_stay_points.append(stay_points)
total_stay_points = [item for sublist in total_stay_points for item in sublist]
total_stay_points = np.asarray(total_stay_points)

# print total_stay_points.shape
# print len(users_list)

# clustering
tree = dcl.construct_tree(total_stay_points, k=100)
fig = tree.plot(form='density')[0]
labels = tree.get_clusters()
# fig.show()

# write TBHG to the TBHG.txt
tree_file = open("./Clustering/TBHG.txt", "w")
tree_str = str(tree)
tree_file.write(tree_str)


# determine the specific user in the each low-level cluster
cluster_dict = {}

for entry in labels:
    cluster_dict[entry[1]] = []

clusters = open("./Clustering/Clusters.txt", "w")

for entry in labels:
    cluster_dict[entry[1]].append(users_list[entry[0]])
for k, v in cluster_dict.iteritems():
    cluster_dict[k] = list(set(cluster_dict[k]))
    clusters.write("%s: %s\n" % (str(k), str(cluster_dict[k]).strip('[]')))
# print cluster_dict

cluster_centroids_file = open("cluster_centroids.txt", "w")

cluster_centroids = {}

for entry in labels:
    cluster_centroids[entry[1]] = []

for entry in labels:
    cluster_centroids[entry[1]].append(total_stay_points[entry[0]])
    
for key, value in cluster_centroids.iteritems():
    cluster_centroids[key] = np.asarray(cluster_centroids[key], dtype='float32')
    cluster_centroids[key] = np.mean(cluster_centroids[key], axis=0)
    #print "the key [%s] has shape %s\n" % (str(key), str(cluster_centroids[key].shape))
'''    
for k, v in cluster_dict.iteritems():
    cluster_dict[k] = list(set(cluster_dict[k]))
'''

for key, value in cluster_centroids.iteritems():
    cluster_centroids_file.write("%s---> %s\n" % (str(key), str(value).strip('[]')))
