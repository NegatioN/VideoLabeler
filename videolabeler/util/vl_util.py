#!/usr/bin/env python
# -*- coding: utf-8
import imageio
import os
import logging


class Util:

    def __init__(self):
        self.logger = logging.getLogger('video_labeler')

    def frames(self, start, end=0, metadata=None):
        fps = metadata['fps']
        total_frames = metadata['nframes']

        start_frame = int(start * fps)  # Should math floor.
        end_frame = int(end * fps) if end != 0 and total_frames > end > start else total_frames
        self.logger.debug('Time start: {} end:{}, Frames start: {} end: {}'.format(start, end, start_frame, end_frame))
        return start_frame, end_frame


    def save_image(self, folder, index, image, filename):
        if os.path.isdir(folder) is False:
            os.makedirs(folder)
        imageio.imwrite('{}/{}-{}.jpg'.format(folder, filename, index), image)
        self.logger.info('Saved image={}-{} in {}'.format(filename, index, folder))


    def save_pickle(self, image_df, name):
        pass
