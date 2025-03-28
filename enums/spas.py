from .build_enum import from_enumeration


spas = from_enumeration(
    'spa',
    'spa_name',
    [
        (0, 'HP'),
        (1, 'AC'),
        (2, 'ATTACK POWER'),
        (3, 'MOVEMENT RATE'),
        (4, 'STR'),
        (5, 'DEX'),
        (6, 'AGI'),
        (7, 'STA'),
        (8, 'INT'),
        (9, 'WIS'),
        (10, 'CHA'),
        (11, 'HASTE'),
        (12, 'INVISIBILITY'),
        (13, 'SEE INVIS'),
        (14, 'ENDURING BREATH'),
        (15, 'MANA'),
        (16, 'NPC FRENZY'),
        (17, 'NPC AWARENESS'),
        (18, 'NPC AGGRO'),
        (19, 'NPC FACTION'),
        (20, 'BLINDNESS'),
        (21, 'STUN'),
        (22, 'CHARM'),
        (23, 'FEAR'),
        (24, 'FATIGUE'),
        (25, 'BIND AFFINITY'),
        (26, 'GATE'),
        (27, 'DISPEL MAGIC'),
        (28, 'INVIS VS UNDEAD'),
        (29, 'INVIS VS ANIMALS'),
        (30, 'NPC AGGRO RADIUS'),
        (31, 'ENTHRALL'),
        (32, 'CREATE ITEM'),
        (33, 'SUMMON PET'),
        (34, 'CONFUSE'),
        (35, 'DISEASE'),
        (36, 'POISON'),
        (37, 'DETECT HOSTILE'),
        (38, 'DETECT MAGIC'),
        (39, 'NO TWINCAST'),
        (40, 'INVULNERABILITY'),
        (41, 'BANISH'),
        (42, 'SHADOW STEP'),
        (43, 'BERSERK'),
        (44, 'LYCANTHROPY'),
        (45, 'VAMPIRISM'),
        (46, 'RESIST FIRE'),
        (47, 'RESIST COLD'),
        (48, 'RESIST POISON'),
        (49, 'RESIST DISEASE'),
        (50, 'RESIST MAGIC'),
        (51, 'DETECT TRAPS'),
        (52, 'DETECT UNDEAD'),
        (53, 'DETECT SUMMONED'),
        (54, 'DETECT ANIMALS'),
        (55, 'STONESKIN'),
        (56, 'TRUE NORTH'),
        (57, 'LEVITATION'),
        (58, 'CHANGE FORM'),
        (59, 'DAMAGE SHIELD'),
        (60, 'TRANSFER ITEM'),
        (61, 'ITEM LORE'),
        (62, 'ITEM IDENTIFY'),
        (63, 'NPC WIPE HATE LIST'),
        (64, 'SPIN STUN'),
        (65, 'INFRAVISION'),
        (66, 'ULTRAVISION'),
        (67, 'EYE OF ZOMM'),
        (68, 'RECLAIM ENERGY'),
        (69, 'MAX HP'),
        (70, 'CORPSE BOMB'),
        (71, 'CREATE UNDEAD'),
        (72, 'PRESERVE CORPSE'),
        (73, 'BIND SIGHT'),
        (74, 'FEIGN DEATH'),
        (75, 'VENTRILOQUISM'),
        (76, 'SENTINEL'),
        (77, 'LOCATE CORPSE'),
        (78, 'SPELL SHIELD'),
        (79, 'INSTANT HP'),
        (80, 'ENCHANT LIGHT'),
        (81, 'RESURRECT'),
        (82, 'SUMMON TARGET'),
        (83, 'PORTAL'),
        (84, 'HP NPC ONLY'),
        (85, 'MELEE PROC'),
        (86, 'NPC HELP RADIUS'),
        (87, 'MAGNIFICATION'),
        (88, 'EVACUATE'),
        (89, 'HEIGHT'),
        (90, 'IGNORE PET'),
        (91, 'SUMMON CORPSE'),
        (92, 'HATE'),
        (93, 'WEATHER CONTROL'),
        (94, 'FRAGILE'),
        (95, 'SACRIFICE'),
        (96, 'SILENCE'),
        (97, 'MAX MANA'),
        (98, 'BARD HASTE'),
        (99, 'ROOT'),
        (100, 'HEALDOT'),
        (101, 'COMPLETEHEAL'),
        (102, 'PET FEARLESS'),
        (103, 'CALL PET'),
        (104, 'TRANSLOCATE'),
        (105, 'NPC ANTI GATE'),
        (106, 'BEASTLORD PET'),
        (107, 'ALTER PET LEVEL'),
        (108, 'FAMILIAR'),
        (109, 'CREATE ITEM IN BAG'),
        (110, 'ARCHERY'),
        (111, 'RESIST ALL'),
        (112, 'FIZZLE SKILL'),
        (113, 'SUMMON MOUNT'),
        (114, 'MODIFY HATE'),
        (115, 'CORNUCOPIA'),
        (116, 'CURSE'),
        (117, 'HIT MAGIC'),
        (118, 'AMPLIFICATION'),
        (119, 'ATTACK SPEED MAX'),
        (120, 'HEALMOD'),
        (121, 'IRONMAIDEN'),
        (122, 'REDUCESKILL'),
        (123, 'IMMUNITY'),
        (124, 'FOCUS DAMAGE MOD'),
        (125, 'FOCUS HEAL MOD'),
        (126, 'FOCUS RESIST MOD'),
        (127, 'FOCUS CAST TIME MOD'),
        (128, 'FOCUS DURATION MOD'),
        (129, 'FOCUS RANGE MOD'),
        (130, 'FOCUS HATE MOD'),
        (131, 'FOCUS REAGENT MOD'),
        (132, 'FOCUS MANACOST MOD'),
        (133, 'FOCUS STUNTIME MOD'),
        (134, 'FOCUS LEVEL MAX'),
        (135, 'FOCUS RESIST TYPE'),
        (136, 'FOCUS TARGET TYPE'),
        (137, 'FOCUS WHICH SPA'),
        (138, 'FOCUS BENEFICIAL'),
        (139, 'FOCUS WHICH SPELL'),
        (140, 'FOCUS DURATION MIN'),
        (141, 'FOCUS INSTANT ONLY'),
        (142, 'FOCUS LEVEL MIN'),
        (143, 'FOCUS CASTTIME MIN'),
        (144, 'FOCUS CASTTIME MAX'),
        (145, 'NPC PORTAL WARDER BANISH'),
        (146, 'PORTAL LOCATIONS'),
        (147, 'PERCENT HEAL'),
        (148, 'STACKING BLOCK'),
        (149, 'STRIP VIRTUAL SLOT'),
        (150, 'DIVINE INTERVENTION'),
        (151, 'POCKET PET'),
        (152, 'PET SWARM'),
        (153, 'HEALTH BALANCE'),
        (154, 'CANCEL NEGATIVE MAGIC'),
        (155, 'POP RESURRECT'),
        (156, 'MIRROR'),
        (157, 'FEEDBACK'),
        (158, 'REFLECT'),
        (159, 'MODIFY ALL STATS'),
        (160, 'CHANGE SOBRIETY'),
        (161, 'SPELL GUARD'),
        (162, 'MELEE GUARD'),
        (163, 'ABSORB HIT'),
        (164, 'OBJECT SENSE TRAP'),
        (165, 'OBJECT DISARM TRAP'),
        (166, 'OBJECT PICKLOCK'),
        (167, 'FOCUS PET'),
        (168, 'DEFENSIVE'),
        (169, 'CRITICAL MELEE'),
        (170, 'CRITICAL SPELL'),
        (171, 'CRIPPLING BLOW'),
        (172, 'EVASION'),
        (173, 'RIPOSTE'),
        (174, 'DODGE'),
        (175, 'PARRY'),
        (176, 'DUAL WIELD'),
        (177, 'DOUBLE ATTACK'),
        (178, 'MELEE LIFETAP'),
        (179, 'PURETONE'),
        (180, 'SANCTIFICATION'),
        (181, 'FEARLESS'),
        (182, 'HUNDRED HANDS'),
        (183, 'SKILL INCREASE CHANCE'),
        (184, 'ACCURACY'),
        (185, 'SKILL DAMAGE MOD'),
        (186, 'MIN DAMAGE DONE MOD'),
        (187, 'MANA BALANCE'),
        (188, 'BLOCK'),
        (189, 'ENDURANCE'),
        (190, 'INCREASE MAX ENDURANCE'),
        (191, 'AMNESIA'),
        (192, 'HATE OVER TIME'),
        (193, 'SKILL ATTACK'),
        (194, 'FADE'),
        (195, 'STUN RESIST'),
        (196, 'STRIKETHROUGH1'),
        (197, 'SKILL DAMAGE TAKEN'),
        (198, 'INSTANT ENDURANCE'),
        (199, 'TAUNT'),
        (200, 'PROC CHANCE'),
        (201, 'RANGE ABILITY'),
        (202, 'ILLUSION OTHERS'),
        (203, 'MASS GROUP BUFF'),
        (204, 'GROUP FEAR IMMUNITY'),
        (205, 'RAMPAGE'),
        (206, 'AE TAUNT'),
        (207, 'FLESH TO BONE'),
        (208, 'PURGE POISON'),
        (209, 'CANCEL BENEFICIAL'),
        (210, 'SHIELD CASTER'),
        (211, 'DESTRUCTIVE FORCE'),
        (212, 'FOCUS FRENZIED DEVASTATION'),
        (213, 'PET PCT MAX HP'),
        (214, 'HP MAX HP'),
        (215, 'PET PCT AVOIDANCE'),
        (216, 'MELEE ACCURACY'),
        (217, 'HEADSHOT'),
        (218, 'PET CRIT MELEE'),
        (219, 'SLAY UNDEAD'),
        (220, 'INCREASE SKILL DAMAGE'),
        (221, 'REDUCE WEIGHT'),
        (222, 'BLOCK BEHIND'),
        (223, 'DOUBLE RIPOSTE'),
        (224, 'ADD RIPOSTE'),
        (225, 'GIVE DOUBLE ATTACK'),
        (226, '2H BASH'),
        (227, 'REDUCE SKILL TIMER'),
        (228, 'ACROBATICS'),
        (229, 'CAST THROUGH STUN'),
        (230, 'EXTENDED SHIELDING'),
        (231, 'BASH CHANCE'),
        (232, 'DIVINE SAVE'),
        (233, 'METABOLISM'),
        (234, 'POISON MASTERY'),
        (235, 'FOCUS CHANNELING'),
        (236, 'FREE PET'),
        (237, 'PET AFFINITY'),
        (238, 'PERM ILLUSION'),
        (239, 'STONEWALL'),
        (240, 'STRING UNBREAKABLE'),
        (241, 'IMPROVE RECLAIM ENERGY'),
        (242, 'INCREASE CHANGE MEMWIPE'),
        (243, 'ENHANCED CHARM'),
        (244, 'ENHANCED ROOT'),
        (245, 'TRAP CIRCUMVENTION'),
        (246, 'INCREASE AIR SUPPLY'),
        (247, 'INCREASE MAX SKILL'),
        (248, 'EXTRA SPECIALIZATION'),
        (249, 'OFFHAND MIN WEAPON DAMAGE'),
        (250, 'INCREASE PROC CHANCE'),
        (251, 'ENDLESS QUIVER'),
        (252, 'BACKSTAB FRONT'),
        (253, 'CHAOTIC STAB'),
        (254, 'NOSPELL'),
        (255, 'SHIELDING DURATION MOD'),
        (256, 'SHROUD OF STEALTH'),
        (257, 'GIVE PET HOLD'),
        (258, 'TRIPLE BACKSTAB'),
        (259, 'AC LIMIT MOD'),
        (260, 'ADD INSTRUMENT MOD'),
        (261, 'SONG MOD CAP'),
        (262, 'INCREASE STAT CAP'),
        (263, 'TRADESKILL MASTERY'),
        (264, 'REDUCE AA TIMER'),
        (265, 'NO FIZZLE'),
        (266, 'ADD 2H ATTACK CHANCE'),
        (267, 'ADD PET COMMANDS'),
        (268, 'ALCHEMY FAIL RATE'),
        (269, 'FIRST AID'),
        (270, 'EXTEND SONG RANGE'),
        (271, 'BASE RUN MOD'),
        (272, 'INCREASE CASTING LEVEL'),
        (273, 'DOTCRIT'),
        (274, 'HEALCRIT'),
        (275, 'MENDCRIT'),
        (276, 'DUAL WIELD AMT'),
        (277, 'EXTRA DI CHANCE'),
        (278, 'FINISHING BLOW'),
        (279, 'FLURRY'),
        (280, 'PET FLURRY'),
        (281, 'PET FEIGN'),
        (282, 'INCREASE BANDAGE AMT'),
        (283, 'WU ATTACK'),
        (284, 'IMPROVE LOH'),
        (285, 'NIMBLE EVASION'),
        (286, 'FOCUS DAMAGE AMT'),
        (287, 'FOCUS DURATION AMT'),
        (288, 'ADD PROC HIT'),
        (289, 'DOOM EFFECT'),
        (290, 'INCREASE RUN SPEED CAP'),
        (291, 'PURIFY'),
        (292, 'STRIKETHROUGH'),
        (293, 'STUN RESIST2'),
        (294, 'SPELL CRIT CHANCE'),
        (295, 'REDUCE SPECIAL TIMER'),
        (296, 'FOCUS DAMAGE MOD DETRIMENTAL'),
        (297, 'FOCUS DAMAGE AMT DETRIMENTAL'),
        (298, 'TINY COMPANION'),
        (299, 'WAKE DEAD'),
        (300, 'DOPPELGANGER'),
        (301, 'INCREASE RANGE DMG'),
        (302, 'FOCUS DAMAGE MOD CRIT'),
        (303, 'FOCUS DAMAGE AMT CRIT'),
        (304, 'SECONDARY RIPOSTE MOD'),
        (305, 'DAMAGE SHIELD MOD'),
        (306, 'WEAK DEAD 2'),
        (307, 'APPRAISAL'),
        (308, 'ZONE SUSPEND MINION'),
        (309, 'TELEPORT CASTERS BINDPOINT'),
        (310, 'FOCUS REUSE TIMER'),
        (311, 'FOCUS COMBAT SKILL'),
        (312, 'OBSERVER'),
        (313, 'FORAGE MASTER'),
        (314, 'IMPROVED INVIS'),
        (315, 'IMPROVED INVIS UNDEAD'),
        (316, 'IMPROVED INVIS ANIMALS'),
        (317, 'INCREASE WORN HP REGEN CAP'),
        (318, 'INCREASE WORN MANA REGEN CAP'),
        (319, 'CRITICAL HP REGEN'),
        (320, 'SHIELD BLOCK CHANCE'),
        (321, 'REDUCE TARGET HATE'),
        (322, 'GATE STARTING CITY'),
        (323, 'DEFENSIVE PROC'),
        (324, 'HP FOR MANA'),
        (325, 'NO BREAK AE SNEAK'),
        (326, 'ADD SPELL SLOTS'),
        (327, 'ADD BUFF SLOTS'),
        (328, 'INCREASE NEGATIVE HP LIMIT'),
        (329, 'MANA ABSORB PCT DMG'),
        (330, 'CRIT ATTACK MODIFIER'),
        (331, 'FAIL ALCHEMY ITEM RECOVERY'),
        (332, 'SUMMON TO CORPSE'),
        (333, 'DOOM RUNE EFFECT'),
        (334, 'NO MOVE HP'),
        (335, 'FOCUSED IMMUNITY'),
        (336, 'ILLUSIONARY TARGET'),
        (337, 'INCREASE EXP MOD'),
        (338, 'EXPEDIENT RECOVERY'),
        (339, 'FOCUS CASTING PROC'),
        (340, 'CHANCE SPELL'),
        (341, 'WORN ATTACK CAP'),
        (342, 'NO PANIC'),
        (343, 'SPELL INTERRUPT'),
        (344, 'ITEM CHANNELING'),
        (345, 'ASSASSINATE MAX LEVEL'),
        (346, 'HEADSHOT MAX LEVEL'),
        (347, 'DOUBLE RANGED ATTACK'),
        (348, 'FOCUS MANA MIN'),
        (349, 'INCREASE SHIELD DMG'),
        (350, 'MANABURN'),
        (351, 'SPAWN INTERACTIVE OBJECT'),
        (352, 'INCREASE TRAP COUNT'),
        (353, 'INCREASE SOI COUNT'),
        (354, 'DEACTIVATE ALL TRAPS'),
        (355, 'LEARN TRAP'),
        (356, 'CHANGE TRIGGER TYPE'),
        (357, 'FOCUS MUTE'),
        (358, 'INSTANT MANA'),
        (359, 'PASSIVE SENSE TRAP'),
        (360, 'PROC ON KILL SHOT'),
        (361, 'PROC ON DEATH'),
        (362, 'POTION BELT'),
        (363, 'BANDOLIER'),
        (364, 'ADD TRIPLE ATTACK CHANCE'),
        (365, 'PROC ON SPELL KILL SHOT'),
        (366, 'GROUP SHIELDING'),
        (367, 'MODIFY BODY TYPE'),
        (368, 'MODIFY FACTION'),
        (369, 'CORRUPTION'),
        (370, 'RESIST CORRUPTION'),
        (371, 'SLOW'),
        (372, 'GRANT FORAGING'),
        (373, 'DOOM ALWAYS'),
        (374, 'TRIGGER SPELL'),
        (375, 'CRIT DOT DMG MOD'),
        (376, 'FLING'),
        (377, 'DOOM ENTITY'),
        (378, 'RESIST OTHER SPA'),
        (379, 'DIRECTIONAL TELEPORT'),
        (380, 'EXPLOSIVE KNOCKBACK'),
        (381, 'FLING TOWARD'),
        (382, 'SUPPRESSION'),
        (383, 'FOCUS CASTING PROC NORMALIZED'),
        (384, 'FLING AT'),
        (385, 'FOCUS WHICH GROUP'),
        (386, 'DOOM DISPELLER'),
        (387, 'DOOM DISPELLEE'),
        (388, 'SUMMON ALL CORPSES'),
        (389, 'REFRESH SPELL TIMER'),
        (390, 'LOCKOUT SPELL TIMER'),
        (391, 'FOCUS MANA MAX'),
        (392, 'FOCUS HEAL AMT'),
        (393, 'FOCUS HEAL MOD BENEFICIAL'),
        (394, 'FOCUS HEAL AMT BENEFICIAL'),
        (395, 'FOCUS HEAL MOD CRIT'),
        (396, 'FOCUS HEAL AMT CRIT'),
        (397, 'ADD PET AC'),
        (398, 'FOCUS SWARM PET DURATION'),
        (399, 'FOCUS TWINCAST CHANCE'),
        (400, 'HEALBURN'),
        (401, 'MANA IGNITE'),
        (402, 'ENDURANCE IGNITE'),
        (403, 'FOCUS SPELL CLASS'),
        (404, 'FOCUS SPELL SUBCLASS'),
        (405, 'STAFF BLOCK CHANCE'),
        (406, 'DOOM LIMIT USE'),
        (407, 'DOOM FOCUS USED'),
        (408, 'LIMIT HP'),
        (409, 'LIMIT MANA'),
        (410, 'LIMIT ENDURANCE'),
        (411, 'FOCUS LIMIT CLASS'),
        (412, 'FOCUS LIMIT RACE'),
        (413, 'FOCUS BASE EFFECTS'),
        (414, 'FOCUS LIMIT SKILL'),
        (415, 'FOCUS LIMIT ITEM CLASS'),
        (416, 'AC2'),
        (417, 'MANA2'),
        (418, 'FOCUS INCREASE SKILL DMG 2'),
        (419, 'PROC EFFECT 2'),
        (420, 'FOCUS LIMIT USE'),
        (421, 'FOCUS LIMIT USE AMT'),
        (422, 'FOCUS LIMIT USE MIN'),
        (423, 'FOCUS LIMIT USE TYPE'),
        (424, 'GRAVITATE'),
        (425, 'FLY'),
        (426, 'ADD EXTENDED TARGET SLOTS'),
        (427, 'SKILL PROC'),
        (428, 'PROC SKILL MODIFIER'),
        (429, 'SKILL PROC SUCCESS'),
        (430, 'POST EFFECT'),
        (431, 'POST EFFECT DATA'),
        (432, 'EXPAND MAX ACTIVE TROPHY BENEFITS'),
        (433, 'ADD NORMALIZED SKILL MIN DMG AMT'),
        (434, 'ADD NORMALIZED SKILL MIN DMG AMT 2'),
        (435, 'FRAGILE DEFENSE'),
        (436, 'FREEZE BUFF TIMER'),
        (437, 'TELEPORT TO ANCHOR'),
        (438, 'TRANSLOCATE TO ANCHOR'),
        (439, 'ASSASSINATE'),
        (440, 'FINISHING BLOW MAX'),
        (441, 'DISTANCE REMOVAL'),
        (442, 'REQUIRE TARGET DOOM'),
        (443, 'REQUIRE CASTER DOOM'),
        (444, 'IMPROVED TAUNT'),
        (445, 'ADD MERC SLOT'),
        (446, 'STACKER A'),
        (447, 'STACKER B'),
        (448, 'STACKER C'),
        (449, 'STACKER D'),
        (450, 'DOT GUARD'),
        (451, 'MELEE THRESHOLD GUARD'),
        (452, 'SPELL THRESHOLD GUARD'),
        (453, 'MELEE THRESHOLD DOOM'),
        (454, 'SPELL THRESHOLD DOOM'),
        (455, 'ADD HATE PCT'),
        (456, 'ADD HATE OVER TIME PCT'),
        (457, 'RESOURCE TAP'),
        (458, 'FACTION MOD'),
        (459, 'SKILL DAMAGE MOD 2'),
        (460, 'OVERRIDE NOT FOCUSABLE'),
        (461, 'FOCUS DAMAGE MOD 2'),
        (462, 'FOCUS DAMAGE AMT 2'),
        (463, 'SHIELD'),
        (464, 'PC PET RAMPAGE'),
        (465, 'PC PET AE RAMPAGE'),
        (466, 'PC PET FLURRY'),
        (467, 'DAMAGE SHIELD MITIGATION AMT'),
        (468, 'DAMAGE SHIELD MITIGATION PCT'),
        (469, 'CHANCE BEST IN SPELL GROUP'),
        (470, 'TRIGGER BEST IN SPELL GROUP'),
        (471, 'DOUBLE MELEE ATTACKS'),
        (472, 'AA BUY NEXT RANK'),
        (473, 'DOUBLE BACKSTAB FRONT'),
        (474, 'PET MELEE CRIT DMG MOD'),
        (475, 'TRIGGER SPELL NON ITEM'),
        (476, 'WEAPON STANCE'),
        (477, 'HATELIST TO TOP'),
        (478, 'HATELIST TO TAIL'),
        (479, 'FOCUS LIMIT MIN VALUE'),
        (480, 'FOCUS LIMIT MAX VALUE'),
        (481, 'FOCUS CAST SPELL ON LAND'),
        (482, 'SKILL BASE DAMAGE MOD'),
        (483, 'FOCUS INCOMING DMG MOD'),
        (484, 'FOCUS INCOMING DMG AMT'),
        (485, 'FOCUS LIMIT CASTER CLASS'),
        (486, 'FOCUS LIMIT SAME CASTER'),
        (487, 'EXTEND TRADESKILL CAP'),
        (488, 'DEFENDER MELEE FORCE PCT'),
        (489, 'WORN ENDURANCE REGEN CAP'),
        (490, 'FOCUS MIN REUSE TIME'),
        (491, 'FOCUS MAX REUSE TIME'),
        (492, 'FOCUS ENDURANCE MIN'),
        (493, 'FOCUS ENDURANCE MAX'),
        (494, 'PET ADD ATK'),
        (495, 'FOCUS DURATION MAX'),
        (496, 'CRIT MELEE DMG MOD MAX'),
        (497, 'FOCUS CAST PROC NO BYPASS'),
        (498, 'ADD EXTRA PRIMARY ATTACK PCT'),
        (499, 'ADD EXTRA SECONDARY ATTACK PCT'),
        (500, 'FOCUS CAST TIME MOD2'),
        (501, 'FOCUS CAST TIME AMT'),
        (502, 'FEARSTUN'),
        (503, 'MELEE DMG POSITION MOD'),
        (504, 'MELEE DMG POSITION AMT'),
        (505, 'DMG TAKEN POSITION MOD'),
        (506, 'DMG TAKEN POSITION AMT'),
        (507, 'AMPLIFY MOD'),
        (508, 'AMPLIFY AMT'),
        (509, 'HEALTH TRANSFER'),
        (510, 'FOCUS RESIST INCOMING'),
        (511, 'FOCUS TIMER MIN'),
        (512, 'PROC TIMER MOD'),
        (513, 'MANA MAX'),
        (514, 'ENDURANCE MAX'),
        (515, 'AC AVOIDANCE MAX'),
        (516, 'AC MITIGATION MAX'),
        (517, 'ATTACK OFFENSE MAX'),
        (518, 'ATTACK ACCURACY MAX'),
        (519, 'LUCK AMT'),
        (520, 'LUCK PCT'),
        (521, 'ENDURANCE ABSORB PCT DMG'),
        (522, 'INSTANT MANA PCT'),
        (523, 'INSTANT ENDURANCE PCT'),
        (524, 'DURATION HP PCT'),
        (525, 'DURATION MANA PCT'),
        (526, 'DURATION ENDURANCE PCT'),
    ]
)
