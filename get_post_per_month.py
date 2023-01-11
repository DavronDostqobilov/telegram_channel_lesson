from read_data import fromJson


def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    month_data={}
    messages=data['messages']

    for i in messages:
        str1=i['date'].split('T')[0]
        str1=str1.split('-')[1]

        month_data.setdefault(str1, 0)
        month_data[str1]+=1



    return month_data
x=fromJson('result.json')
print(get_post_per_month(x))
