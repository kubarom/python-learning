from datetime import datetime

christmas = datetime(year=2023, month=12, day=25)
birthday = datetime(year=2024, month=3, day=4)

#timedelta is type for diff
delta = birthday - christmas
print("There are",delta.days,"days between Christmas and your birthday.")

now = datetime.today()
print(now)