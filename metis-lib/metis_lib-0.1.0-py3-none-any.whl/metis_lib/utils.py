from datetime import timedelta


def date_calculator(dt, target_days):
    start_dt = dt - timedelta(days=target_days + 2)
    return start_dt.strftime('%Y%m%d00')
