-- create index on the first letter of name on names table
CREATE INDEX idx_name_first ON names (name(1));
