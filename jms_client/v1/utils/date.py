from datetime import datetime, timedelta


def handle_range_datetime(
        start, expired, formater='%Y-%m-%d %H:%M:%S', default_days=70 * 365
):
    try:
        start_time = datetime.strptime(start, formater)
    except ValueError:
        start_time = datetime.now()

    try:
        expired_time = datetime.strptime(expired, formater)
    except ValueError:
        expired_time = start_time + timedelta(days=default_days)
    start_time = start_time.strftime(formater)
    expired_time = expired_time.strftime(formater)
    return start_time, expired_time
