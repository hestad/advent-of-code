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


def toRecord(rawRecord: str) -> Record:
    parts = rawRecord.strip().split('] ')
    recordTime = dateutil.parser.parse(parts[0][1:].strip())
    action = parts[1].strip()
    if "falls asleep" in action:
        return Record(recordTime, SleepState.FALLS_ASLEEP)
    if "wakes up" in action:
        return Record(recordTime, SleepState.WAKES_UP)
    if "begins shift" in action:
        return Record(recordTime, int(action.split('#')[1].split(' ')[0].strip()))
    print("Could not parse the raw record: " + rawRecord)
    exit(1)


records: List[Record] = []
with open('day4.txt') as f:
    for line in f:
        records.append(toRecord(line))

records.sort(key=lambda x: x.recordTime)

guard: Union[None, int] = None
fellAsleep: datetime = None
guards: Dict[int, List[int]] = {}
for record in records:
    event = record.recordEvent
    if type(event) is int:
        guard = event
        guards.setdefault(guard, [0] * 60)
    if guard is None: continue
    if event is SleepState.FALLS_ASLEEP and fellAsleep is None:
        fellAsleep = record.recordTime
    if event is SleepState.WAKES_UP and fellAsleep is not None:
        #print(f"Slept from {fellAsleep.minute} to {record.recordTime.minute}")
        for i in range(fellAsleep.minute, record.recordTime.minute):
            guards[guard][i] += 1
        fellAsleep = None

maxGuard = None
maxSum = -1
for key, value in guards.items():
    thesum = sum(value)
    if thesum > maxSum:
        maxSum = thesum
        maxGuard = key

print(f"Guard #{maxGuard}: {guards[maxGuard].index(max(guards[maxGuard])) * maxGuard}")

