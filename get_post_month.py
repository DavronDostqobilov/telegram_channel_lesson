from read_data import fromJson


def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    messages=data['messages']
    k=0
    for i in messages:
        str1=i['date']
        if str1[5:7]==str(month):
            k+=1
    return k
x=fromJson('result.json')
print(get_post_month(x,10))