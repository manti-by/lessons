SELECT u.email, r.count
FROM purchase AS r
JOIN "user" AS u ON r.user_id = u.id;

SELECT u.email, p.name, p.price, r.count
FROM "user" AS u
JOIN purchase AS r ON u.id = r.user_id
JOIN product AS p on p.id = r.product_id;

SELECT u.email, p.name, p.price, r.count
FROM "user" AS u
LEFT JOIN purchase AS r ON u.id = r.user_id
LEFT JOIN product AS p on p.id = r.product_id;

SELECT u.email, p.name, p.price, r.count
FROM "user" AS u
RIGHT JOIN purchase AS r ON u.id = r.user_id
RIGHT JOIN product AS p on p.id = r.product_id;

SELECT u.email, p.name, p.price, r.count
FROM "user" AS u
FULL JOIN purchase AS r ON u.id = r.user_id
FULL JOIN product AS p on p.id = r.product_id;

