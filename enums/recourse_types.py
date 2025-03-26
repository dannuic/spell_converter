from .build_enum import from_list


recourse_types = from_list(
    'recourse_type',
    'recourse_type_name',
    [
        'Always Hit',
        'Always Hit No Resist',
        'Once No Resist',
        'Once',
    ]
)