import numpy as np
import matplotlib as plt 

np.random.seed(123)

num_people=500
num_steps=100

all_walks=[]

for i in range(num_people):
    random_walk=[0]

for j in range(num_steps):
    step =random_walk[-1]
    dice=np.random.randint(1,7)

    if dice <= 2 :
        step=max(0,step -1)
    elif dice <=5:
        step=step+1
    else:
        step=step+np.random.randint(1,7)
    
    random_walk.append(step)
    all_walks.append(random_walk)

    np_aw=np.array(all_walks)

    np_aw_t=np.transpose(np_aw)

    plt.polt(np_aw_t[:,:10])
    plt.xlabel("step")
    plt.ylabel("position")
    plt.title("rendom")
    plt.show()

    ends=np_aw_t[-1,:]
    plt.hist(ends,bins=20)
    plt.xlabel("end")
    plt.ylabel("number")
    plt.title("final")
    plt.show()
