# operator

## operator.attrgetter(attr, /, *attrs)

After f = attrgetter('name'), the call f(r) returns r.name. After g = attrgetter('name', 'date'), the call g(r) returns (r.name, r.date). After h = attrgetter('name.first', 'name.last'), the call h(r) returns (r.name.first, r.name.last).

## operator.itemgetter(item, /, *items)

Return a callable object that fetches the given item(s) from its operand. After f = itemgetter(2), the call f(r) returns r[2]. After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])

## operator.methodcaller(name, /, *args, **kwargs)

Return a callable object that calls the given method on its operand. After f = methodcaller('name'), the call f(r) returns r.name(). After g = methodcaller('name', 'date', foo=1), the call g(r) returns r.name('date', foo=1).
