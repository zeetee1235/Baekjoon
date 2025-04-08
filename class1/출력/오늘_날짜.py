from datetime import datetime, timezone, timedelta

korea_timezone = timezone(timedelta(hours=9))
korea_today = datetime.now(korea_timezone).date()
print(korea_today)