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
-- | Last update..: May 26th, 2025
-- | WhatIs.......: CongressMU - Data
-- | DBMS.........: MariaDB
-- +----------------------------------------------------------------------------+
--
--
--
INSERT INTO
    mucuser (idmucuser, userkind, userlogin, userhash, firstname, lastName, email, title, specialty)
VALUES
    (
        1,
        'Administrator',
        'vanessa@reteguin.com ',
        '$2b$12$lJtFe/6myaEhZRjki9V6/u8mI6pfwBjBDFvGwH4fklZ.b0hKM9ITy',
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
        '$2b$12$rVG1n5bT.o7dJ8JyEnwbK.lCl2F76uwjk5ToGbe8QPOdqPYBJlvFG',
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
        '$2b$12$VQkGBvV12XmV4FLc/Qj8i./cznXRUvQmoZ2y15k1XcspRlr2d/S5O',
        'Cardui',
        'Bot Yahoo',
        'carduibot@yahoo.com',
        'Lic.',
        'yahoo 11111101000'
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
    musession (idmucuser, sessionnumber)
SELECT
    idmucuser,
    'ThedammnumberYouSillyOMG'
FROM
    mucuser
WHERE
    userlogin = 'vanessa@reteguin.com';



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



SELECT
    idmucuser
FROM
    musession
WHERE
    sessionnumber = '_jW46vM7Dpn3UsYt6TlSV6tc6_cXAbvyW8C0Z8Gw4wE';



SELECT
    *
FROM
    mucuser
WHERE
    idmucuser = 1;



--
-- Get user kind
SELECT
    A.userkind
FROM
    mucuser A
    INNER JOIN musession B ON A.idmucuser = B.idmucuser
WHERE
    B.sessionnumber = '_jW46vM7Dpn3UsYt6TlSV6tc6_cXAbvyW8C0Z8Gw4wE';



------
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



SELECT
    *
FROM
    musession
WHERE
    sessionnumber = _jW46vM7Dpn3UsYt6TlSV6tc6_cXAbvyW8C0Z8Gw4wE;



SELECT
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