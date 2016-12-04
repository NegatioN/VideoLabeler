import numpy as np
import imageio
import argparse
import sys
import pdb


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", type=int, default=0, help="When should labeling start?")
parser.add_argument("-e", "--end", type=int, help="When do you want labeling to end?")
parser.add_argument("-p", "--path", help="Path to video-file")
#parser.add_argument("-f", "--format", default="ffmpeg", help="Format to decode video with")

options = parser.parse_args()

def main():

    #TODO input should be seconds?
    #TODO make option for saving files in separate folders based on label
    #TODO make option to save as pickle / data-file with id associated to images processed.
    #TODO check how many frames of video are actually present, and stop before end to avoide crash?

    filename = 'testdata/cockatoo.mp4'
    savefolder = 'output'
    video_reader = imageio.get_reader(filename,  'ffmpeg')

    metadata = video_reader.get_meta_data()
    fps = metadata['fps']

    total_frames = metadata['nframes']

    start_frame = int(options.start * fps)  # Should math floor.
    end_frame = int(options.end * fps) if options.end else total_frames

    #pdb.set_trace()

    #TODO frame-spectrum cannot be lower than 0 or higher than total_frames.

    for index in range(end_frame-start_frame):
        frame_num = start_frame + index
        # If frame above timestamp we care about.
        video_frame = video_reader.get_data(frame_num)
        print('Mean of frame %i is %1.1f' % (frame_num, video_frame.mean()))
        imageio.imwrite('{}/{}.jpg'.format(savefolder, frame_num), video_frame)

    video_reader.close()


if __name__ == "__main__":
    sys.exit(main())