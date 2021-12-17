# amount = 50
failures = []
def check_tests(amount):
    try:
        assert (amount < 100)
        print('test passed')
    except AssertionError:
        failures.append('add to error')

def check_failures(cf):
    assert [] == failures, 'ERROR: There was failures'

check_tests(50)
print('test1 passed')
check_tests(200)
print('test2 passed')
check_tests(99)
print('test3 passed')

check_failures(failures)
# print(failures)
