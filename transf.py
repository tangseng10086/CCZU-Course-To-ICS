from icalendar import Calendar,Event
import openpyxl
from datetime import datetime,timedelta
import uuid
# 配置时间

# 导入需要转换的文件
wb=openpyxl.load_workbook('cczu.xlsx')
sheet=wb.worksheets[0]

# 配置天
term_start_time=datetime(2026,3,2)
def get_target_time(week,day):
    global target_time
    # 计算目标时间
    target_time=term_start_time+timedelta(days=(week-1)*7+(day-1))
    
# 配合天偏移量
# 配具体时间
time_map={
    1:(8,0,8,40),
    2:(8,45,9,25),
    3:(9,45,10,25),
    4:(10,35,11,15),
    5:(11,20,12,0),
    6:(13,30,14,10),
    7:(14,15,14,55),
    8:(15,15,15,55),
    9:(16,0,16,40),
    10:(18,30,19,10),
    11:(19,15,19,55),
    12:(20,5,20,45)
}
# 编辑第一节课的代码块
cal=Calendar()
def create_course_event(title, desc, loc, start_dt, end_dt):
        e = Event()
        e.add('summary', title)
        e.add('dtstart', start_dt)
        e.add('dtend', end_dt)
        e.add('location', loc)
        e.add('description', desc)
        e.add('uid', str(uuid.uuid4()))
        return e # 返回这个写好的“小块”
def create_day(week,j):
    # 遍历出一天的课程内容
    sum=[]
    for row in sheet.iter_rows(min_row=2,max_row=24,min_col=j,max_col=j):
        for cell in row:
            # print(cell.row)
            # print(cell.value)
            # 对应的节次=对应的row/2
            if cell.row%2==0:
                sum.append(cell.value)
    # print(sum)
    for n in range(len(sum)):
        # print(len(sum))
        course_order=n+1
        # print(course_order)
        h_start,m_start,h_end,m_end=time_map[course_order]
        start_dt=target_time.replace(hour=h_start,minute=m_start)
        end_dt=target_time.replace(hour=h_end,minute=m_end)
        if sum[n]!=None:
            con=sum[n].split(' ')
            # print(con)
            # print(con[4])
            if len(con)==6:
                con[4]=con[4].rstrip(',')
                week_range1=con[4].split('-')
                start_week1=int(week_range1[0])
                end_week1=int(week_range1[1])
                # 筛选一下周次
                if (con[3]=='单' or con[3]==' ') and week%2==1:
                    if week>=start_week1 and week<=end_week1:
                        a=create_course_event(con[0],con[1]+' '+con[3]+' '+con[4],con[2],start_dt,end_dt)
                        cal.add_component(a)
                else:
                    if week>=start_week1 and week<=end_week1:
                        a=create_course_event(con[0],con[1]+' '+con[4],con[2],start_dt,end_dt)
                        cal.add_component(a)
            elif len(con)==12:
                con[4]=con[4].rstrip(',')
                con[0+5]=con[0+5].lstrip('/<br/>')
                con[4+5]=con[4+5].rstrip(',')
                if con[3]=='单' and week%2==1:
                    week_range2=con[4].split('-')
                    start_week2=int(week_range2[0])
                    end_week2=int(week_range2[1])
                    if week>=start_week2 and week<=end_week2:
                        a=create_course_event(con[0],con[1]+' '+con[3]+' '+con[4],con[2],start_dt,end_dt)
                        cal.add_component(a)
                elif con[3+5]=="双" and week%2==0:
                    week_range3=con[4+5].split('-')
                    start_week3=int(week_range3[0])
                    end_week3=int(week_range3[1])
                    if week>=start_week3 and week<=end_week3:
                        a=create_course_event(con[0+5],con[1+5]+' '+con[3+5]+' '+con[4+5],con[2+5],start_dt,end_dt)
                        cal.add_component(a)
                else:
                    week_range4=con[4].split("-")
                    start_week4=int(week_range4[0])
                    end_week4=int(week_range4[1])
                    week_range5=con[4+5].split("-")
                    start_week5=int(week_range5[0])
                    end_week5=int(week_range5[1])
                    if week>=start_week4 and week<=end_week4:
                        a=create_course_event(con[0],con[1]+' '+con[3]+' '+con[4],con[2],start_dt,end_dt)
                        cal.add_component(a)
                    if week>=start_week5 and week<=end_week5:
                        a=create_course_event(con[0+5],con[1+5]+' '+con[3+5]+' '+con[4+5],con[2+5],start_dt,end_dt)
                        cal.add_component(a)
            elif len(con)==3:
                con[2]=con[2].rstrip(',')
                week_range6=con[2].split('-')
                start_week6=int(week_range6[0])
                end_week6=int(week_range6[1])
                if week>=start_week6 and week<=end_week6:
                    a=create_course_event(con[0],con[2],con[1],start_dt,end_dt)
                    cal.add_component(a)
            with open('mcl.ics','wb') as f:
                    f.write(cal.to_ical())
for j in range(1,19):
    for i in range(1,8):
        get_target_time(j,i)
        get_target_time(j,i)
        create_day(j,i+2)
        print(f'第{j}周第{i}天课表写入成功')