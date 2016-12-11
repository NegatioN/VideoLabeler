[![Build Status](https://travis-ci.org/NegatioN/VideoLabeler.svg?branch=master)](https://travis-ci.org/NegatioN/VideoLabeler)

# Video Labeler

This is meant to be a handy program to label data from a video.

Individuals do not have as many resources to label data as organizations, and will have to take shortcuts to achieve results.

My hope is that this can help me, and others generate interesting labeled datasets from videos. This can be valuable if
the data you're seeking is usually protected heavily by copyright. You can instead generate it locally and train on it there.

### Example usage:

(after running `python setup.py install`)

```videolabeler --path $MY_VIDEO_FILE_PATH --start $MY_START_TIME --end $MY_END_TIME --label $MY_LABEL_VALUE```