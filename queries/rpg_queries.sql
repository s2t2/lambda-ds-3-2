-- how many characters of each subclass?
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









-- How many Weapons does each character have? 
-- (Return first 20 rows) 
-- row per character (302, including ones that have zero)
-- three cols: char id, char name, weapon_count

SELECT 
  c.character_id
  ,c.name as character_name
  -- ,inv.item_id
  -- ,w.item_ptr_id as weapon_id
  ,count(distinct w.item_ptr_id) as weapon_count
FROM charactercreator_character c
LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
LEFT JOIN armory_weapon w ON w.item_ptr_id = inv.item_id
GROUP BY c.character_id

