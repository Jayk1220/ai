def safe_index(lst, item):
    """첫번쨰 매개변수 lst에서 item 요소가 있는 index를 반환, 
    item요소가 없으면 -1반환"""
    if item in lst:
        return lst.index(item)
    return -1