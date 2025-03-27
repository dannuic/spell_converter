import os
from typing import Any, Type, TypeVar
from argparse import ArgumentParser
from glob import glob

import pandas as pd
import sqlite3

import enums

T = TypeVar('T', bound='Parent')

spells_file = 'spells_us.txt'
spells_strings_file = 'spells_us_str.txt'
spells_stacking_file = 'Resources/SpellStackingGroups.txt'
strings_db_file = 'dbstr_us.txt'


def read_str(val: Any) -> str | None:
    if val:
        return str(val)
    return None


def read_float(val: Any) -> float | None:
    if val:
        return float(val)
    return None


def read_int(val: Any) -> int | None:
    if val:
        return int(read_float(val))
    return None


def read_bool(val: Any) -> bool | None:
    if val:
        return bool(read_int(val))
    return None


class SPA(object):
    def __init__(self,
                 slot: int,
                 spa: int,
                 base1: int,
                 base2: int,
                 calc: int,
                 cap: int
                 ) -> None:
        self.slot = slot
        self.spa = spa
        self.base1 = base1
        self.base2 = base2
        self.calc = calc
        self.max = cap

    def __str__(self):
        return '[{}, {}, {}, {}, {}, {}]'.format(self.slot, self.spa, self.base1, self.base2, self.calc, self.max)

    @classmethod
    def parse(cls: Type[T], val: Any) -> T | None:
        def parse_spa(spa_def):
            vals = [read_int(d) for d in spa_def.split('|')]
            return cls(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5])

        if not val:
            return None
        return [vars(parse_spa(spa_def)) for spa_def in str(val).split('$')]


