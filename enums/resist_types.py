from .build_enum import from_enumeration


resist_types = from_enumeration(
    'resist_type',
    'resist_type_name',
    [
        (0, 'None'),
        (1, 'Magic'),
        (2, 'Fire'),
        (3, 'Cold'),
        (4, 'Poison'),
        (5, 'Disease'),
        (6, 'Chromatic'),
        (7, 'Prismatic'),
        (8, 'Physical'),
        (9, 'Corruption'),
    ]
)
