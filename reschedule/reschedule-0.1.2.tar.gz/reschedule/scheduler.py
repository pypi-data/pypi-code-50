import math
import sys
import typing as t
from tqdm import tqdm

from .calendar_api import CalendarAPI
from .config import chunk_size
from .models import TaskStatus
from .task_parser import Task
from .time_helpers import (
    end_index_to_datetime,
    now_utc,
    parse_rfc_33339,
    start_index_to_datetime,
    utc_to_local,
)


def schedule_tasks(parse_tasks: t.List[Task]):
    cal_api = CalendarAPI()
    cal_tasks = cal_api.get_events_from_task_calendar()
    cal_task_ids = {c["id"] for c in cal_tasks}
    # tasks which are already deleted
    cancelled_cal_task_ids = {c["id"] for c in cal_tasks if c["status"] == "cancelled"}
    parse_task_ids = {c.id for c in parse_tasks}
    # delete tasks which are in calendar but not in parse tasks
    cal_task_ids_to_delete = cal_task_ids.difference(parse_task_ids).difference(
        cancelled_cal_task_ids
    )
    for event_id in cal_task_ids_to_delete:
        cal_api.delete_event_from_task_calendar(event_id)
    cancelled_cal_task_ids = cancelled_cal_task_ids.union(cancelled_cal_task_ids)

    # ids of tasks which are not finished
    unfinished_task_status_set = set([TaskStatus.UNSCHEDULED, TaskStatus.IN_PROGRESS])
    parse_task_ids_not_finished = set(
        [t.id for t in parse_tasks if t.status in unfinished_task_status_set]
    )

    # tasks in the future on the calendar
    future_cal_task_ids = {
        c["id"] for c in cal_tasks if parse_rfc_33339(c["end"]["dateTime"]) > now_utc()
    }

    # delete tasks in the future that are finished
    cal_task_ids_to_delete = future_cal_task_ids.difference(
        parse_task_ids_not_finished
    ).difference(
        cancelled_cal_task_ids
    )  # make an exception for already deleted tasks
    for event_id in cal_task_ids_to_delete:
        cal_api.delete_event_from_task_calendar(event_id)
    for tid in cal_task_ids_to_delete:
        cancelled_cal_task_ids.add(tid)

    # reschedule tasks which are not finished but are on the calendar
    task_ids_to_reschedule = parse_task_ids_not_finished.intersection(cal_task_ids)
    # schedule tasks ids which are not finished and are not on the calendar
    task_ids_to_schedule = parse_task_ids_not_finished.difference(cal_task_ids)
    task_id_dict = {t.id: t for t in parse_tasks}
    # list of all tasks to add to the calendar
    all_tasks_to_add_to_cal = [
        task_id_dict[tid] for tid in task_ids_to_reschedule.union(task_ids_to_schedule)
    ]
    # sort list by line number
    all_tasks_to_add_to_cal.sort(key=lambda t: t.line_number)
    # create a dict of id to task sorted by line number
    sorted_task_dict = {t.id: task_id_dict[t.id] for t in all_tasks_to_add_to_cal}

    # the actual scheduling
    day_offset = 0
    busy_array = cal_api.get_busy_array_for_day(day_offset)

    t = tqdm(total=len(sorted_task_dict), unit="events")
    while len(sorted_task_dict):
        try:
            # get the first possible free time
            start_free_index = busy_array.index(False)
        except ValueError:
            # no free time remaining so go to next day
            day_offset += 1
            busy_array = cal_api.get_busy_array_for_day(day_offset)
            continue

        try:
            # get the next busy time after the free time
            next_busy_index = busy_array.index(True, start_free_index)
        except ValueError:
            # no more busy times so we are free til the end of the day
            next_busy_index = len(busy_array)

        # free time in minutes
        free_time = (next_busy_index - start_free_index) * chunk_size
        task_ids_which_fit = filter(
            lambda tid: sorted_task_dict[tid].estimate <= free_time, sorted_task_dict
        )

        for fitting_task_id in task_ids_which_fit:
            fitting_task = sorted_task_dict[fitting_task_id]
            # schedule the task
            # get the start and end time
            task_end_index = start_free_index + math.ceil(
                fitting_task.estimate / chunk_size
            )
            start_time = start_index_to_datetime(start_free_index, day_offset)
            end_time = end_index_to_datetime(task_end_index, day_offset)
            # schedule the task
            cal_api.schedule_task(
                fitting_task.description,
                fitting_task.id,
                start_time,
                end_time,
                fitting_task.id in task_ids_to_reschedule,
            )
            # remove task from sorted task dict
            sorted_task_dict.pop(fitting_task.id)
            t.update(n=1)
            fitting_task.scheduled_date = utc_to_local(start_time).date()
            # mark allotted time as busy
            for i in range(start_free_index, task_end_index):
                busy_array[i] = True
            break
        else:
            # no task could be scheduled mark entire time as busy
            for i in range(start_free_index, next_busy_index):
                busy_array[i] = True
    t.close()

    error_mesage = ""
    for task in all_tasks_to_add_to_cal:
        if task.due_date is not None and task.scheduled_date is not None:
            if task.due_date <= task.scheduled_date:
                error_mesage += (
                    f'ERROR: failed to schedule the task "{task}" before due date.\n'
                )
                error_mesage += f"\tscheduled for {task.scheduled_date:%Y-%m-%d} and due on {task.due_date:%Y-%m-%d}\n"
                error_mesage += "FIX: break up long tasks into smaller ones or change priority by placing task earlier in file.\n"

    if error_mesage:
        sys.exit(error_mesage)
