# resize a video
### If you need to simply resize your video to a specific size (e.g 320⨉240), you can use the scale filter in its most basic form:

ffmpeg -i input.avi -vf scale=320:240 output.avi


```python 
def resize_video_for_obdl(self):
    """
    the obdl need video has the size of 32 X
    """
    for i_video in range(len(video_test)):

        input_video = '/home/ml/Pami_reponse_SAUC/Data/for_obdl/cubemap_whole_raw_video/' + video_test[i_video] + '.avi'
        output_video = '/home/ml/Pami_reponse_SAUC/Data/for_obdl/cubemap_whole_for_obdl/' + video_test[i_video] + '.mp4'
        out_put_size = '1280:960'

        subprocess.call(['ffmpeg -i ' +  input_video + ' -vf scale=' + out_put_size + ' ' +output_video ], shell = True)
```
