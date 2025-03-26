from .build_enum import from_enumeration


value_calcs = from_enumeration(
	'calc',
	'calc_name',
	[
		(107, 'DecayTick1'),
		(108, 'DecayTick2'),
		(120, 'DecayTick5'),
		(122, 'DecayTick12'),
		(123, 'Random'),
	]
)