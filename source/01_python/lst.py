#def safe_index(lst, item):
#    """첫번쨰 매개변수 lst에서 item 요소가 있는 index를 반환, 
#    item요소가 없으면 -1반환"""
#    if item in lst:
#        return lst.index(item)
#    return -1


def safe_index(lst, item, start = 0):
    '''
    첫번째 매개변수 lst : 나열 가능한 자료(list, tuple)
    두번째 매개변수 item: 리스트, 튜플에서 찾을 데이터
    세번째 매개변수 start: 몇번째 인덱스부터 찾을지 index 수(기본값:0)
    '''

    return lst.index(item, start) if item in lst[start:]else -1
    
    
#    if item in lst[start:]:
#        return lst.index(item, start) #start번째 부터 item이 있는 index를 반환
#    return -1

    