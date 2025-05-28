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
-- | Last update..: May 27th, 2025
-- | WhatIs.......: CongressMU - Data
-- | DBMS.........: MariaDB
-- +----------------------------------------------------------------------------+
--
--
--
------------------- Test users -------------------
INSERT INTO
    mucuser (idmucuser, userkind, userlogin, userhash, firstname, lastName, email, title, specialty)
VALUES
    (
        1,
        'Administrator',
        'vanessa@reteguin.com ',
        '$2b$12$15lsouk5nmYP44CvQwrqeuRa0SeK/yUIRXVCe.hl3S1jPTGtFPg.2',
        'Vanessa',
        'Skywalker Amidala',
        'vanessa@reteguin.com',
        'Ing.',
        'Dormir'
    ),
    (
        2,
        'Evaluator',
        'carduibot@gmail.com',
        '$2b$12$ptjjKMasUPtymQF5MKmQseYe1OWPwhvFnfKb5Y/PEdNtemflCfCt6',
        'Cardui',
        'Bot Gmail',
        'carduibot@gmail.com',
        'Phd.',
        'gmail 11111101000'
    ),
    (
        3,
        'Author',
        'carduibot@yahoo.com',
        '$2b$12$nOZUDKnI25s7gZFH/66YBOM0b1bGvvZsMrJNQgyDWqsRgiP8v.P8S',
        'Cardui',
        'Bot Yahoo',
        'carduibot@yahoo.com',
        'Lic.',
        'yahoo 11111101000'
    );



------------------- Evaluation question phrases -------------------
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



------------------- Evaluation question score -------------------
/*INSERT INTO
evaluationquestion (idquestion, score)
VALUES
(1, NULL),
(2, NULL),
(3, NULL),
(4, NULL),
(5, NULL);
 */
------------------- Evaluation Dummy values -------------------
/*
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



INSERT INTO
partialevaluation (idpartialevaluation, evaluator, meanscore, resolution, evaluationcomment)
VALUES
(1, 1, 0, 'not-accepted', 'May the force be with you'),
(2, 1, 0, 'accepted-no-modifications', 'Im Marcel Ive got a face and hmm shoes');
 */
--
--
--
------------------- Get user kind -------------------
/*
SELECT
A.userkind
FROM
mucuser A
INNER JOIN musession B ON A.idmucuser = B.idmucuser
WHERE
B.sessionnumber = '_jW46vM7Dpn3UsYt6TlSV6tc6_cXAbvyW8C0Z8Gw4wE';
 */
--
--
--
------------------- Sesssion / User match -------------------
/*
INSERT INTO
musession (idmucuser, sessionnumber)
SELECT
idmucuser,
'ThedammnumberYouSillyOMG'
FROM
mucuser
WHERE
userlogin = 'vanessa@reteguin.com';
 */
--
--
--
------------------- Set session endtime -------------------
/*
UPDATE musession
SET
endtime = '2025-05-26 14:08:37'
WHERE
sessionnumber = 'ThedammnumberYouSilly';

UPDATE musession
SET
endtime = CURRENT_TIMESTAMP
WHERE
sessionnumber = 'ThedammnumberYouSilly'
AND CURRENT_TIMESTAMP <= endtime + INTERVAL 1 HOUR;
 */
--
--
--
------------------- Insert session-user relationship -------------------
/*
INSERT INTO
musession (idmucuser, sessionnumber)
SELECT
idmucuser,
'{user_session}'
FROM
mucuser
WHERE
userlogin = '{form.data[' email ']}'
AND NOT EXISTS (
SELECT
 *
FROM
musession
WHERE
sessionnumber = '{user_session}'
);
 */
--
--
--------------------- Fetch user data through session id -------------------
/*
SELECT
A.idmucuser, A.userkind, A.email, A.firstname, A.lastName, A.title, A.specialty
FROM
mucuser A
INNER JOIN musession B ON A.idmucuser = B.idmucuser
WHERE
B.sessionnumber = 'o9DdMq7_WuuEK4smrrD_1catQLo7h2nciamgITbbIOQ';
 */
--
--
--
--------------------- Fetch user data through session id -------------------
/*
SELECT
title
FROM
mucarticle
WHERE
author = 1;
 */
--
--
--
------------------- New partial evaluation questions set (+ get inserted IDs) -------------------
-- Save IDs: {id de la pregunt1}, {id de la pregunt2}, {id de la pregunt3}, {id de la pregunt4}, {id de la pregunt5}
INSERT INTO
    evaluationquestion (idquestion, score)
VALUES
    (1, NULL),
    (2, NULL),
    (3, NULL),
    (4, NULL),
    (5, NULL) RETURNING idevaluationquestion;



------------------- New partial evaluation (+ get evaluation ID) -------------------
-- Save ID: {id de la evaluación}
INSERT INTO
    partialevaluation (evaluator, meanscore, resolution, evaluationcomment)
VALUES
    ('{id del evaluador}', NULL, NULL, NULL),
    RETURNING idevaluationquestion;



------------------- New Relation: partial evaluation <-> questions -------------------
INSERT INTO
    partialevaluationquestion (idevaluationquestion, idpartialevaluation)
VALUES
    ('{id de la pregunt1}', '{id de la evaluación}'),
    ('{id de la pregunt2}', '{id de la evaluación}'),
    ('{id de la pregunt3}', '{id de la evaluación}'),
    ('{id de la pregunt4}', '{id de la evaluación}'),
    ('{id de la pregunt5}', '{id de la evaluación}');



------------------- New Article -------------------
INSERT INTO
    mucarticle (
        author,
        title,
        category,
        articleroute,
        submissionComment,
        partialevaluationmean,
        finalevaluation,
        mailsent
    )
SELECT
    idmucuser,
    '{title}',
    'inclusion',
    'ruta',
    'comentario',
    NULL,
    NULL,
    FALSE
FROM
    musession
WHERE
    sessionnumber = 'o9DdMq7_WuuEK4smrrD_1catQLo7h2nciamgITbbIOQ';



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
        partialevaluationmean FLOAT DEFAULT 0,
        finalevaluation ENUM (
            'accepted-no-modifications',
            'accepted-basic-modifications',
            'accepted-structural-modifications',
            'rewrite-content',
            'not-accepted'
        ),
        --
        mailsent BOOL NOT NULL DEFAULT 0,
        --
        PRIMARY KEY (idmucarticle),
        FOREIGN KEY (author) REFERENCES mucuser (idmucuser)
    ) ENGINE = InnoDB DEFAULT CHARACTER
SET
    = utf8;