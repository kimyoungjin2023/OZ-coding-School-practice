-- 1) 입원한 적 있는 환자의 정보만 조회를 해주세요. (patients, admissions 테이블 활용)
SELECT patients.first_name ,patients.last_name FROM patients
INNER JOIN admissions
ON patients.patient_id = admissions.patient_id;

-- 2) 아래 조건을 만족하는 결과를 조회하세요
    -- 실제로 입원한 환자만
    -- 실제로 담당 의사가 배정된 경우만
    -- 환자 이름과 진단명, 의사 specialty 출력  
SELECT patients.first_name, patients.last_name, admissions.diagnosis, doctors.specialty FROM patients
INNER JOIN admissions ON patients.patient_id = admissions.patient_id
INNER JOIN doctors ON admissions.attending_doctor_id = doctors.doctor_id; 
