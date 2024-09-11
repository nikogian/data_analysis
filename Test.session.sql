-- Create a new table with the desired columns
CREATE TABLE properties_temp AS
SELECT displayAddress, bathrooms, bedrooms, price, verified, furnishing, sizeMin
FROM properties;

-- Drop the old table
DROP TABLE properties;

-- Rename the new table to the original table name
ALTER TABLE properties_temp RENAME TO properties;
