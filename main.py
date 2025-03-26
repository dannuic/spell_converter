import os

import pandas as pd
import sqlite3

spells_file = 'spells_us.txt'
spells_strings_file = 'spells_us_str.txt'
spells_stacking_file = 'SpellStackingGroups.txt'
strings_db_file = 'dbstr_us.txt'
spells_db = 'spells.db'


def read_str(val):
    if val:
        return str(val)
    return None


def read_float(val):
    if val:
        return float(val)
    return None


def read_int(val):
    if val:
        return int(read_float(val))
    return None


def read_bool(val):
    if val:
        return bool(read_int(val))
    return None


class SPA(object):
    def __init__(self, slot, spa, base1, base2, calc, cap):
        self.slot = slot
        self.spa = spa
        self.base1 = base1
        self.base2 = base2
        self.calc = calc
        self.max = cap

    def __str__(self):
        return '[{}, {}, {}, {}, {}, {}]'.format(self.slot, self.spa, self.base1, self.base2, self.calc, self.max)

    @classmethod
    def parse(cls, val):
        def parse_spa(spa_def):
            vals = [read_int(d) for d in spa_def.split('|')]
            return cls(vals[0], vals[1], vals[2], vals[3], vals[4], vals[5])

        if not val:
            return None
        return [vars(parse_spa(spa_def)) for spa_def in str(val).split('$')]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
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
        'no_overwrite': read_bool, # 161 NO_OVERWRITE
        'image_number': read_int, # 162 IMAGENUMBER
        'mem_image_number': read_int, # 163 MEMIMAGENUMBER
        'spa_slots': SPA.parse, # 164 SPA_SLOTS
    }

    spells_table = pd.read_csv(spells_file,
                               header=None,
                               encoding='utf-8',
                               delimiter='^',
                               names=[*spells_names],
                               converters=spells_names,
                               index_col='id',
                               nrows=None)

    spells_table = spells_table.convert_dtypes()

    spells_strings_names = {
        'id': read_int,
        'caster_me': read_str,
        'caster_other': read_str,
        'casted_me': read_str,
        'casted_other': read_str,
        'spell_gone': read_str,
        'nop': read_str,
    }

    spells_strings_table = pd.read_csv(spells_strings_file,
                                       header=None,
                                       skiprows=1,
                                       encoding='utf-8',
                                       delimiter='^',
                                       names=[*spells_strings_names],
                                       converters=spells_strings_names,
                                       index_col='id',
                                       nrows=None)

    spells_strings_table = spells_strings_table.drop(['nop'], axis=1)
    spells_strings_table = spells_strings_table.convert_dtypes()

    spells_stacking_names = {
        'id': read_int,
        'stacking_group': read_int,
        'stacking_rank': read_int,
        'stacking_type': read_int,
        'nop': read_str,
    }

    spells_stacking_table = pd.read_csv(spells_stacking_file,
                                        header=None,
                                        skiprows=1,
                                        encoding='utf-8',
                                        delimiter='^',
                                        names=[*spells_stacking_names],
                                        converters=spells_stacking_names,
                                        index_col='id',
                                        nrows=None)

    spells_stacking_table = spells_stacking_table.drop(['nop'], axis=1)
    spells_stacking_table = spells_stacking_table.convert_dtypes()

    strings_names = {
        'desc_id': read_int,
        'channel': read_int,
        'description': read_str,
        'unk': read_int,
        'nop': read_str,
    }

    strings_table = pd.read_csv(strings_db_file,
                                header=None,
                                skiprows=0,
                                encoding='utf-8',
                                delimiter='^',
                                names=[*strings_names],
                                converters=strings_names,
                                index_col='desc_id',
                                nrows=None)

    strings_table = strings_table.drop(['channel', 'unk', 'nop'], axis=1)
    strings_table = strings_table.convert_dtypes()

    master_table = (
        spells_table
        .join(spells_strings_table, on='id', how='left')
        .join(spells_stacking_table, on='id', how='left')
        .join(strings_table, on='desc_id', how='left')
    )
    spells = master_table.drop(['spa_slots'], axis=1)

    spas = master_table[['spa_slots']].explode('spa_slots')
    spas = spas[spas['spa_slots'].notnull()].reset_index(level=0)
    spas = spas.join(pd.DataFrame(spas.pop('spa_slots').values.tolist())).set_index(['id', 'slot'])

    if os.path.isfile(spells_db):
        os.remove(spells_db)

    with sqlite3.connect(spells_db) as connection:
        spells.to_sql(name='spells', con=connection, index=True)
        spas.to_sql(name='spas', con=connection, index=True)
