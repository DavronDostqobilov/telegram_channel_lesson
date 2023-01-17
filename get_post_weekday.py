import datetime
from read_data import fromJson
def get_post_weekday(data:dict,week:int)->dict:
    """
    Return the number of posts for each weekday
    args:
        data: a dictionary of posts
    returns: a dictionary with the number of posts for each weekday
    """
    month_data={}
    messages=data['messages']
    for i in messages:
        str1=i['date'].split('T')[0]
        str2=str1.split('-')
        
        year=int(str2[0])
        month=int(str2[1])
        day=int(str2[2])

        date=datetime.date(year, month, day)
        week_day=date.weekday()
        text=date.strftime('%A')

        if week==week_day:
            month_data.setdefault(text, 0)
            month_data[text]+=1
        


    return month_data
x=fromJson('result.json')
print(get_post_weekday(x,6))