import time

from utility_soup.iter.timer import ForLoopTimer


def test_with_range():
    timer = ForLoopTimer()
    counter = 0
    for i in timer(range(10)):
        assert counter == i
        counter += 1

    assert counter == 10


def test_with_string():
    timer = ForLoopTimer()
    counter = 0
    for i in timer('hello there'):
        assert 'hello there'[counter] == i
        counter += 1

    assert counter == len('hello there')


def test_check_timing():
    sleep_inc = 0.1
    sleep_error = 0.1

    timer = ForLoopTimer()
    for i in timer(range(10)):
        time.sleep(sleep_inc)

    assert len(timer.laps) == 10
    assert timer.laps == pytest.approx([sleep_inc] * len(timer.laps),
                                       abs=sleep_inc * sleep_error)
