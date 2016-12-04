import numpy as np
import imageio
import pdb


#TODO input should be seconds?
#TODO make option for saving files in separate folders based on label
#TODO make option to save as pickle / data-file with id associated to images processed.
#TODO check how many frames of video are actually present, and stop before end to avoide crash?

filename = 'testdata/cockatoo.mp4'
savefolder = 'output'
video_reader = imageio.get_reader(filename,  'ffmpeg')

start_second = 5
metadata = video_reader.get_meta_data()
fps = metadata['fps']

total_frames = metadata['nframes']

start_frame = int(start_second * fps)  # Should math floor.
end_frame = total_frames

#pdb.set_trace()

#TODO frame-spectrum cannot be lower than 0 or higher than total_frames.

for index in range(end_frame-start_frame):
    frame_num = start_frame + index
    # If frame above timestamp we care about.
    video_frame = video_reader.get_data(frame_num)
    print('Mean of frame %i is %1.1f' % (frame_num, video_frame.mean()))
    imageio.imwrite('{}/{}.jpg'.format(savefolder, frame_num), video_frame)

video_reader.close()
