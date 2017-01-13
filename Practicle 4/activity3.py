__author__ = 'jc458537'

def list_avg(L):
    try:
        avg = sum(L)/len(L)
    except TypeError:
        print('Not all elements are numeric')
        return None
    except ZeroDivisionError:
        print('Empty list')
        return None
    except:
        print('Unknown error!')
        return None
    return avg
print(list_avg([]))
print(list_avg([1, "a", 3]))
