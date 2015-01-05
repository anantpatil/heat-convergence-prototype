example_template = Template({
    'A': RsrcDef({}, []),
    'B': RsrcDef({}, []),
    'C': RsrcDef({'a': '4alpha'}, ['A', 'B']),
    'D': RsrcDef({'c': GetRes('C')}, []),
    'E': RsrcDef({'ca': GetAtt('C', 'a')}, []),
    'J': RsrcDef({}, []),
    #'K': RsrcDef({'k': GetRes('J')}, []),
    'K': RsrcDef({}, []),
    })
engine.create_stack('foo', example_template)
engine.noop(7)
engine.call(verify, example_template)
