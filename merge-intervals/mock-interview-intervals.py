from math import e
from typing import List, TypedDict

class TechInterval(TypedDict):
    start: int
    end: int
    tech_id: str


def find_available_slots(
    shifts: List[TechInterval],
    appointments: List[TechInterval],
    non_job_appointments: List[TechInterval],
) -> List[TechInterval]:
    # single tech case
    single_tech_id = shifts[0]["tech_id"]
    all_appointments = appointments + non_job_appointments
    # get start and end intervals:
    intervals = []
    for interval in all_appointments:
        start = interval["start"]
        end = interval["end"]
        intervals.append([start, end])
    print(intervals)
    intervals.sort(key=lambda x: x[0])
    open_slots = []
    start_work = shifts[0]["start"]
    end_work = shifts[0]["end"]
    for interval in intervals:
        app_start = interval[0]
        app_end = interval[1]
        if start_work < app_start:
            open_slots.append([start_work, app_start])
            start_work = app_end
        else:
            start_work = app_end
    # make sure end interval is accounted for
    if start_work != end_work:
        open_slots.append([start_work, end_work])
    print(open_slots)
    return [{"start": s, "end": e, "tech_id": single_tech_id} for (s, e) in open_slots]





# ---------------- TEST CASES ----------------
def run_tests():
    tests = [
        {
            "name": "Example 1 — single tech",
            "shifts": [{"start": 9, "end": 17, "tech_id": "t1"}],
            "appointments": [{"start": 10, "end": 11, "tech_id": "t1"}],
            "non_job_appointments": [{"start": 12, "end": 14, "tech_id": "t1"}],
            "expected": [
                {"start": 9, "end": 10, "tech_id": "t1"},
                {"start": 11, "end": 12, "tech_id": "t1"},
                {"start": 14, "end": 17, "tech_id": "t1"},
            ],
        },
        {
            "name": "Example 2 — two techs",
            "shifts": [
                {"start": 9, "end": 17, "tech_id": "tech1"},
                {"start": 10, "end": 16, "tech_id": "tech2"},
            ],
            "appointments": [
                {"start": 10, "end": 12, "tech_id": "tech1"},
                {"start": 14, "end": 15, "tech_id": "tech1"},
                {"start": 11, "end": 12, "tech_id": "tech2"},
            ],
            "non_job_appointments": [
                {"start": 13, "end": 14, "tech_id": "tech1"},
                {"start": 14, "end": 15, "tech_id": "tech2"},
            ],
            "expected": [
                {"start": 9, "end": 10, "tech_id": "tech1"},
                {"start": 12, "end": 13, "tech_id": "tech1"},
                {"start": 15, "end": 17, "tech_id": "tech1"},
                {"start": 10, "end": 11, "tech_id": "tech2"},
                {"start": 12, "end": 14, "tech_id": "tech2"},
                {"start": 15, "end": 16, "tech_id": "tech2"},
            ],
        },
    ]

    for t in tests:
        result = find_available_slots(t["shifts"], t["appointments"], t["non_job_appointments"])
        print(f"\n{t['name']}")
        print("Expected:", t["expected"])
        print("Got     :", result)
        print("Pass    :", result == t["expected"])


if __name__ == "__main__":
    run_tests()


