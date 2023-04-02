CREATE DATABASE BugSearch;
USE BugSearch;

-- TABLE FOR USER
CREATE TABLE Users
(
    user_id INT NOT NULL AUTO_INCREMENT,
    passcode INT NOT NULL,
    username VARCHAR(20) NOT NULL,
    email_id VARCHAR(30) NOT NULL,
    creation_date DATE NOT NULL,
    profile_image_url VARCHAR(30),
    reputation INT NOT NULL DEFAULT 0,
    about TEXT,
    badge VARCHAR(30) NOT NULL DEFAULT "newbie",
    nfollowers INT NOT NULL DEFAULT 0,
    nfollowing INT NOT NULL DEFAULT 0,
    PRIMARY KEY (user_id)
);

-- TABLE FOR Answers
CREATE TABLE Answers
(
    answer_id INT NOT NULL AUTO_INCREMENT,
    body TEXT NOT NULL,
    question_id INT NOT NULL,
    user_id INT NOT NULL,
    score INT DEFAULT 0,
    creation_date DATE NOT NULL,
    comment_count INT NOT NULL DEFAULT 0,
    upvotes INT NOT NULL DEFAULT 0,
    downvotes INT NOT NULL DEFAULT 0,
    PRIMARY KEY (answer_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id) 
);

-- table for questions
CREATE TABLE Questions
(
    question_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(100),
    body TEXT NOT NULL,
    answer_id INT ,
    user_id INT NOT NULL,
    score INT NOT NULL DEFAULT 0,
    creation_date DATE NOT NULL,
    comment_count INT NOT NULL DEFAULT 0,
    answer_count INT NOT NULL DEFAULT 0,
    upvotes INT NOT NULL DEFAULT 0,
    downvotes INT NOT NULL DEFAULT 0,
    PRIMARY KEY (question_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (answer_id) REFERENCES Answers(answer_id)
);
ALTER TABLE Answers ADD FOREIGN KEY (question_id) REFERENCES Questions(question_id) ON DELETE CASCADE;


--
CREATE TABLE Comments
(
    comment_id INT NOT NULL AUTO_INCREMENT,
    body TEXT NOT NULL,
    creation_date DATE NOT NULL,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    post_type ENUM('question', 'answer') NOT NULL,
    PRIMARY KEY (comment_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (post_id) REFERENCES Questions(question_id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES Answers(answer_id) ON DELETE CASCADE
);

CREATE TABLE Votes
(
    vote_id INT NOT NULL AUTO_INCREMENT,
    vote_type ENUM('upvote', 'downvote') NOT NULL,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    post_type ENUM('question', 'answer') NOT NULL,
    PRIMARY KEY (vote_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (post_id) REFERENCES Questions(question_id) ON DELETE CASCADE,
    FOREIGN KEY (post_id) REFERENCES Answers(answer_id) ON DELETE CASCADE
);

CREATE TABLE Tags
(
    tag_id INT NOT NULL AUTO_INCREMENT,
    tag_name VARCHAR(20) NOT NULL,
    about TEXT NOT NULL
);

CREATE TABLE Follwertags
(
    follower_id INT NOT NULL,
    following_id INT NOT NULL
);

CREATE TABLE Usertags
(
    tag_id INT NOT NULL,
    user_id INT NOT NULL
);

CREATE TABLE Questiontags
(
    tag_id INT NOT NULL,
    question_id INT NOT NULL
);


----
CREATE TRIGGER update_badge
BEFORE UPDATE ON Users 
FOR EACH ROW
BEGIN
        IF NEW.reputation >= 20 AND NEW.reputation < 40 THEN
            SET NEW.badge = 'Pupil';
        ELSEIF NEW.reputation >= 40 AND NEW.reputation < 70 THEN
            SET NEW.badge = 'Specialist';
        ELSEIF NEW.reputation >= 70 AND NEW.reputation < 100 THEN
            SET NEW.badge = 'Expert';
        ELSEIF NEW.reputation >= 100 AND NEW.reputation < 120 THEN
            SET NEW.badge = 'Candidate Master';
        ELSEIF NEW.reputation >= 120 AND NEW.reputation < 130 THEN
            SET NEW.badge = 'Master';
        ELSEIF NEW.reputation >= 130 AND NEW.reputation < 140 THEN
            SET NEW.badge = 'International Master';
        ELSEIF NEW.reputation >= 140 AND NEW.reputation < 150 THEN
            SET NEW.badge = 'Grandmaster';
        ELSEIF NEW.reputation >= 150 AND NEW.reputation < 200 THEN
            SET NEW.badge = 'International Grandmaster';
        ELSEIF NEW.reputation >= 200 THEN
            SET NEW.badge = 'Legendary Grandmaster';
        END IF;
    END IF;
END;