def read_spells(file: str) -> pd.DataFrame:
    spells_names = {
        'id': read_int, # 0 SPELLINDEX
        'name': read_str, # 1 SPELLNAME
        'actortag': read_int, # 2 ACTORTAG
        'extra': read_str, # 3 NPC_FILENAME
        'range': read_int, # 4 RANGE
        'ae_range': read_int, # 5 IMPACTRADIUS
        'push_back': read_float, # 6 OUTFORCE
        'push_up': read_float, # 7 UPFORCE
        'casting_time': read_int, # 8 CASTINGTIME
        'rest_time': read_int, # 9 RECOVERYDELAY
        'recast_time': read_int, # 10 SPELLDELAY
        'duration_base': read_int, # 11 DURATIONBASE
        'duration_ticks': read_int, # 12 DURATIONCAP
        'ae_duration': read_int, # 13 IMPACTDURATION
        'mana': read_int, # 14 MANACOST
        'reagent1': read_int, # 15 EXPENDREAGENT1 .. 18 EXPENDREAGENT4
        'reagent2': read_int,
        'reagent3': read_int,
        'reagent4': read_int,
        'reagent_qty1': read_int, # 19 EXPENDQTY1 .. 22 EXPENDQTY4
        'reagent_qty2': read_int,
        'reagent_qty3': read_int,
        'reagent_qty4': read_int,
        'focus_id1': read_int, # 23 NOEXPENDREAGENT1 .. 26 NOEXPENDREAGENT4
        'focus_id2': read_int,
        'focus_id3': read_int,
        'focus_id4': read_int,
        'light_type': read_int, # 27 LIGHTTYPE
        'beneficial': read_int, # 28 BENEFICIAL
        'resist_type': read_int, # 29 RESISTTYPE
        'target_type': read_int, # 30 TYPENUMBER
        'base_difficulty': read_int, # 31 BASEDIFFICULTY = fizzle?
        'skill': read_int, # 32 CASTINGSKILL
        'zone': read_int, # 33 ZONETYPE
        'environment': read_int, # 34 ENVIRONMENTTYPE
        'time_of_day': read_int, # 35 TIMEOFDAY
        'war_level': read_int, # 36 WARRIORMIN .. 51 BERSERKERMIN
        'clr_level': read_int,
        'pld_level': read_int,
        'rng_level': read_int,
        'shd_level': read_int,
        'dru_level': read_int,
        'mnk_level': read_int,
        'brd_level': read_int,
        'rog_level': read_int,
        'shm_level': read_int,
        'nec_level': read_int,
        'wiz_level': read_int,
        'mag_level': read_int,
        'enc_level': read_int,
        'bst_level': read_int,
        'ber_level': read_int,
        'casting_anim': read_int, # 52 CASTINGANIM
        'target_anim': read_int, # 53 TARGETANIM
        'travel_type': read_int, # 54 TRAVELTYPE
        'spell_affect_index': read_int, # 55 SPELLAFFECTINDEX
        'cancel_on_sit': read_bool, # 56 CANCELONSIT
        'deity_agnostic': read_bool, # 58 DIETY_AGNOSTIC .. 73 DIETY_VEESHAN
        'deity_bertox': read_bool,
        'deity_brell': read_bool,
        'deity_cazic': read_bool,
        'deity_erollisi': read_bool,
        'deity_bristlebane': read_bool,
        'deity_innoruuk': read_bool,
        'deity_karana': read_bool,
        'deity_mithaniel': read_bool,
        'deity_prexus': read_bool,
        'deity_quellious': read_bool,
        'deity_rallos': read_bool,
        'deity_rodcet': read_bool,
        'deity_solusek': read_bool,
        'deity_tribunal': read_bool,
        'deity_tunare': read_bool,
        'deity_veeshan': read_bool,
        'npc_no_cast': read_bool, # 74 NPC_NO_CAST
        'icon': read_int, # 75 NEW_ICON
        'effect_index': read_int, # 76 SPELL_EFFECT_INDEX
        'no_interrupt': read_bool, # 77 NO_INTERRUPT
        'resist_mod': read_int, # 78 RESIST_MOD
        'not_stackable_dot': read_bool, # 79 NOT_STACKABLE_DOT
        'delete_ok': read_bool, # 80 DELETE_OK
        'recourse_id': read_int, # 81 REFLECT_SPELLINDEX
        'partial_resist': read_bool, # 82 NO_PARTIAL_SAVE = used to prevent a nuke from being partially resisted. it also prevents or allows a player to resist a spell fully if they resist "part" of its components.
        'persistent_particles': read_bool, # 83 USES_PERSISTENT_PARTICLES
        'song_window': read_bool, # 84 BARD_BUFF_BOX
        'desc_id': read_int, # 85 DESCRIPTION_INDEX
        'primary_category': read_int, # 86 PRIMARY_CATEGORY
        'secondary_category1': read_int, # 87 SECONDARY_CATEGORY_1
        'secondary_category2': read_int, # 88 SECONDARY_CATEGORY_2
        'no_npc_los': read_bool, # 89 NO_NPC_LOS - NPC Does not Require LoS
        'feedbackable': read_bool, # 90 FEEDBACKABLE - Triggers spell damage shield. This is mostly used on procs and non nukes, so it's not that useful to show
        'reflectable': read_bool, # 91 REFLECTABLE
        'hate_mod': read_int, # 92 HATE_MOD
        'resist_per_level': read_int, # 93 RESIST_PER_LEVEL
        'resist_cap': read_int, # 94 RESIST_CAP
        'affect_inanimate': read_bool, # 95 AFFECT_INANIMATE - Can be cast on objects
        'endurance': read_int, # 96 STAMINA_COST
        'timer_id': read_int, # 97 TIMER_INDEX
        'is_skill': read_bool, # 98 IS_SKILL
        'hate_override': read_int, # 99 SPELL_HATE_GIVEN
        'endurance_upkeep': read_int, # 100 ENDUR_UPKEEP
        'max_hits_type': read_float, # 101 LIMITED_USE_TYPE
        'max_hits': read_int, # 102 LIMITED_USE_COUNT
        'pvp_resist_mod': read_float, # 103 PVP_RESIST_MOD
        'pvp_resist_per_level': read_int, # 104 PVP_RESIST_PER_LEVEL
        'pvp_resist_cap': read_int, # 105 PVP_RESIST_CAP
        'pvp_duration': read_int, # 106 PVP_DURATION
        'pvp_duration_cap': read_int, # 107 PVP_DURATION_CAP
        'pcnpc_only_flag': read_bool, # 108 PCNPC_ONLY_FLAG
        'cast_not_standing': read_bool, # 109 CAST_NOT_STANDING
        'can_mgb': read_bool, # 110 CAN_MGB
        'no_dispell': read_bool, # 111 NO_DISPELL
        'npc_mem_category': read_int, # 112 NPC_MEM_CATEGORY
        'npc_usefulness': read_int, # 113 NPC_USEFULNESS
        'min_resist': read_int, # 114 MIN_RESIST
        'max_resist': read_int, # 115 MAX_RESIST
        'min_spread_time': read_int, # 116 MIN_SPREAD_TIME
        'max_spread_time': read_int, # 117 MAX_SPREAD_TIME
        'duration_particle_effect': read_int, # 118 DURATION_PARTICLE_EFFECT
        'cone_start_angle': read_int, # 119 CONE_START_ANGLE
        'cone_end_angle': read_int, # 120 CONE_END_ANGLE
        'sneak_attack': read_bool, # 121 SNEAK_ATTACK
        'not_focusable': read_bool, # 122 NOT_FOCUSABLE
        'no_detrimental_spell_aggro': read_bool, # 123 NO_DETRIMENTAL_SPELL_AGGRO
        'show_wear_off_message': read_bool, # 124 SHOW_WEAR_OFF_MESSAGE
        'duration_frozen': read_bool, # 125 IS_COUNTDOWN_HELD
        'spread_range': read_int, # 126 SPREAD_RADIUS
        'song_cap': read_int, # 127 BASE_EFFECTS_FOCUS_CAP
        'stacks_with_self': read_bool, # 128 STACKS_WITH_SELF
        'not_shown': read_bool, # 129 NOT_SHOWN_TO_PLAYER
        'no_buff_block': read_bool, # 130 NO_BUFF_BLOCK
        'anim_variation': read_int, # 131 ANIM_VARIATION
        'group': read_int, # 132 SPELL_GROUP
        'rank': read_int, # 133 SPELL_GROUP_RANK // rank 1/5/10. a few auras do not have this set properly
        'no_resist': read_bool, # 134 NO_RESIST - ignore SPA 177 resist
        'allow_scribe': read_bool, # 135 ALLOW_SPELLSCRIBE
        'target_restrict': read_int, # 136 SPELL_REQ_ASSOCIATION_ID
        'allow_fast_regen': read_bool, # 137 BYPASS_REGEN_CHECK
        'can_cast_in_combat': read_bool, # 138 CAN_CAST_IN_COMBAT
        'can_cast_out_of_combat': read_bool, # 139 CAN_CAST_OUT_OF_COMBAT
        'show_dot_message': read_bool, # 140 SHOW_DOT_MESSAGE
        'crit_override': read_int, # 141 OVERRIDE_CRIT_CHANCE
        'max_targets': read_int, # 142 MAX_TARGETS
        'no_heal_damage_item_mod': read_int, # 143 NO_HEAL_DAMAGE_ITEM_MOD
        'caster_restrict': read_int, # 144 CASTER_REQUIREMENT_ID
        'spell_class': read_int, # 145 SPELL_CLASS
        'spell_subclass': read_int, # 146 SPELL_SUBCLASS
        'ai_valid_targets': read_float, # 147 AI_VALID_TARGETS
        'persist_after_death': read_bool, # 148 NO_STRIP_ON_DEATH
        'base_effects_focus_slope': read_float, # 149 BASE_EFFECTS_FOCUS_SLOPE
        'base_effects_focus_offset': read_float, # 150 BASE_EFFECTS_FOCUS_OFFSET
        'range_close_dist': read_int, # 151 DISTANCE_MOD_CLOSE_DIST
        'range_close_mult': read_float, # 152 DISTANCE_MOD_CLOSE_MULT
        'range_far_dist': read_int, # 153 DISTANCE_MOD_FAR_DIST
        'range_far_mult': read_int, # 154 DISTANCE_MOD_FAR_MULT
        'min_range': read_int, # 155 MIN_RANGE
        'no_remove': read_bool, # 156 NO_REMOVE
        'recourse_type': read_int, # 157 SPELL_RECOURSE_TYPE
        'only_fast_regen': read_bool, # 158 ONLY_DURING_FAST_REGEN
        'beta': read_bool, # 159 IS_BETA_ONLY
        'subgroup': read_int, # 160 SPELL_SUBGROUP
        'no_overwrite': read_int, # 161 NO_OVERWRITE
        'image_number': read_int, # 162 IMAGENUMBER
        'mem_image_number': read_int, # 163 MEMIMAGENUMBER
        'spa_slots': SPA.parse, # 164 SPA_SLOTS
    }

    return pd.read_csv(file,
                       header=None,
                       encoding='utf-8',
                       delimiter='^',
                       names=[*spells_names],
                       converters=spells_names,
                       index_col='id',
                       nrows=None
                       ).convert_dtypes(
    ).merge(
        enums.categories.rename(columns={'category_name': 'primary_category_name'}),
        left_on='primary_category',
        right_index=True,
        how='left',
    ).merge(
        enums.categories.rename(columns={'category_name': 'secondary_category1_name'}),
        left_on='secondary_category1',
        right_index=True,
        how='left',
    ).merge(
        enums.categories.rename(columns={'category_name': 'secondary_category2_name'}),
        left_on='secondary_category2',
        right_index=True,
        how='left',
    ).join(
        enums.beneficial_types, on='beneficial', how='left'
    ).join(
        enums.no_overwrite, on='no_overwrite', how='left'
    ).join(
        enums.recourse_types, on='recourse_type', how='left'
    ).join(
        enums.resist_types, on='resist_type', how='left'
    ).join(
        enums.target_types, on='target_type', how='left'
    )


