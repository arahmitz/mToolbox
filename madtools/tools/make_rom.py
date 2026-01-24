import maya.cmds as cmds
import math
from madtools.utils.selection import get_selection

def make_rom():
    """
    Sets keyframes every 10 frames on the selected objects,
    starting from the current timeline start up to the timeline end.

    - Aligns keys to interval
    - Preserves existing keys on the start frame
    """
    selection = get_selection("Make ROM")
    if not selection:
        return

    interval = 10
    start_time = int(cmds.playbackOptions(q=True, min=True)) # grabs the start of the selected timeline
    end_time = int(cmds.playbackOptions(q=True, max=True)) # grabs end of the selected timeline

    # align start time for next interval
    first_key = int(math.ceil(start_time/interval) * interval)

    # save last keyframe w/o overwriting previous keys
    if start_time < first_key:
        cmds.currentTime(start_time)
        cmds.setKeyframe(selection)
    
    if selection:
        # has to end at end time + interval to include endtime
        for keyframe in range(first_key, end_time + interval, interval):
            cmds.currentTime(keyframe)
            cmds.setKeyframe(selection)
            