-- Create a new table using the existing data with necessary modifications
CREATE TABLE properties_clean AS
SELECT 
    displayAddress, 
    CAST(bathrooms AS INTEGER) AS bathrooms, 
    CAST(bedrooms AS INTEGER) AS bedrooms, 
    CAST(price * 0.24737 AS INTEGER) AS price, -- Currency conversion to Euros 
    CASE 
        WHEN verified = True THEN 1 
        ELSE 0 
    END AS verified, -- Dropping the False verified values
    CASE 
        WHEN furnishing = 'YES' THEN 1 
        ELSE 0 
    END AS furnishing,
    CASE
        WHEN sizeMin LIKE '%sqft%' THEN CAST(REPLACE(sizeMin, ' sqft', '') AS FLOAT) * 0.092903
        ELSE CAST(sizeMin AS FLOAT)
    END AS sizeMin
FROM properties;

-- Drop the old table
-- DROP TABLE properties;

-- Rename the new table to the original table name
-- ALTER TABLE properties_temp RENAME TO properties;

SELECT name 
FROM sqlite_master 
WHERE type = 'table' 
  AND name = 'properties_clean';

SELECT * 
FROM properties_clean 
LIMIT 50;