def read_spell_strings(file: str) -> pd.DataFrame:
    columns = {
        'id': read_int,
        'caster_me': read_str,
        'caster_other': read_str,
        'casted_me': read_str,
        'casted_other': read_str,
        'spell_gone': read_str,
        'nop': read_str,
    }

    return pd.read_csv(file,
                       header=None,
                       skiprows=1,
                       encoding='utf-8',
                       delimiter='^',
                       names=[*columns],
                       converters=columns,
                       index_col='id',
                       nrows=None
                       ).drop(['nop'], axis=1).convert_dtypes()


def read_strings(file: str) -> pd.DataFrame:
    columns = {
        'id': read_int,
        'type': read_int,
        'text': read_str,
        'unk': read_int,
        'nop': read_str,
    }

    return pd.read_csv(file,
                       header=None,
                       skiprows=0,
                       encoding='utf-8',
                       delimiter='^',
                       names=[*columns],
                       converters=columns,
                       index_col='id',
                       nrows=None
                       ).drop(['unk', 'nop'], axis=1).convert_dtypes()


def read_spell_stacking(file: str, strings: pd.DataFrame) -> pd.DataFrame:
    columns = {
        'id': read_int,
        'stacking_group': read_int,
        'stacking_rank': read_int,
        'stacking_type': read_int,
        'nop': read_str,
    }

    return pd.read_csv(file,
                       header=None,
                       skiprows=1,
                       encoding='utf-8',
                       delimiter='^',
                       names=[*columns],
                       converters=columns,
                       index_col='id',
                       nrows=None
                       ).drop(['nop'], axis=1).convert_dtypes().join(
        read_stacking_names(strings), on='stacking_group', how='left'
    ).join(enums.stacking_rules, on='stacking_type', how='left')


