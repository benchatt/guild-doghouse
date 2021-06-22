import sys

def estimate_food(jsonfile):
    result = ''
    error = ''
    import json
    with open(jsonfile) as stream:
        rawdata = stream.read().lower()
    dogdata = json.loads(rawdata)
    foodkey = None
    for k in [k for k in dogdata.keys() if k not in ['small','medium','large']]:
        if 'remain' in k or 'left' in k or 'food' in k:
            foodkey = k
        else:
            result = result + f"Found extra data: {k}: {dogdata[k]}"+'\n'
    if foodkey is None:
        result = result + "No entry for leftover food found, assuming 0.0 lbs left over.\n"
        foodkey = "remain"
        dogdata[foodkey] = 0.0
    for size in ['small','medium','large']:
        if size not in dogdata.keys():
            dogdata[size] = 0
    alldogs =  dogdata['small'] + dogdata['medium'] + dogdata['large']
    if alldogs > 30:
        result = result + "You have too many dogs.\n"
        error = 'TOO_MANY_DOGS'
    elif alldogs < 1:
        result = result + "You have no dogs, or negative dogs!"
        error = 'INSUFFICIENT_DOGS'
        return {'result':result, 'error':error}
    needed = float(dogdata['small']*10.0) + float(dogdata['medium']*20.0) +\
             float(dogdata['large']*30.0)
    result = result + "You need {needed-dogdata[foodkey]} lbs of dog food this month."
    return {'result': result, 'error': error}

if __name__ == '__main__':
    data = estimate_food(sys.argv[1])
