-- +----------------------------------------------------------------------------+
-- | CARDUI WORKS v1.0.0
-- +----------------------------------------------------------------------------+
-- | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
-- | Vanessa Reteguín <vanessa@reteguin.com>
-- | Released under the MIT license
-- | www.cardui.com/carduiframework/license/license.txt
-- +----------------------------------------------------------------------------+
-- | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
-- | First release: April 7th, 2025
-- | Last update..: May 18th, 2025
-- | WhatIs.......: CongressMU - Scheme
-- | DBMS.........: MariaDB
-- +----------------------------------------------------------------------------+
--
--
--
-- DROP TABLE IF EXISTS mucuser;
CREATE TABLE
    mucuser (
        idmucuser INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
        --
        userlogin VARCHAR(64) UNIQUE NOT NULL,
        userpassword VARCHAR(96) NOT NULL,
        --
        firstname VARCHAR(64) NOT NULL,
        lastName VARCHAR(64) NOT NULL,
        email VARCHAR(128) NOT NULL,
        title ENUM ('Lic.', 'Ing.', 'Arq.', 'Mtr.', 'Phd.'),
        specialty VARCHAR(64),
        --
        PRIMARY KEY (idmucuser)
    ) ENGINE = InnoDB DEFAULT CHARACTER
SET
    = utf8;



-- DROP TABLE IF EXISTS question;
CREATE TABLE
    question (
        idquestion INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
        --
        phrase VARCHAR(128) NOT NULL,
        --
        PRIMARY KEY (idquestion)
    ) ENGINE = InnoDB DEFAULT CHARACTER
SET
    = utf8;



-- DROP TABLE IF EXISTS evaluatedquestion;
CREATE TABLE
    evaluatedquestion (
        idevaluationquestion INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
        --
        idquestion INT UNSIGNED NOT NULL,
        score TINYINT UNSIGNED,
        idpartialevaluation INT UNSIGNED NOT NULL,
        --
        PRIMARY KEY (idevaluationquestion),
        FOREIGN KEY (idquestion) REFERENCES question (idquestion),
        FOREIGN KEY (idpartialevaluation) REFERENCES partialevaluation (idpartialevaluation)
    ) ENGINE = InnoDB DEFAULT CHARACTER
SET
    = utf8;



-- DROP TABLE IF EXISTS partialevaluation;
CREATE TABLE
    partialevaluation (
        idpartialevaluation INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
        --
        evaluator INT UNSIGNED NOT NULL,
        --
        idevaluationquestion INT UNSIGNED NOT NULL,
        meanscore FLOAT DEFAULT 0,
        resolution ENUM (
            'accepted-no-modifications',
            'accepted-basic-modifications',
            'accepted-structural-modifications',
            'rewrite-content',
            'not-accepted'
        ) NOT NULL,
        evaluationcomment VARCHAR(128),
        --
        PRIMARY KEY (idpartialevaluation),
        FOREIGN KEY (evaluator) REFERENCES mucuser (idmucuser),
        FOREIGN KEY (idevaluationquestion) REFERENCES evaluationquestion (idevaluationquestion)
    ) ENGINE = InnoDB DEFAULT CHARACTER
SET
    = utf8;



-- DROP TABLE IF EXISTS mucarticle;
CREATE TABLE
    mucarticle (
        idmucarticle INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
        --
        author INT UNSIGNED NOT NULL,
        title VARCHAR(128) NOT NULL,
        category ENUM ('inclusion', 'educational-technology', 'school-on-the-cloud') NOT NULL,
        articleroute VARCHAR(128) NOT NULL,
        submissionComment VARCHAR(255),
        --
        idpartialevaluation INT UNSIGNED NOT NULL,
        partialevaluationmean FLOAT DEFAULT 0,
        finalevaluation ENUM (
            'accepted-no-modifications',
            'accepted-basic-modifications',
            'accepted-structural-modifications',
            'rewrite-content',
            'not-accepted'
        ) NOT NULL,
        --
        mailsent BOOL NOT NULL DEFAULT 0,
        --
        PRIMARY KEY (idmucarticle),
        FOREIGN KEY (author) REFERENCES mucuser (idmucuser),
        FOREIGN KEY (idpartialevaluation) REFERENCES partialevaluation (idpartialevaluation)
    ) ENGINE = InnoDB DEFAULT CHARACTER
SET
    = utf8;



-- DROP TABLE IF EXISTS mucuserarticle;
CREATE TABLE
    mucuserarticle (
        idmucuser INT UNSIGNED NOT NULL,
        --
        idmucarticle INT UNSIGNED NOT NULL,
        --
        UNIQUE KEY (idmucuser, idmucarticle),
        FOREIGN KEY (idmucuser) REFERENCES mucuser (idmucuser),
        FOREIGN KEY (idmucarticle) REFERENCES mucarticle (idmucarticle)
    ) ENGINE = InnoDB DEFAULT CHARACTER
SET
    = utf8;



-- DROP TABLE IF EXISTS partialevaluationquestion;
CREATE TABLE
    partialevaluationquestion (
        idevaluationquestion INT UNSIGNED NOT NULL,
        --
        idpartialevaluation INT UNSIGNED NOT NULL,
        --
        UNIQUE KEY (idevaluationquestion, idpartialevaluation),
        FOREIGN KEY (idevaluationquestion) REFERENCES evaluationquestion (idevaluationquestion),
        FOREIGN KEY (idpartialevaluation) REFERENCES partialevaluation (idpartialevaluation)
    ) ENGINE = InnoDB DEFAULT CHARACTER
SET
    = utf8;



-- DROP TABLE IF EXISTS mucpartialevaluationarticle;
CREATE TABLE
    mucpartialevaluationarticle (
        idpartialevaluation INT UNSIGNED NOT NULL,
        --
        idmucarticle INT UNSIGNED NOT NULL,
        --
        UNIQUE KEY (idpartialevaluation, idmucarticle),
        FOREIGN KEY (idpartialevaluation) REFERENCES partialevaluation (idpartialevaluation),
        FOREIGN KEY (idmucarticle) REFERENCES mucarticle (idmucarticle)
    ) ENGINE = InnoDB DEFAULT CHARACTER
SET
    = utf8;