BEGIN TRANSACTION;

/* Create a table called NAMES */
CREATE TABLE marks(STUDENT_ID integer, MARKS integer);

/* Create few records in this table */
INSERT INTO marks VALUES(1,350);
INSERT INTO marks VALUES(2,54);
INSERT INTO marks VALUES(1,760);
INSERT INTO marks VALUES(3,250);
INSERT INTO marks VALUES(3,300);
INSERT INTO marks VALUES(4,250);
INSERT INTO marks VALUES(1,270);
INSERT INTO marks VALUES(5,300);
INSERT INTO marks VALUES(4,340);
INSERT INTO marks VALUES(5,250);
COMMIT;

/* select student id and marks where marks sum is greater than 500 */
SELECT STUDENT_ID, S FROM (SELECT STUDENT_ID, SUM(MARKS) AS S FROM marks GROUP BY STUDENT_ID) WHERE S >= 500;
