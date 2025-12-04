select province_names.province_name, AVG(patients.height) from patients
inner join province_names
on patients.province_id = province_names.province_id
group by province_names.province_name
having AVG(patients.height) >= 155
order by AVG(patients.height) desc
limit 3;
