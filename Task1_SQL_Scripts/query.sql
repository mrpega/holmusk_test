select
   c.concept_name AS gender_name,
   EXTRACT(year from age(now(), birth_datetime)) AS person_age,
   COUNT(p.person_id) AS num_persons
from
    cdm_schema.person p 
    LEFT JOIN cdm_schema.CONCEPT c
    ON p.gender_concept_id = c.concept_id
WHERE 
-- select persons who are between 35 and 60 years old(inclusive)
EXTRACT(year from age(now(), birth_datetime)) BETWEEN 35 and 60
GROUP BY 
c.concept_name, EXTRACT(year from age(now(), birth_datetime))


-- improvement by avoiding function in the query

select
   c.concept_name AS gender_name,
   year_of_birth,
   COUNT(p.person_id) AS num_persons
from
    cdm_schema.person p 
    LEFT JOIN cdm_schema.CONCEPT c
    ON p.gender_concept_id = c.concept_id
WHERE 
-- select persons who are between 35 and 60 years old(inclusive)
year_of_birth >=1962 and year_of_birth<=1987 
GROUP BY 
c.concept_name, year_of_birth