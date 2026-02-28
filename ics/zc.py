from icalendar import Calendar,Event
import openpyxl
from datetime import datetime,timedelta
import uuid
# 配置时间
term_start_time=datetime(2026,3,2)
cal=Calendar()
event=Event()
def get_target_time(week):
    global target_time
    # 计算目标时间
    start=term_start_time+timedelta(days=(week-1)*7)
    end=start+timedelta(days=7)
    return start,end
    
def create_course_event(title, start_dt,end_dt):
        e = Event()
        e.add('summary', title)
        e.add('dtstart', start_dt)
        e.add('dtend', end_dt)
        e.add('uid', str(uuid.uuid4()))
        return e

for i in range(1,19):
    start,end=get_target_time(i)
    a=create_course_event(f'第{i}周',start,end)
    cal.add_component(a)
    with open('zc.ics','wb') as f:
         f.write(cal.to_ical())
