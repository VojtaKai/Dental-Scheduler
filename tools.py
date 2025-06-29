get_current_time_tool = {
    "type": "function",
    "function": {
        "name": "get_current_time",
        "description": "Returns a current time string in this format: YYYY-MM-DD HH:MM:SS",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        },
        "strict": True
    }
}

get_dentist_availability_tool = {
    "type": "function",
    "function": {
        "name": "get_dentist_availability",
        "description": "Retrieves the dentist's availability between two dates.",
        "parameters": {
            "type": "object",
            "properties": {
                "date_from": {
                    "type": "string",
                    "description": "Start date for availability range in YYYY-MM-DD HH:MM:SS format."
                },
                "date_to": {
                    "type": "string",
                    "description": "End date for availability range in YYYY-MM-DD HH:MM:SS format."
                }
            },
            "required": ["date_from", "date_to"],
            "additionalProperties": False
        },
        "strict": True
    }
}

get_user_calendar_tool = {
    "type": "function",
    "function": {
        "name": "get_user_calendar",
        "description": "Retrieves the user's availability between two datetime values.",
        "parameters": {
            "type": "object",
            "properties": {
                "date_from": {
                    "type": "string",
                    "description": "Start datetime in format YYYY-MM-DD HH:MM (24-hour)."
                },
                "date_to": {
                    "type": "string",
                    "description": "End datetime in format YYYY-MM-DD HH:MM (24-hour)."
                }
            },
            "required": ["date_from", "date_to"],
            "additionalProperties": False
        },
        "strict": True
    }
}


schedule_dental_appointment_tool = {
    "type": "function",
    "function": {
        "name": "schedule_dental_appointment",
        "description": "Schedules a dental appointment for a given date and time.",
        "parameters": {
            "type": "object",
            "properties": {
                "date": {
                    "type": "string",
                    "description": "Appointment date in YYYY-MM-DD format."
                },
                "time": {
                    "type": "string",
                    "description": "Appointment time in HH:MM 24-hour format."
                }
            },
            "required": ["date", "time"],
            "additionalProperties": False
        },
        "strict": True
    }
}

schedule_meeting_in_user_calendar_tool = {
    "type": "function",
    "function": {
        "name": "schedule_meeting_in_user_calendar",
        "description": "Schedules a meeting in the user's calendar at the specified datetime.",
        "parameters": {
            "type": "object",
            "properties": {
                "datetime": {
                    "type": "string",
                    "description": "Datetime for the meeting in format YYYY-MM-DD HH:MM (24-hour)."
                },
                "topic": {
                    "type": "string",
                    "description": "Topic of the meeting. It should be a short description of the meeting."
                }
            },
            "required": ["datetime", "topic"],
            "additionalProperties": False
        },
        "strict": True
    }
}


tools = [
    get_current_time_tool,
    get_dentist_availability_tool,
    get_user_calendar_tool,
    schedule_dental_appointment_tool,
    schedule_meeting_in_user_calendar_tool
]