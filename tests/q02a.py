test = {
  'name': 'Question',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> list(y_class.unique()) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(y_class) == 9966
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
