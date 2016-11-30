import debacl as dcl
import numpy as np
import matplotlib

total_stay_points = []

for i in range(0,6):
    file_name = '00' + str(i) + '.txt'
    stay_points = open(file_name, 'r')
    stay_points = list(stay_points)
    print len(stay_points)
    stay_points = [s.strip('\n').split(',') for s in stay_points]
    stay_points = np.asarray(stay_points, dtype='float32')
    tree = dcl.construct_tree(stay_points, k=10)
    print tree
    fig = tree.plot(form='density')[0]
    labels = tree.get_clusters()
    print labels.shape
    fig.show()
    break
    #total_stay_points.append(stay_points)
    #print tree[0]
#print len(total_stay_points)    
#total_stay_points = np.asarray(total_stay_points, dtype='float32')
    

