SELECT I.animal_id, I.animal_type, I.name
FROM animal_ins I
INNER JOIN animal_outs O
ON I.animal_id = O.animal_id
WHERE (I.sex_upon_intake IN ('Intact Male', 'Intact Female'))
    AND (O.sex_upon_outcome IN ('Neutered Male', 'Spayed Female'))
ORDER BY I.animal_id ASC;