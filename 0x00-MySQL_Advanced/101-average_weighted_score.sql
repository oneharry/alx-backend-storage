-- create procedure tocomputes and return the avg weighted of all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users as u, (SELECT u.id, SUM(score * weight) / SUM(weight) AS w
		FROM users AS u
		JOIN corrections AS c
		ON u.id = c.user_id
		JOIN projects AS p
		ON c.project_id = p.id
		GROUP BY u.id) AS w_avg
	SET u.average_score = w_avg.w
	WHERE u.id = w_avg.id;
END $$

DELIMITER ;
