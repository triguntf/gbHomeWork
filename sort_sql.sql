USE dz;
SET SQL_SAFE_UPDATES = 0;
UPDATE users SET created_at = now();
UPDATE users SET updated_at = now();

ALTER TABLE users ADD new_created_at DATETIME;
ALTER TABLE users ADD new_updated_at DATETIME;
UPDATE users SET new_created_at = STR_TO_DATE(created_at,'%Y-%m-%d%H:%i:%s');
UPDATE users SET new_updated_at = STR_TO_DATE(created_at, '%Y-%m-%d%H:%i:%s');
ALTER TABLE users DROP created_at, CHANGE new_created_at created_at DATETIME;
ALTER TABLE users DROP updated_at, CHANGE new_updated_at updated_at DATETIME;

SELECT
	* 
FROM
	storehouses_products
ORDER BY 
	IF(value>0,0,1), value;

SELECT round(avg(YEAR(CURDATE())-YEAR(Birthday_at)))
FROM users;

SELECT
    DAYNAME(CONCAT(YEAR(NOW()), '-', SUBSTRING(birthday_at, 6, 10))) AS week_day_of_birthday_in_this_Year,
    COUNT(*) AS amount_of_birthday
FROM
    users
GROUP BY 
    week_day_of_birthday_in_this_Year
ORDER BY
	amount_of_birthday DESC;

