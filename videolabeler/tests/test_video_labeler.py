#!/usr/bin/env python
# -*- coding: utf-8
from videolabeler.util import vl_util

#TODO make fixtures
total_frames = 10000
metadata = {'nframes': total_frames, 'fps': 24.886}


class TestVideoLabeler:
    def test_frames_nonintegerinput_should_floor(self):
        end_time = 10
        start_frame, end_frame = vl_util.frames(0, end_time, metadata=metadata)
        assert start_frame == 0
        assert end_frame == 248

    def test_frames_too_high_input_limited(self):
        end_time = 200000
        start_frame, end_frame = vl_util.frames(0, end_time, metadata=metadata)
        assert start_frame == 0
        assert end_frame == total_frames

    def test_frames_end_not_set_get_max(self):
        start_frame, end_frame = vl_util.frames(0, metadata=metadata)
        assert start_frame == 0
        assert end_frame == total_frames

    def test_frames_end_never_lower_than_start(self):
        start_frame, end_frame = vl_util.frames(5, 4, metadata=metadata)
        assert start_frame == int(5*metadata['fps'])
        assert end_frame == total_frames
