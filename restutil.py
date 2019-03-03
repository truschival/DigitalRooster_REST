

def read_slice(lst, kwargs):
    if len(kwargs) > 1:
        cnt = kwargs['length']
        offset = kwargs['offset']
        try:
            return lst[offset:offset+cnt],200
        except IndexError:
            return 404
    else:    
        return lst, 200