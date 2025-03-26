from .build_enum import from_list


stacking_rules = from_list(
    'stacking_type',
    'stacking_type_name',
    [
        'None',
        'Single Caster',
        'All Casters',
        'Single Caster Only Greater',
        'All Casters Only Greater',
        'Single Caster Never Overwrite',
        'All Casters Never Overwrite',
        'Single Caster Always Overwrite',
        'All Casters Always Overwrite',
        'Invalid',
    ]
)