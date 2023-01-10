from read_data import fromJson


def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    messages=data['messages']
    k=0
    m=0
    n=0
    for i in messages:
        str1=i['date']
        if str1[5:7]=='09':
            k+=1
        if str1[5:7]=='10':
            m+=1
        if str1[5:7]=='11':
            n+=1
    return {'Sentabr': k,'Oktabr':m, 'Noyabr':n}
x=fromJson('result.json')
print(get_post_per_month(x))
