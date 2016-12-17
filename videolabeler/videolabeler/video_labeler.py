#!/usr/bin/env python
# -*- coding: utf-8
import sys
import argparse
import logging
import imageio
import ntpath
from videolabeler.util import vl_util

modes = ['folder', 'pickle']

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", type=int, default=0, help="When should labeling start?")
parser.add_argument("-e", "--end", type=int, help="When do you want labeling to end?")
parser.add_argument("-l", "--label", required=True, help="What to label this section of the clip as?")
parser.add_argument("-p", "--path", required=True, help="Path to video-file")
parser.add_argument("-m", "--mode", default='folder', choices=modes, help="Save-mode")
parser.add_argument("-st", "--step", type=float, default=1, help="Number of frames to sample per second of video")
parser.add_argument("-v", "--verbose", type=bool, default=False, help="Output debug-info?")
parser.add_argument("-f", "--format", default="ffmpeg",
                    help="Format to decode video with. List of options at http://imageio.readthedocs.io/en/latest/formats.html")

options = parser.parse_args()

# Setup logging
logger = logging.getLogger('video_labeler')
ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
if options.verbose:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

util = vl_util.Util()


def main():
    # TODO support taking in arrays of labels and timings?
    # TODO option to save as grayscale images. require significantly less disk-space / memory to hold.
    filepath = options.path
    filename = path_leaf(filepath)[:-4]
    savefolder = 'output' if options.mode == modes[1] else 'output/{}'.format(options.label)

    with imageio.get_reader(filepath, format=options.format) as video_reader:
        metadata = video_reader.get_meta_data()
        start_frame, end_frame = util.frames(options.start, options.end, metadata)
        frame_num = start_frame
        step = int(metadata['fps'] / options.step)
        num_frames = 0
        while frame_num <= end_frame:
            video_frame = video_reader.get_data(frame_num)
            if options.mode == modes[1]:
                util.add_image_data(video_frame, options.label)
            elif options.mode == modes[0]:
                util.save_image(savefolder, frame_num, video_frame, filename)
            frame_num += step
            num_frames += 1
    if options.mode == modes[1]:
        util.save_pickle(savefolder, options.label)
    logger.info('Labeled {} frames as {}'.format(num_frames, options.label))


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


if __name__ == "__main__":
    sys.exit(main())
