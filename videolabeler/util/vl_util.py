#!/usr/bin/env python
# -*- coding: utf-8
import imageio
import os


def frames(start, end=0, metadata=None):
    fps = metadata['fps']
    total_frames = metadata['nframes']

    start_frame = int(start * fps)  # Should math floor.
    end_frame = int(end * fps) if end < total_frames and end != 0 and end > start else total_frames
    return start_frame, end_frame


def save_image(folder, name, image):
    if os.path.isdir(folder) is False:
        os.makedirs(folder)
    imageio.imwrite('{}/{}.jpg'.format(folder, name), image)
    print('Saved image={} in {}'.format(name, folder))


def save_pickle(image_df, name):
    pass
