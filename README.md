# guild-doghouse
The Dog Shelter test case for Guild Education interview, Ben Chatterton

## How to install
- Clone the repository
- Be sure you are running Python 3.6 or later
- From the `guild-doghouse` directory, run:
> python3 setup.py pytest

As a bonus, you should be able to build a wheel by:
> python3 setup.py bdist_wheel

## Task requirements
From the repo root directory, you can import the code in python3 interactive mode:

> from doghouse import mgmt

The food estimator takes raw JSON text as the only parameter, example of such to follow:

> data = '{"small": 3, "medium": 12, "large": 10, "leftover": 35.5}'

> mgmt.estimate_food(data)

The results provide a dict with two entries: `result`, which provides all text feedback including the food estimate if available, and `error`, which names error or warning feedback.

### Assumptions
I operated under one primary assumption, from which all the others flowed: that I don't know what to assume. As an example without a dev team or product owners to consult, I just went ahead and made assumptions that made the project easier for me:
- As mentioned, input is in JSON
- When an estimate of food needs is even vaguely reasonable, it should be returned. While it's not immediately clear what, for example, 1.5 small dogs would mean, the user might have some reason for this (the small dog is only going to be in the shelter for 15 days, or the dog is particularly small).
- When a request is anything other than nominal, an "error" should be returned. For the purposes of this project, I'm conflating errors and warnings into this category (hence the quotation marks). The end user should get feedback anytime something is irregular, so they have an opportunity to correct the request should it be mistaken.
- I am pretending that this code should be part of a larger kennel management system, and that another team would theoretically be responsible for UX elements.
- While it wasn't strictly necessary, I thought formatting the project as if it were the beginnings of a new Python library might make things tidier.
