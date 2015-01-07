h_uuid = None

def store_h_uuid():
    global h_uuid
    h_uuid = next(iter(reality.resources_by_logical_name('H')))

def check_resource_count(expected_count):
    actual = len(reality.all_resources())
    assert (expected_count == actual)

def check_h_not_replaced():
    h_uuid_after_update = next(iter(reality.resources_by_logical_name('H')))
    assert (h_uuid_after_update == h_uuid)
    test.assertIsNot(h_uuid, None)

example_template0 = Template({
    'H': RsrcDef({'!h': 'initial'}, []),
    })
engine.create_stack('foo', example_template0)
engine.noop(1)
engine.call(verify, example_template0)
engine.call(store_h_uuid)

example_template = Template({
    'H': RsrcDef({'!h': 'updated'}, []),
    'A': RsrcDef({}, []),
    'B': RsrcDef({}, []),
    'C': RsrcDef({'a': '4alpha'}, ['A', 'B']),
    'D': RsrcDef({'c': GetRes('C')}, []),
    'E': RsrcDef({'ca': GetAtt('C', 'a')}, []),
    })
engine.update_stack('foo', example_template)
engine.noop(5)

engine.rollback_stack('foo')
engine.noop(10)

engine.call(verify, example_template0)
engine.call(check_resource_count, 1)
engine.call(check_h_not_replaced)
