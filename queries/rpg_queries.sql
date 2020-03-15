
select
  ch.character_id
  ,ch.name
  ,cl.*
  ,CASE
  WHEN cl.character_ptr_id is not null THEN "cleric"
  -- WHEN f.character_ptr_id is not null THEN "fighter"
  -- WHEN n.mage_ptr_id is not null THEN "mage-necro"
  -- WHEN m.character_ptr_id is not null THEN "mage"
  -- WHEN th.character_ptr_id is not null THEN "thief"
  ELSE "todo"
  END as char_type
from charactercreator_character as ch
left join charactercreator_cleric as cl on ch.character_id = cl.character_ptr_id



-- row per character (302 total)
select
  CASE
  WHEN cl.character_ptr_id is not null THEN "cleric"
  WHEN f.character_ptr_id is not null THEN "fighter"
  WHEN n.mage_ptr_id is not null THEN "mage-necro"
  WHEN m.character_ptr_id is not null THEN "mage"
  WHEN th.character_ptr_id is not null THEN "thief"
  ELSE "todo"
  END as char_type
  ,count(distinct ch.character_id) as char_count
from charactercreator_character as ch
left join charactercreator_cleric as cl on ch.character_id = cl.character_ptr_id
left join charactercreator_fighter as f on ch.character_id = f.character_ptr_id
left join charactercreator_mage as m on ch.character_id = m.character_ptr_id
left join charactercreator_thief as th on ch.character_id = th.character_ptr_id
-- left join charactercreator_necromancer as n on ch.character_id = n.character_ptr_id
left join charactercreator_necromancer as n on m.character_ptr_id = n.mage_ptr_id
group by char_type




-- select * from sqlite_master

-- PRAGMA table_info(armory_item)

pragma table_info(charactercreator_character_inventory)

pragma foreign_key_list(charactercreator_character_inventory)
