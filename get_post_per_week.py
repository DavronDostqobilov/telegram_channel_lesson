import datetime
from read_data import fromJson

def get_post_per_week(data:dict,month:int)->dict:
    """
    Return the number of posts for each week of a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        dict: a dictionary with the number of posts for each week.
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

        month_data.setdefault(week_day, 0)
        month_data[week_day]+=1
        


    return month_data
x=fromJson('result.json')
print(get_post_per_week(x,10))

