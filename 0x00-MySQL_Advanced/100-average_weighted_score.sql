-- ceate a procedure that calculates weighted average
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE average FLOAT;
	SELECT SUM(score * weight) / SUM(weight)
	INTO average
	FROM corrections AS c
	JOIN projects AS p
	ON c.project_id = p.id
	WHERE c.user_id = user_id;

	UPDATE users
	SET average_score = average
	WHERE id = user_id;
END $$

DELIMITER ;
