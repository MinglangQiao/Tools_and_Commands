# runnewdata.md
ispc: 用来判断当前的电脑系统是否是windows系统，是返回1，不是返回0

filesep: 用于返回当前平台的目录分隔符，Windows是反斜杠(\)，Linux是斜杠(/)


### 跑程序的顺序
1、run_new_data1（自动生成yuv）

2、run_new_data2(路径， cfg + yuv， 修改图片尺寸为64的倍数)

3、run_new_data3


#### 准备mat文件格式

VideoNameList.mat: 包含所有的video_name

每个video的Data.mat： 包含num_frames, fps, w, h

