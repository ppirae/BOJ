for _ in range(int(input())):
    name = []
    drink = []
    for _ in range(int(input())):
        a, b = map(str, input().split())
        name.append(a)
        drink.append(int(b))
        m_d = max(drink)
    print(name[drink.index(m_d)])