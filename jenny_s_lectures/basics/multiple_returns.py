import statistics
def mean_mode_medain(list):
    return [statistics.mean(list),statistics.mode(list),statistics.median(list)]
a,b,c=mean_mode_medain([3,5,45,3,2,1,89])
print(f"mean is {a}\nmode is {b}\nmedian is {c}")