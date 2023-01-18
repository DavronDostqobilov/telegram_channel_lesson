import json
def fromJson(file_path: str)->dict:
    """
    This function will read the json file and return the data as a dictionary.
    
    Parameters:
        file_path (str): Path of the file to be read
    Returns:
        dict: Dictionary containing the data of the json file.
    
    """
    f=open(file_path, encoding='UTF8')
    a=f.read()
    ans=json.loads(a)
    return ans
print(fromJson('result.json'))
