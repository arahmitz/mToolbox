import maya.cmds as cmds
import math
from mtoolbox.utils.selection import get_selection

def make_rom():
    """
    Sets keyframes every 10 frames on the selected objects starting from frame 0 up to
    the current timeline end, inclusive. Intended for Range Of Movement testing.
    """
    start_time = int(cmds.playbackOptions(q=True, min=True))
    end_time = int(cmds.playbackOptions(q=True, max=True)) # grabs end of the selected timeline

    interval = 10

    first_key = int(math.ceil(start_time/interval) * interval)
    
    selection = get_selection("Make ROM")
    if selection:
        # has to end at end time + interval to include endtime
        for keyframe in range(start_time, end_time + interval, interval):
            cmds.currentTime(keyframe)
            cmds.setKeyframe(selection)