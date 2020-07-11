example_template = Template({
    'A': RsrcDef({}, []),
    'B': RsrcDef({}, []),
    'C': RsrcDef({'a': '4alpha'}, ['A']),
    'D': RsrcDef({'c': GetRes('C')}, []),
    'E': RsrcDef({}, []),
})
engine.create_stack('foo', example_template)
engine.noop(5)
engine.call(verify, example_template)
