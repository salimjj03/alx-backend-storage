-- computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avrage FLOAT;
	SET avrage = (SELECT AVG(score) FROM corrections as C WHERE C.user_id = user_id);
	UPDATE users
	SET average_score = avrage
	WHERE id = user_id;
END $$
DELIMITER $$
