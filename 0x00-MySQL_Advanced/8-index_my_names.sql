-- index he first letter of name on names table
CREATE INDEX index_name ON names(LEFT(name, 1));
