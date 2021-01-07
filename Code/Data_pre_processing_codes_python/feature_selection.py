# -*- coding: utf-8 -*-

#%% import librairies 
from os import listdir
from os.path import isfile, join

import  numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif, chi2

#%% import data 

# path to the data files 
mypath='C:/Users/Dali/Downloads/1250A/1250A'  
# all csv files
all_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#create a list of data frames to store all the data
list_of_dfs=[pd.read_csv(join(mypath, f), sep = ' ',header=None) for f in all_files]


#%%   create dataframes that contain normal and anomaly data
#concatenate all normal_data  and anomaly data
data_normal=pd.concat([(list_of_dfs[-3]).iloc[:50],(list_of_dfs[-2]).iloc[:50],(list_of_dfs[-1]).iloc[:50]]).values
data_anomaly=list_of_dfs[0].values
data_multiclass=pd.concat([list_of_dfs[2],list_of_dfs[5],list_of_dfs[8], list_of_dfs[11],list_of_dfs[14]]).values

#%% transform 3 axis accelerations to the resultant acceleration 
data_normal=(data_normal[:,0::3]**2+data_normal[:,1::3]**2+data_normal[:,2::3]**2)**0.5
data_anomaly=(data_anomaly[:,0::3]**2+data_anomaly[:,1::3]**2+data_anomaly[:,2::3]**2)**0.5
data_multiclass=(data_multiclass[:,0::3]**2+data_multiclass[:,1::3]**2+data_multiclass[:,2::3]**2)**0.5

#%%concatenate normal and anomaly data and create the label
data= np.vstack((data_normal,data_multiclass))
label=np.asarray([0]*len(data_normal)+[1]*len(list_of_dfs[2])+[2]*len(list_of_dfs[5])+[3]*len(list_of_dfs[8])+[4]*len(list_of_dfs[11])+[5]*len(list_of_dfs[14])).T

#%% fft transform  
data_freq=np.abs(np.fft.rfft(data))
#%% plot the signals 
#close all figures
plt.close('all')
# plot the spectrum of each data type
for i in range(len(label)):
    plt.figure(label[i])
    plt.plot(data_freq[i,:])
    
# add titles     
titles=['normal_data','faul type ']  
plt.figure(0)
plt.title(titles[0])
for i in range(1,6) :
    plt.figure(i)
    plt.title(titles[1]+str(i))
    

#%% applying feature selection techniques

#apply SelectKBest class to extract 
bestfeatures_mutual= SelectKBest(score_func=mutual_info_classif)
bestfeatures_chi= SelectKBest(score_func=chi2)


fit_mutual= bestfeatures_mutual.fit(data_freq,label)
fit_chi= bestfeatures_chi.fit(data_freq,label)

scores_mutual= fit_mutual.scores_
scores_chi=fit_chi.scores_

#plot scores
plt.figure(6)
plt.plot(scores_mutual)
plt.title('scores based on mutual information')

plt.figure(7)
plt.plot(scores_chi)
plt.title('scores based on chi2')
#%% save data with the highest scores
chi_indices=scores_chi>scores_chi.mean()
mutual_indices=scores_mutual>scores_mutual.mean()

np.savetxt(titles[0]+'_chi'+'.txt',data_freq[label==0][:,chi_indices], delimiter=" ",  fmt='%s')
np.savetxt(titles[0]+'_mutual'+'.txt',data_freq[label==0][:,mutual_indices], delimiter=" ",  fmt='%s')

for i in range(1,6):
    np.savetxt(titles[1]+'_chi'+ str(i)+'.txt',data_freq[label==i][:,chi_indices], delimiter=" ",  fmt='%s')
    np.savetxt(titles[1]+'_mutual'+ str(i)+'.txt',data_freq[label==i][:,mutual_indices], delimiter=" ",  fmt='%s')



#
#
#
#dfscores_mutual= pd.DataFrame(fit_mutual.scores_)
#dfscores_chi= pd.DataFrame(fit_chi.scores_)
#
#dfcolumns= pd.DataFrame(np.array(range(data.shape[1])))
##concat two dataframes for better visualization 
#featureScores_mutual = pd.concat([dfcolumns,dfscores_mutual],axis=1)
#featureScores_chi = pd.concat([dfcolumns,dfscores_chi],axis=1)
#
##naming the dataframe columns
#featureScores_mutual.columns = ['Specs','Score']  
#featureScores_chi.columns = ['Specs','Score'] 
#print(featureScores_mutual.nlargest(10,'Score'))
#print(featureScores_chi.nlargest(10,'Score'))
#



