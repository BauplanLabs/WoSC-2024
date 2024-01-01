-- This is a simple query that retrieves some columns from the titanic table to 
-- start the pipeline.

-- bauplan: materialize=false
SELECT
    Age,    
    Fare,
    PassengerId,
    Pclass,
    Embarked,
    Sex,
    Survived
FROM
    titanic