# dvc_mlops
MLOPS DVC(Data Version Control)


# pip install scikit-learn
# pip install dvc 
1.) Now we do "dvc init" (Creates .dvcignore, .dvc)
2.) Create dvc folder to store data . mkdir experiment_data
3.) now we do tell dvc to store data to "dvc remote add -d myremote experiment_data"
4.) next "dvc add data/"
5.) "dvc status"  and now "dvc commit" and then "dvc push"
6.) Again change in code