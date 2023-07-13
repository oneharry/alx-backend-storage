-- implement trigger after adding to table
DELIMITER $$
CREATE TRIGGER place_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END $$

DELIMITER ;
