import os
import shutil
#先解压tiny-imagenet-200.zip
#root_path是解压后所在文件夹
root_path='tiny-imagenet-200'
if os.path.exists(path=os.path.join(root_path,'tiny-imagenet-200_modified'))==False:
    os.makedirs(name=os.path.join(root_path,'tiny-imagenet-200_modified'))
if os.path.exists(path=os.path.join(root_path,'tiny-imagenet-200_modified','train'))==False:
    os.makedirs(name=os.path.join(root_path,'tiny-imagenet-200_modified','train'))
if os.path.exists(path=os.path.join(root_path,'tiny-imagenet-200_modified','val'))==False:
    os.makedirs(name=os.path.join(root_path,'tiny-imagenet-200_modified','val'))
#wnids.txt里包含所有的标签种类，读取wnids.txt
with open (file=os.path.join(root_path,'tiny-imagenet-200','wnids.txt'),mode='r') as fwnids:
    nxxxxxxxx_list=fwnids.read().splitlines()
print('共读取到标签数量%d' %len(nxxxxxxxx_list))
#print(nxxxxxxxx_list)
#wnids.txt里包含所有的val的标签，读取val_annotations.txt
with open (file=os.path.join(root_path,'tiny-imagenet-200','val','val_annotations.txt'),mode='r') as fannotations:
    annotations_list=fannotations.read().splitlines()
print('共读取到val数量%d' %len(annotations_list))
#print(annotations_list)
#在train与val目录里分别创建各标签文件夹，文件夹名从wnids.txt里读取，按标签创建文件夹，复制train图片
for nxxxxxxxx in nxxxxxxxx_list:
    if os.path.exists(path=os.path.join(root_path,'tiny-imagenet-200_modified','train',nxxxxxxxx))==False:
        os.makedirs(name=os.path.join(root_path,'tiny-imagenet-200_modified','train',nxxxxxxxx))
    for file in os.listdir(os.path.join(root_path,'tiny-imagenet-200','train',nxxxxxxxx,'images')):
        shutil.copy(src=os.path.join(root_path,'tiny-imagenet-200','train',nxxxxxxxx,'images',file),dst=os.path.join(root_path,'tiny-imagenet-200_modified','train',nxxxxxxxx)) 
    if os.path.exists(path=os.path.join(root_path,'tiny-imagenet-200_modified','val',nxxxxxxxx))==False:
        os.makedirs(name=os.path.join(root_path,'tiny-imagenet-200_modified','val',nxxxxxxxx))
    print('完成创建目录%s，复制其train图片。' %(nxxxxxxxx))
#根据val_annotations.txt里各val图片的标签，将图片分别复制至带有标签名的文件夹
for line in annotations_list:
    pieces = line.strip().split()
    shutil.copy(src=os.path.join(root_path,'tiny-imagenet-200','val','images',pieces[0]),dst=os.path.join(root_path,'tiny-imagenet-200_modified','val',pieces[1]))

#统计各标签下的train与val图片数量
with open (file=os.path.join(root_path,'tiny-imagenet-200_modified','count.txt'),mode='a+') as fcount:
    total_train=total_val=0
    for nxxxxxxxx in nxxxxxxxx_list:
        nxxxxxxxx_train=len(os.listdir(os.path.join(root_path,'tiny-imagenet-200_modified','train',nxxxxxxxx)))
        nxxxxxxxx_val=len(os.listdir(os.path.join(root_path,'tiny-imagenet-200_modified','val',nxxxxxxxx)))
        total_train=total_train+nxxxxxxxx_train
        total_val=total_val+nxxxxxxxx_val
        fcount.write('%s\t%d\t%d\n' %(nxxxxxxxx,nxxxxxxxx_train,nxxxxxxxx_val))
        print('%s\t%d\t%d' %(nxxxxxxxx,nxxxxxxxx_train,nxxxxxxxx_val))


