-- creates a stored procedure that computes and stores students avg score
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	    DECLARE avgerage FLOAT;
	    SELECT AVG(score) INTO avgerage
	    FROM corrections
	    WHERE user_id = user_id;

	    UPDATE users
	    SET average_score = avgerage
	    WHERE id = user_id;
END $$

DELIMITER ;
