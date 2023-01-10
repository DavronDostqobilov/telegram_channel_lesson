from read_data import fromJson

def get_number_of_posts(data:dict)->int:
    """
    Return the number of posts for a given dictionary

    Args:
        data (dict): a dictionary of posts

    Returns: 
        int: the number of posts for the given dictionary
    """
    messages=data['messages']
    k=0
    for i in messages:
            k+=1
    return k
x=fromJson('result.json')
print(get_number_of_posts(x))