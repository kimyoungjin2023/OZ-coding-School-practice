-- ============================================
-- MySQL 간단 프로젝트 - SQL 연습 문제
-- ============================================
-- 테이블 구조:
-- patients (patient_id, name, age, gender, birth_date)
-- diagnosis (diagnosis_id, patient_id, diagnosis_name, diag_date)
-- visits (visit_id, patient_id, visit_date, hospital)
-- ============================================


-- 문제 1
-- patients 테이블에서 모든 환자의 이름과 나이를 조회하세요.
SET SQL_SAFE_UPDATES = 0; -- 1175 오류가 발생하는데 safe모드가 켜져있어서 나는 오류dlamfh safe 모드 off
UPDATE patients
SET age = TIMESTAMPDIFF(YEAR, birth_date, CURDATE());
SET SQL_SAFE_UPDATES = 1; -- safe 모드 on
select patients.name, patients.age from patients;


-- 문제 2 
-- patients 테이블에서 여성(gender = 'F') 환자만 조회하세요.
select patients.name, patients.gender from patients
where gender = 'F';


-- 문제 3 
-- diagnosis 테이블에서 진단명이 'Hypertension'인 레코드를 모두 조회하세요.
select * from diagnoses
where diagnoses.diagnosis_name = 'Hypertension';



-- 문제 4 
-- patients 테이블에서 나이가 40세 이상인 환자의 이름과 나이를 조회하세요.
select patients.name, patients.age from patients
where patients.age >= 40;


-- 문제 5
-- visits 테이블에서 'Seoul Clinic'에 방문한 기록을 조회하세요.
select * from visits
where visits.hospital = 'Seoul Clinic';


-- 문제 6
-- 고혈압(Hypertension) 진단을 받은 환자의 이름을 조회하세요.
-- (힌트: patients와 diagnosis 테이블을 JOIN 하세요)
select patients.name, diagnoses.diagnosis_name from patients
join diagnoses on patients.patient_id = diagnoses.patient_id
where diagnoses.diagnosis_name = 'Hypertension';

-- 문제 7 
-- 각 병원별 방문 횟수를 조회하세요. (병원명과 방문 횟수를 출력)
select visits.hospital, count(visits.hospital) from visits
group by visits.hospital;

-- 문제 8 
-- 대사 질환 위험군을 찾으세요.
-- (Diabetes 또는 Hypertension 진단을 받은 환자의 이름을 중복 없이 조회)
select DISTINCT(patients.name) from patients
join diagnoses on patients.patient_id = diagnoses.patient_id
where diagnoses.diagnosis_name in ('Hypertension', 'Diabetes');


-- 문제 9 
-- 고위험 환자(Diabetes 또는 Hypertension 진단)를 찾고,
-- 각 환자의 이름, 진단 횟수, 가장 최근 진단일을 조회하세요.
-- 진단 횟수가 많은 순으로 정렬하세요.
select patients.name, count(diagnoses.diag_id), max(diagnoses.diag_date) from patients
join diagnoses on patients.patient_id = diagnoses.patient_id
where diagnoses.diagnosis_name in ('Hypertension', 'Diabetes')
group by patients.patient_id, patients.name
order by count(diagnoses.diag_id) desc;

-- 문제 10 
-- 최근에 방문한 고위험 환자 TOP 3를 찾으세요.
-- (Diabetes 또는 Hypertension 진단이 있는 환자 중 방문 기록이 있는 환자)
-- 환자 이름, 가장 최근 방문일, 방문 병원을 조회하세요.
select patients.name, visits.visit_date, visits.hospital from patients 
join diagnoses on patients.patient_id = diagnoses.patient_id
join (
    select patient_id, MAX(visit_date) as recent from visits
    group by patient_id
) rv 
    on patients.patient_id = rv.patient_id
join visits 
    on visits.patient_id = rv.patient_id
   and visits.visit_date = rv.recent
where diagnoses.diagnosis_name in ('Hypertension', 'Diabetes')
order by visits.visit_date DESC
limit 3;

