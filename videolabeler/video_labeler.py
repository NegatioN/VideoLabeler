#!/usr/bin/env python
# -*- coding: utf-8

import numpy as np
import imageio
import argparse
import sys
import pdb
from videolabeler import util as vl

modes = ['folder', 'pickle']

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", type=int, default=0, help="When should labeling start?")
parser.add_argument("-e", "--end", type=int, help="When do you want labeling to end?")
parser.add_argument("-l", "--label", required=True, help="What to label this section of the clip as?")
parser.add_argument("-p", "--path", help="Path to video-file")
parser.add_argument("-m", "--mode", default='folder', choices=modes, help="Save-mode")
#parser.add_argument("-f", "--format", default="ffmpeg", help="Format to decode video with")

options = parser.parse_args()

def main():

    #TODO make option for saving files in separate folders based on label
    #TODO make option to save as pickle / data-file with id associated to images processed.
    #TODO check how many frames of video are actually present, and stop before end to avoide crash?
    #TODO verbose percentage completion etc?
    #TODO support taking in arrays of labels and timings?

    filename = 'testdata/cockatoo.mp4'
    savefolder = 'output' if options.mode is modes[1] else 'output/{}'.format(options.label)
    video_reader = imageio.get_reader(filename,  'ffmpeg')

    start_frame, end_frame = vl.frames(options, video_reader.get_meta_data())

    for index in range(end_frame-start_frame):
        frame_num = start_frame + index
        video_frame = video_reader.get_data(frame_num)
        vl.save_image(savefolder, frame_num, video_frame)

    video_reader.close()


if __name__ == "__main__":
    sys.exit(main())
