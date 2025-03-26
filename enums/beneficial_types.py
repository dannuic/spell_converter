from .build_enum import from_enumeration


beneficial_types = from_enumeration(
    'beneficial',
    'beneficial_name',
    [
        (0, 'Detrimental'),
        (1, 'Beneficial'),
        (2, 'Beneficial Group Only'),
    ]
)
