==============================================
For my project, datas found (availibles in Dataset_brut) contains accelerations and gyroscope datas. I based my searches only on the "total accelerations data". These datas weren't in the good disposition for my work : there were separated by coordinates (x/y/z) but i had to separate them by label_activities (1/2/3/4/5/6).
I wrote two python files, one to separate each file by activity label, then another one to segroup them in the good format (acc_x_subject1 acc_y_subject1 acc_z_subject1,  acc_x_subject2 acc_y_subject2 acc_z_subject2, etc)
=============================================

Datset_traite contains two python files :
  - Separate_datas.py : the first python file described above this
  - Regroup_datas.py : the other python file described above this

Dataset_traite also contains two folders :
  - train : contains dataset_studio (files created by Separated_datas.py then Regroup_datas.py) for the train subjects.
  - test : contains dataset_studio (files created by Separated_datas.py then Regroup_datas.py) for the test subjects.
