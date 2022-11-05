import pytest

import allpresidents

president_lastname = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Buren", "Harrison", "Tyler",
                      "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln", "Grant", "Hayes", "Garfield", "Arthur", "Cleveland",
                      "McKinley", "Roosevelt", "Taft", "Wilson", "Harding", "Hoover", "Truman", "Eisenhower", "Kennedy", "Johnson",
                      "Nixon", "Ford", "Carter", "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden", "Coolidge"]


@pytest.mark.parametrize("lastnames", president_lastname)
def test_allpresidents(lastnames):
    presidents = allpresidents.get_all_presidents()
    assert presidents.__contains__(lastnames)

