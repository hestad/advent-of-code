from dataclasses import dataclass
from datetime import datetime
from enum import Enum, unique, auto
from typing import Union, List, Dict

import dateutil.parser


@unique
class SleepState(Enum):
    FALLS_ASLEEP = auto()
    WAKES_UP = auto()


@dataclass
class Record:
    # [1518-07-04 00:01]
    recordTime: datetime
    # falls asleep |  wakes up | Guard #[0-9]+ begins shift
    recordEvent: Union[SleepState, int]

    def __str__(self) -> str:
        return "When:" + str(self.recordTime) + ", Event: " + str(self.recordEvent)

    def __repr__(self) -> str:
        return self.__str__()


def to_record(raw_record: str) -> Record:
    parts = raw_record.strip().split('] ')
    record_time = dateutil.parser.parse(parts[0][1:].strip())
    action = parts[1].strip()
    if "falls asleep" in action:
        return Record(record_time, SleepState.FALLS_ASLEEP)
    if "wakes up" in action:
        return Record(record_time, SleepState.WAKES_UP)
    if "begins shift" in action:
        return Record(record_time, int(action.split('#')[1].split(' ')[0].strip()))
    print("Could not parse the raw record: " + raw_record)
    exit(1)


def sleep_dict() -> Dict[int, List[int]]:
    records: List[Record] = []
    with open('day4.txt') as f:
        for line in f:
            records.append(to_record(line))

    records.sort(key=lambda x: x.recordTime)

    guard: Union[None, int] = None
    fell_asleep: datetime = None
    guards: Dict[int, List[int]] = {}
    for record in records:
        event = record.recordEvent
        if type(event) is int:
            guard = event
            guards.setdefault(guard, [0] * 60)
        if guard is None: continue
        if event is SleepState.FALLS_ASLEEP and fell_asleep is None:
            fell_asleep = record.recordTime
        if event is SleepState.WAKES_UP and fell_asleep is not None:
            # print(f"Slept from {fell_asleep.minute} to {record.recordTime.minute}")
            for i in range(fell_asleep.minute, record.recordTime.minute):
                guards[guard][i] += 1
            fell_asleep = None
    return guards

def part1():
    guards = sleep_dict()
    maxGuard = None
    maxSum = -1
    for key, value in guards.items():
        thesum = sum(value)
        if thesum > maxSum:
            maxSum = thesum
            maxGuard = key
    return f"Guard #{maxGuard}: {guards[maxGuard].index(max(guards[maxGuard])) * maxGuard}"


def part2():
    guards = sleep_dict()
    maxGuard = None
    maxSum = -1
    for key, value in guards.items():
        thesum = max(value)
        if thesum > maxSum:
            maxSum = thesum
            maxGuard = key
    return f"Guard #{maxGuard}: {guards[maxGuard].index(max(guards[maxGuard])) * maxGuard}"


print("Day 4, part 1\n" + part1())
print("\nDay 4, part 2\n" + part2())
