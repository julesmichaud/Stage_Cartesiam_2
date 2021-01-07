__author__ = 'julesmichaud'
__filename__ = 'Regroup_data.py'
__date__ = '25/11/20'

"""We want now to regroup datas activity by activity to put them in the studio, used for train and for test"""

"Attribute to objective 'train' or 'test' value to extract datas"

objective = "train"

f_volunteers = open(objective+"/subject_"+objective+".txt", "r")
volunteers = list(set(line for line in f_volunteers))

for activity in range(1, 7):
    "Creation of a file for the activity selected datas"
    f_activity = open(objective+"/dataset_studio/data_" + str(activity) + ".txt", "w")
    for x in volunteers:
        f = open(objective+"/dataset_intermed/dataset_" + str(activity) + "\n_" + str(x) + ".txt", "r")
        for line in f:
            f_activity.write(line)
