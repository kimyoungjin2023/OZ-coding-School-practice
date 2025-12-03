create database health_ai;

use health_ai;




create table patients(
patient_id int auto_increment primary key,
name varchar(50) not NULL,
gender enum('M','F'),
birth_date DATE
);

create table diagnoses(
diag_id int auto_increment primary key,
patient_id int, 
diagnosis_name varchar(50) not NULL,
diag_date date,
constraint fk_diagnoses_patient_id
	foreign key (patient_id) references patients(patient_id)
);

create table visits(
visit_id int auto_increment primary key,
patient_id int,
visit_date datetime,
doctor varchar(50),
constraint fk_visits_patient_id
	foreign key (patient_id) references patients(patient_id)
);

alter table patients
add age int;

alter table visits
change doctor hospital varchar(100);


UPDATE patients
SETpatients age = TIMESTAMPDIFF(YEAR, birth_date, CURDATE());

INSERT INTO patients (patient_id, name, gender, birth_date) VALUES
(1, 'Alice', 'F', '1991-04-12'),
(2, 'Brian', 'M', '1973-11-02'),
(3, 'Clara', 'F', '1996-08-30'),
(4, 'Daniel', 'M', '1980-02-17'),
(5, 'Eva', 'F', '1965-09-25');


INSERT INTO diagnoses (diag_id, patient_id, diagnosis_name, diag_date) VALUES
(101, 1, 'Hypertension', '2024-12-20'),
(102, 2, 'Diabetes', '2025-01-05'),
(103, 2, 'Hypertension', '2025-02-01'),
(104, 4, 'Arrhythmia', '2024-11-14'),
(105, 5, 'Hypertension', '2025-01-22');


INSERT INTO visits (visit_id, patient_id, visit_date, hospital) VALUES
(1001, 1, '2025-01-03 10:00:00', 'Seoul Clinic'),
(1002, 1, '2025-02-10 15:30:00', 'Seoul Clinic'),
(1003, 3, '2025-01-25 09:20:00', 'Busan Center'),
(1004, 4, '2025-03-20 13:10:00', 'Incheon Gen.'),
(1005, 5, '2025-02-14 11:45:00', 'Daegu Hosp.');



select patients.name from patients
inner join diagnoses
ON patients.patient_id = diagnoses.patient_id
where diagnosis_name = 'Hypertension';

select patients.name, diagnoses.diagnosis_name, visits.visit_date from patients
inner join diagnoses
ON patients.patient_id = diagnoses.patient_id
inner join visits
ON patients.patient_id = visits.patient_id
where diagnosis_name = 'Hypertension' or diagnosis_name = 'Diabetes'
order by visit_date desc
limit 3;

