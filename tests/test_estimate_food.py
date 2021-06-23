from doghouse import mgmt
import json
import pytest

with open('tests/tests.json') as fh:
    alltests = json.load(fh)

serialized_tests = []
for k,v in alltests.items():
    serialized_tests.append((k,v[0],v[1]))

@pytest.mark.parametrize("name,inputs,results",serialized_tests)
def test_food_estimator(name,inputs,results):
    output = mgmt.estimate_food(json.dumps(inputs))
    error_exists = results['error']
    if results['total'] is not None:
        expected_lbs = float(results['total'])
        assert output['result'].endswith("You need "+str(expected_lbs)+" lbs of dog food this month.")
    else:
        assert "You need" not in output['result'] and "of dog food this month" not in output['result']
    assert bool(output['error']) == error_exists
