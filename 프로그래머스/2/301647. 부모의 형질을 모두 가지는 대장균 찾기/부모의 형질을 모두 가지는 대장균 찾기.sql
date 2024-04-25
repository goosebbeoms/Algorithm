SELECT child.id, child.genotype, parent.genotype AS parent_genotype
FROM ecoli_data parent INNER JOIN ecoli_data child
    on parent.id = child.parent_id
WHERE (parent.genotype & child.genotype) != 0;