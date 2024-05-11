-- computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avrage FLOAT;
	SET avrage = (SELECT AVG(score) FROM corrections WHERE user_id = user_id);
	UPDATE users
	SET average_score = avrage
	WHERE user_id = user_id;
END $$
DELIMITER $$
