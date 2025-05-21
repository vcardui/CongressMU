-- +----------------------------------------------------------------------------+
-- | CARDUI WORKS v1.0.0
-- +----------------------------------------------------------------------------+
-- | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
-- | Vanessa Reteguín <vanessa@reteguin.com>
-- | Released under the MIT license
-- | www.cardui.com/carduiframework/license/license.txt
-- +----------------------------------------------------------------------------+
-- | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
-- | First release: May 18th, 2025
-- | Last update..: May 18th, 2025
-- | WhatIs.......: CongressMU - Data
-- | DBMS.........: MariaDB
-- +----------------------------------------------------------------------------+
--
--
--
INSERT INTO
    mucuser (userlogin, userpassword, firstname, lastName, email, title, specialty)
VALUES
    (
        'vanessa@reteguin.com',
        'rememberToChangeThePasswordYouSilly',
        'Vanessa',
        'Reteguín',
        'vanessa@reteguin.com',
        'Ing.',
        'Dormir'
    ),
    (
        'carduibot@gmail.com',
        'thisIsCarduiBotsPassword',
        'Cardui',
        'Bot',
        'carduibot@gmail.com',
        NULL,
        '11111101000'
    );



INSERT INTO
    question (idquestion, phrase)
VALUES
    (1, '¿Hay claridad en el propósito u objetivo de la investigación o del texto?'),
    (
        2,
        '¿Se presentan datos de forma clara y ordenada, se informa su origen y se evidencia su relación con el texto?'
    ),
    (
        3,
        'En caso de que el texto incluya hipótesis, ¿éstas se encuentran explicitadas de manera clara y articuladas con la introducción y la teoría? ¿Los resultados aportan conceptualización o contribuyen a resolver un problema?'
    ),
    (
        4,
        '¿Hay precisión de las definiciones conceptuales? ¿Se evidencia rigor en la recolección de los datos? (sistematización).'
    ),
    (5, '¿El artículo sigue el formato APA?');



INSERT INTO
    evaluatedquestion (idevaluationquestion, idquestion, score, idpartialevaluation)
VALUES
    (1, 1, 5, 1),
    (2, 2, 5, 1),
    (3, 3, 5, 1),
    (4, 4, 5, 1),
    (5, 5, 5, 1),
    (6, 1, 4, 2),
    (7, 2, 4, 2),
    (8, 3, 4, 2),
    (9, 4, 4, 2),
    (10, 5, 4, 2);



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



INSERT INTO
    partialevaluation (idpartialevaluation, evaluator, meanscore, resolution, evaluationcomment)
VALUES
    (1, 1, 0, 'not-accepted', 'May the force be with you'),
    (2, 1, 0, 'accepted-no-modifications', 'Im Marcel Ive got a face and hmm shoes');



-- DROP TABLE IF EXISTS partialevaluation;
CREATE TABLE
    partialevaluation (
        idpartialevaluation INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
        --
        evaluator INT UNSIGNED NOT NULL,
        --
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
        FOREIGN KEY (evaluator) REFERENCES mucuser (idmucuser)
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