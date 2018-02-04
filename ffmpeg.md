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

## 合成视频：

ffmpeg -r 帧率(一般25） -i path_of_input%03.png -b 码率（改善模糊度） -codec mpeg4 path_of_output将多个图片合成为视频

如：ffmpeg -r 25 -i F:\VR\过程图\A380\t=%03d.png -b 2000k -codec mpeg4 F>\VR\A380.mp4

```python 
def from_image_to_video(self):
    'convert the cubemap_face image to video'

    frame_rate = '25'

    for i_video in range(len(video_test)):

        for i_sub_image in range(1, 7):
            image_path = '/home/ml/Pami_reponse_SAUC/Data/for_obdl/cubemap_face_steps/' + video_test[i_video] + '_' +  '%d' + '_' + '%04d'%i_sub_image + '.jpg'
            out_put_path = '/home/ml/Pami_reponse_SAUC/Data/for_obdl/cubemap_face_6_video/' + video_test[i_video] + '_' + '%04d'%i_sub_image + '.mp4'

            subprocess.call(['ffmpeg -r ' + frame_rate +  ' -i ' + image_path +  ' -b 2000k ' + ' -codec mpeg4 out_put_path], shell = True)
            
```

