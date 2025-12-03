SELECT patients.first_name, admissions.admission_date FROM patients
LEFT JOIN admissions ON patients.patient_id = admissions.patient_id;

-- 2) 모든 의사의 배정된 환자의 입원 정보를 조회하세요. 의사가 환자를 진료한 적이 없어도 포함하세요.
SELECT patients.first_name, patients.last_name, admissions.diagnosis, doctors.specialty FROM patients
LEFT JOIN admissions ON patients.patient_id = admissions.patient_id
LEFT JOIN doctors ON admissions.attending_doctor_id = doctors.doctor_id;

-- 실습2
-- 1) patient 테이블을 기준으로 LEFT JOIN을 사용하여 모든 환자들의 정보 + 지역명을 가져오고 그 중에서 province_id = ‘AB’인 환자만 조회하세요.
SELECT patients.first_name, patients.last_name, patients.province_id, province_names.province_name FROM patients
LEFT JOIN province_names on patients.province_id = province_names.province_id
WHERE patients.province_id = 'AB';

-- 2) patients와 admissions를 INNER JOIN하여 입원 기록이 있는 환자만 대상이 되도록 하고, 그 중에서 진단명이 ‘Cancer’인 경우만 남기세요.
SELECT patients.first_name, admissions.diagnosis, admissions.admission_date FROM patients
INNER JOIN admissions ON patients.patient_id = admissions.patient_id
WHERE admissions.diagnosis = 'Cancer';
