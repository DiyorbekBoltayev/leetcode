def unikal_haflar_soni(s):
    n = len(s)
    a = []
    for i in s:
        if i not in a:
            n -= s.count(i)
            n += 1
            a.append(i)

    return n


tests = [
    'abracadabra',
    'python',
    'java',
    'javascript',
    'html'
]
answers = [5, 6, 3, 9, 4, ]
for i in range(len(tests)):
    test = tests[i]
    answer = answers[i]
    result = unikal_haflar_soni(test)
    if result == answer:
        print('Test {} PASSED'.format(i + 1))
    else:
        print('Test {} FAILED'.format(i + 1))

assert unikal_haflar_soni('abracadabra') == 5