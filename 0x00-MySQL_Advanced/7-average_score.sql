-- creates a stored procedure that computes and stores students avg score
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average FLOAT;
    SELECT AVG(score) INTO average
    FROM corrections AS c
    WHERE c.user_id = user_id;

    UPDATE users
    SET average_score = average
    WHERE id = user_id;
END $$

DELIMITER ;
