__author__ = 'julesmichaud'
__filename__ = 'Separate_datas.py'
__date__ = '25/11/20'

"""Algorithm writing datas in new files .txt in order to separate them by activity and volunteer, used for train and for
 test"""

"Attribute to objective 'train' or 'test' value to extract datas"

objective = "train"

f_acc_read_x = open(objective + "/Inertial Signals/total_acc_x_" + objective + ".txt", "r")
f_acc_read_y = open(objective + "/Inertial Signals/total_acc_y_" + objective + ".txt", "r")
f_acc_read_z = open(objective + "/Inertial Signals/total_acc_z_" + objective + ".txt", "r")

f_volunteers = open(objective+"/subject_"+objective+".txt", "r")
f_activities = open(objective+"/y_"+objective+".txt", "r")

"We split datas in order to delete the double space between each data component"

txt_acc_x = [line.split() for line in f_acc_read_x]
txt_acc_y = [line.split() for line in f_acc_read_y]
txt_acc_z = [line.split() for line in f_acc_read_z]

volunteers = [line for line in f_volunteers]
activities = [line for line in f_activities]

"We write datas in a new file named by the activity number and the volunteer number"

for i in range(len(txt_acc_x)):
    f_write = open(objective+"/dataset_intermed/dataset_" + activities[i] + "_" + volunteers[i] + ".txt", "a")
    for j in range(len(txt_acc_x[i])):
        "A comparison more in order to remove a number in the form 1.001e-5 or something similar"
        'Acceleration'
        acc_x = float(txt_acc_x[i][j])
        if abs(acc_x) <= 0.0001:
            acc_x = 0
        acc_y = float(txt_acc_y[i][j])
        if abs(acc_y) <= 0.0001:
            acc_y = 0
        acc_z = float(txt_acc_z[i][j])
        if abs(acc_z) <= 0.0001:
            acc_z = 0
        f_write.write(str(acc_x) + " " + str(acc_y) + " " + str(acc_z) + " ")
    f_write.write("\n")
