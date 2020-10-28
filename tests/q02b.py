test = {
  'name': 'Question',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> list(X.shape) == [9966, 20]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> set(X.columns) == set(['demo','demo1','demo2','demo3','demo4','demo5','demo6','demo7','demo8','demo9','dv0','dv1','dv2','dv3','dv4','dv5','dv6','dv7','dv8','dv9'])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
