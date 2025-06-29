import random
from datetime import datetime, timedelta

def get_current_time() -> str:
    """ Static time for testing purposes """
    return datetime(2025, 6, 28, 10, 0, 0).strftime("%Y-%m-%d %H:%M:%S")
    

def get_dentist_availability(date_from: str, date_to: str) -> dict:
    """ Mocks an API call to retrieve the dentist's availability """
    return {
        "availability": [
            {"date": "2025-06-30", "time": "09:00"},
            {"date": "2025-06-30", "time": "13:30"},
            {"date": "2025-07-01", "time": "10:00"},
            {"date": "2025-07-02", "time": "11:00"},
            {"date": "2025-07-03", "time": "14:00"},
            {"date": "2025-07-04", "time": "09:30"},
            {"date": "2025-07-07", "time": "10:15"},
            {"date": "2025-07-08", "time": "15:00"},
            {"date": "2025-07-09", "time": "13:00"},
            {"date": "2025-07-10", "time": "11:45"},
            {"date": "2025-07-11", "time": "16:00"},
        ]
    }

def get_user_calendar(date_from: str, date_to: str) -> dict:
    start = datetime.strptime(date_from, "%Y-%m-%d %H:%M")
    end = datetime.strptime(date_to, "%Y-%m-%d %H:%M")

    result = {"availability": []}
    current = start

    # Define meeting labels for variety
    meeting_titles = [
        "Team sync", "Client call", "Design review", "1:1 check-in", 
        "Performance review", "Stand-up", "Tech talk", "Lunch break", 
        "Deep work", "Internal update"
    ]

    # Build busy event schedule dynamically
    busy_events = {}
    date_cursor = start.date()
    while date_cursor <= end.date():
        date_str = date_cursor.strftime("%Y-%m-%d")
        events = []
        if date_cursor.weekday() < 5:  # Weekdays only
            num_events = random.randint(6, 10)
            for _ in range(num_events):
                start_hour = random.choice(range(9, 16))  # Between 9:00 and 15:00
                start_minute = random.choice([0, 15, 30, 45])
                start_time = datetime.strptime(f"{start_hour}:{start_minute:02}", "%H:%M").time()
                end_time = (datetime.combine(datetime.today(), start_time) + timedelta(minutes=30)).time()
                message = random.choice(meeting_titles)
                events.append((start_time.strftime("%H:%M"), end_time.strftime("%H:%M"), message))
        else:
            # Maybe one short event on a weekend
            if random.random() < 0.3:
                events.append(("11:00", "11:30", "Brunch with friends"))
        busy_events[date_str] = events
        date_cursor += timedelta(days=1)

    # Build availability per 15-minute block
    current = start
    while current <= end:
        date_str = current.strftime("%Y-%m-%d")
        time_str = current.strftime("%H:%M")
        entry = {"date": date_str, "time": time_str}

        is_busy = False
        for busy_start, busy_end, message in busy_events.get(date_str, []):
            busy_start_dt = datetime.strptime(busy_start, "%H:%M").time()
            busy_end_dt = datetime.strptime(busy_end, "%H:%M").time()
            if busy_start_dt <= current.time() < busy_end_dt:
                entry["status"] = "busy"
                entry["message"] = message
                is_busy = True
                break

        if not is_busy:
            entry["status"] = "free"

        result["availability"].append(entry)
        current += timedelta(minutes=15)

    return result

def schedule_dental_appointment(date: str, time: str) -> dict:
    return {
        "status": "success",
        "message": f"Appointment scheduled successfully for {date} at {time}"
    }

def schedule_meeting_in_user_calendar(datetime: str, topic: str) -> dict:
    return {
        "status": "success",
        "message": f"Meeting \"{topic}\" at {datetime} has been successfully created in user's calendar."
    }

available_functions = {
    "get_current_time": get_current_time,
    "get_dentist_availability": get_dentist_availability,
    "get_user_calendar": get_user_calendar,
    "schedule_dental_appointment": schedule_dental_appointment,
    "schedule_meeting_in_user_calendar": schedule_meeting_in_user_calendar,
}