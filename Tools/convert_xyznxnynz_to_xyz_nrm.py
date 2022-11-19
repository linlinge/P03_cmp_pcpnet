import pandas as pd
import numpy as np
def list_all_files(rootdir, pattern="", is_contain_pattern=True, is_recurse=True):
    import os
    _files = []

    #列出文件夹下所有的目录与文件
    list_file = os.listdir(rootdir)
    
    for i in range(0,len(list_file)):
        # 构造路径
        path = os.path.join(rootdir,list_file[i])

        # 判断路径是否是一个文件目录或者文件
        # 如果是文件目录，继续递归        
        if is_recurse==True and os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            if pattern=="":
                _files.append(path)
            else:
                if is_contain_pattern==True: 		# 假如想匹配包含该字符串的所有文件
                    if path.find(pattern)!=-1:
                        _files.append(path)
                else:
                    if path.find(pattern)==-1:	# 假如想匹配不包含该字符串的所有文件
                        _files.append(path)
                
    return _files

path_of_raw="/home/i9/experiment_nc/stanford/Disturbed/xyz_nrm/not_close"
fs=list_all_files(path_of_raw, is_contain_pattern="xyz")
for f in fs:
    df=pd.read_csv(f, header=None, sep=" ")
    dat= np.asarray(df.values)
    
    xyz=dat[:, 0:3]
    pd.DataFrame(xyz).to_csv("{}.xyz".format(f.split(".")[0]), header=None, index=None, sep=" ")
    nrm=dat[:,3:6]
    pd.DataFrame(nrm).to_csv("{}.normals".format(f.split(".")[0]), header=None, index=None, sep=" ")
