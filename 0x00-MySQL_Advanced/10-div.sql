-- create a function that divides and returns  first and second number
-- or returns 0 if the second number is equals 0
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT DETERMINISTIC
BEGIN
	IF b == 0 THEN
		RETURN 0
	ELSE 
		RETURN (a / b)
	END IF;
END;
