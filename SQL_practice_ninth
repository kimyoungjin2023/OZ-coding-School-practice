-- 1) 환자를 지역(province_id)별로 그룹화하고, 그 지역 코드가 ‘NL’인 그룹만 조회하세요. [WHERE 사용 금지]
SELECT * FROM patients
GROUP BY province_id
HAVING province_id = 'NL';

-- 2) 의사 중 doctor_id가 offset이 10인 곳부터 10개의 행을 반환하세요. [WHERE 사용 금지]
SELECT * FROM doctors 
LIMIT  10, 10;

-- 실습5
-- patients와 province_names 테이블을 INNER JOIN하여 province_name 기준으로 GROUP BY를 하세요.
-- 그 후, province_name이 ‘N’으로 시작하는 지역들만 HAVING으로 필터링하고 
-- province_name 기준 오름차순 정렬 후 상위 3개만 LIMIT하세요.
SELECT * FROM patients
INNER JOIN province_names ON patients.province_id = province_names.province_id
GROUP BY province_names.province_name
HAVING province_names.province_name LIKE 'N%'
ORDER BY province_names.province_name ASC
LIMIT 3;