def read_stacking_names(strings: pd.DataFrame) -> pd.DataFrame:
    stacking_names = (
        strings[strings['type'] == 40][['text']]
        .rename(columns={'text': 'stacking_name'})
    )

    stacking_names.index.name = 'stacking_group'

    return stacking_names


def read_spell_descriptions(strings: pd.DataFrame) -> pd.DataFrame:
    spell_descriptions = (
        strings[strings['type'] == 6][['text']]
        .rename(columns = {'text': 'description'})
    )

    spell_descriptions.index.name = 'desc_id'

    return spell_descriptions


def base_tables(eq_dir: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    from os.path import join

    spells = read_spells(join(eq_dir, spells_file))
    spell_strings = read_spell_strings(join(eq_dir, spells_strings_file))
    strings = read_strings(join(eq_dir, strings_db_file))
    spell_stacking = read_spell_stacking(join(eq_dir, spells_stacking_file), strings)
    spell_descriptions = read_spell_descriptions(strings)

    master_table = (
        spells
        .join(spell_strings, on='id', how='left')
        .join(spell_stacking, on='id', how='left')
        .join(spell_descriptions, on='desc_id', how='left')
    )

    spells = master_table.drop(['spa_slots'], axis=1)

    spas = master_table[['spa_slots']].explode('spa_slots')
    spas = spas[spas['spa_slots'].notnull()].reset_index(level=0)
    spas = (
        spas
        .join(pd.DataFrame(spas.pop('spa_slots').values.tolist()))
        .join(enums.spas, on='spa', how='left')
        .join(enums.value_calcs, on='calc', how='left')
        .set_index(['id', 'slot'])
    )

    return spells, spas


def character_table(character_file: str, name_server: tuple[str, str]) -> pd.DataFrame:
    columns = {
        'level': read_int,
        'name': read_str,
    }

    return pd.read_csv(character_file,
                       header=None,
                       skiprows=0,
                       encoding='utf-8',
                       delimiter='\t',
                       names=[*columns],
                       converters=columns,
                       nrows=None).convert_dtypes().assign(
        character=name_server[0], server=name_server[1],
    )[['character', 'server', 'level', 'name']]


def character_tables(eq_dir: str, suffix: str) -> list[tuple[pd.DataFrame, tuple[str, str]]]:
    from os.path import join
    import re

    return [(character_table(join(eq_dir, m.string), m.groups()), m.groups()) for m in
     [re.search(rf'(.*)_(.*)-{suffix}.txt', f) for f in os.listdir(eq_dir)]
     if m is not None]


# Press the green button in the gutter to run the script.
def main(eq_dir: str,
         spells_db: str,
         do_base: bool = False,
         do_character: bool = False) -> None:
    if do_base:
        spells, spas = base_tables(eq_dir)

        with sqlite3.connect(spells_db) as connection:
            connection.execute('DROP TABLE IF EXISTS spells')
            spells.to_sql(name='spells', con=connection, index=True)

            connection.execute('DROP TABLE IF EXISTS spas')
            spas.to_sql(name='spas', con=connection, index=True)

    if do_character:
        with sqlite3.connect(spells_db) as connection:
            connection.execute(
                'CREATE TABLE IF NOT EXISTS spellbooks(character TEXT, server TEXT, level INTEGER, name TEXT)')

            for table, (name, server) in character_tables(eq_dir, 'Spellbook'):
                connection.execute(f'DELETE FROM spellbooks WHERE character=? AND server=?', (name, server))
                table.to_sql(name='spellbooks', con=connection, if_exists='append', index=False)

            connection.execute(
                'CREATE TABLE IF NOT EXISTS missing_spells(character TEXT, server TEXT, level INTEGER, name TEXT)')

            for table, (name, server) in character_tables(eq_dir, 'MissingSpells'):
                connection.execute(f'DELETE FROM missing_spells WHERE character=? AND server=?', (name, server))
                table.to_sql(name='missing_spells', con=connection, if_exists='append', index=False)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('eq_dir',
                        help='everquest directory where files necessary for parsing live')
    parser.add_argument('-b', '--base-tables', dest='base_tables', action='store_true',
                        help='recreate the base spells and spas tables in the db')
    parser.add_argument('-c', '--character-tables', dest='character_tables', action='store_true',
                        help='parse character spellbook outputs and add tables in the result')
    parser.add_argument('-o', '--output', dest='output', default='spells.db',
                        help='sqlite db file to write results to')

    args = parser.parse_args()
    main(args.eq_dir, args.output, do_base=args.base_tables, do_character=args.character_tables)