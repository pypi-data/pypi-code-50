import re
from typing import Callable, List

from boiler import BoilerError, BoilerWarning
from boiler.definitions import activity_spec, ActivityType, actor_codes, ActorType
from boiler.models import Activity, ActivityList, Actor, Detection

# Ideally, we set this higher, but theoretically there could be a 3 frame track...
MAX_KEYFRAME_RATIO = 0.75


def validate_activity_actor_types(actor_string: str, activity_type: ActivityType) -> bool:
    pattern = activity_spec[activity_type]
    if pattern is not None:
        sorted_actor_string = ''.join(sorted(actor_string))
        pattern = f'^{pattern}$'
        result = re.match(pattern, sorted_actor_string)
        if result is None:
            raise BoilerWarning(
                (
                    f'activity spec validation failed for {activity_type.value}:'
                    f' {sorted_actor_string} found, {activity_spec[activity_type]} expected'
                )
            )
    return True


def validate_detection(detection: Detection):
    """
    * detections have 4 int corners
    * detection: top < bottom, left < right
    """
    box = detection.box
    if not (box.left < box.right):
        raise BoilerError('left ({box.left}) should be < right ({box.right})')
    if not (box.top < box.bottom):
        raise BoilerError('top ({box.top}) should be < bottom ({box.bottom})')


def validate_actor(actor: Actor, detection_validator: Callable = validate_detection):
    keyframe_count = 0
    last = None
    for detection in actor.detections:
        if last and detection.frame < last.frame:  # type: ignore
            raise BoilerError(
                f'detection_frame={detection.frame} was not greater than {last.frame}'
            )
        last = detection
        try:
            detection_validator(detection)
        except BoilerError as err:
            raise BoilerError(f'detection_frame={detection.frame}') from err
        if detection.keyframe:
            keyframe_count += 1
    if not (len(actor.detections) >= 2):
        raise BoilerError('actor must have at least a start and end frame')

    # TODO: add interpolated frame detection https://gitlab.com/diva-mturk/stumpf-diva/issues/30
    # failed_frame = actor.pruned()
    # assert failed_frame < 0, f'frame={failed_frame} interpolation detected on keyframe'

    if not actor.detections[0].frame <= actor.begin:
        raise BoilerError('actor must have first detection <= activity begin frame')
    if not (actor.detections[0].keyframe):
        raise BoilerError('first detection must be keyframe')
    if not (actor.detections[-1].frame >= actor.end):
        raise BoilerError('actor must have last detection >= activity end frame')
    if not (actor.detections[-1].keyframe):
        raise BoilerError('last detection must be keyframe')

    total_frames = actor.detections[-1].frame - actor.detections[0].frame + 1
    if not (keyframe_count <= MAX_KEYFRAME_RATIO * total_frames):
        raise BoilerError(
            f'keyframe density {round(keyframe_count / total_frames * 100)}%'
            f' higher than {round(MAX_KEYFRAME_RATIO * 100)}%'
        )


def validate_activity(
    activity: Activity,
    actor_validator: Callable = validate_actor,
    detection_validator: Callable = validate_detection,
):
    """
    * actors involved are appropriate for activity type
    * actors framerange is within activity framerange
    """
    actor_string = ''
    activity_type = ActivityType(activity.activity_type)
    for actor in activity.actors:
        try:
            actor_validator(actor, detection_validator=detection_validator)
        except BoilerError as err:
            raise BoilerError(f'actor_id={actor.actor_id}') from err
        actor_type = ActorType(actor.actor_type)
        actor_string += actor_codes[actor_type]
        if not (activity.begin <= actor.begin <= activity.end):
            raise BoilerError('actor must begin in range')
        if not (activity.begin <= actor.end <= activity.end):
            raise BoilerError('actor must end in range')
    validate_activity_actor_types(actor_string, activity_type)


def validate_activities(
    activity_list: ActivityList,
    activity_validator: Callable = validate_activity,
    actor_validator: Callable = validate_actor,
    detection_validator: Callable = validate_detection,
):
    warnings: List[Exception] = []
    fatals: List[Exception] = []
    if len(activity_list) == 0:
        fatals.append(BoilerError('found no activities to validate'))
    for activity in activity_list:
        try:
            activity_validator(
                activity, actor_validator=actor_validator, detection_validator=detection_validator,
            )
        except BoilerWarning as err:
            new_err = BoilerError(f'activity_id={activity.activity_id}')
            new_err.__cause__ = err
            warnings.append(new_err)
        except Exception as err:
            new_err = BoilerError(f'activity_id={activity.activity_id}')
            new_err.__cause__ = err
            fatals.append(new_err)
    return warnings, fatals
