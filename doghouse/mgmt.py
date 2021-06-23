import sys
import json

def estimate_food(jsondata):
    result = ''
    error = ''
    dogdata = json.loads(jsondata.lower())
    foodkey = None
    for k in [k for k in dogdata.keys() if k not in ['small','medium','large']]:
        if 'remain' in k or 'left' in k or 'food' in k:
            foodkey = k
        else:
            result = result + "Found extra data: "+k+": "+str(dogdata[k])+'\n'
    if foodkey is None:
        result = result + "No entry for leftover food found, assuming 0.0 lbs left over.\n"
        error = "WARNING: ASSUMING 0.0 LB FOOD REMAINING"
        foodkey = "remain"
        dogdata[foodkey] = 0.0
    for size in ['small','medium','large']:
        if size not in dogdata.keys():
            dogdata[size] = 0
    alldogs = dogdata['small'] + dogdata['medium'] + dogdata['large']
    if alldogs > 30:
        result = result + "You have too many dogs.\n"
        error = 'TOO_MANY_DOGS'
    elif alldogs < 1:
        result = result + "You have no dogs, or negative dogs!"
        error = 'INSUFFICIENT_DOGS'
        return {'result':result, 'error':error}
    needed = float(dogdata['small']*10.0) + float(dogdata['medium']*20.0) +\
             float(dogdata['large']*30.0)
    result = result + "You need "+str(needed-dogdata[foodkey])+" lbs of dog food this month."
    return {'result': result, 'error': error}

if __name__ == '__main__':
    with open(sys.argv[1]) as stream:
        rawdata = stream.read()
    data = estimate_food(rawdata)
