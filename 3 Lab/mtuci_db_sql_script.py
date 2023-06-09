CREATE DATABASE mtuci_db;

CREATE TABLE departament
(
	id SERIAL PRIMARY KEY,
	name varchar(150) NOT NULL,
	decanat varchar(300) NOT NULL
);

CREATE TABLE student_group
(
	id SERIAL PRIMARY KEY,
	name varchar(150) NOT NULL,
	departament varchar(300) NOT NULL,
	fk_student_group integer REFERENCES departament (id)
);

CREATE TABLE student
(
	id SERIAL PRIMARY KEY,
	name varchar(150) NOT NULL,
	passport integer NOT NULL,
	student_group varchar(150) NOT NULL,
	fk_student integer REFERENCES student_group(id)
);

INSERT INTO departament
VALUES
(1, 'Иностранные языки', 'Цифровая экономика и масоовые коммуникации'),
(2, 'Математическая кибернетика и информационные технологии', 'Информационные технологии');

INSERT INTO student
VALUES
(1, 'Александров Александр Александрович', '1234567890', 'БИН2201'), (2, 'Борисов Борис Борисович', '1234567891', 'БИН2201'),
(3, 'Владимиров Владимир Владимирович', '1234567892', 'БИН2201'), (4, 'Георгиев Георгий Георгиевич', '1234567893', 'БИН2201'),
(5, 'Дмитров Дмитрий Дмитриевич', '1234567894', 'БИН2201'),
(6, 'Евгеньев Евгений Евгеньевич', '1234567895', 'БИН2202'), (7, 'Жераров Жерар Жерарович', '1234567896', 'БИН2202'),
(8, 'Захаров Захар Захарович', '1234567897', 'БИН2202'), (9, 'Игорев Игорь Игоревич', '1234567898', 'БИН2202'),
(10, 'Кириллов Кирилл Кириллович', '1234567899', 'БИН2202'),
(11, 'Леонидов Леонид Леонидович', '1234678900', 'БВТ2201'), (12, 'Максимов Максим Максимович', '1234678901', 'БВТ2201'),
(13, 'Николаев Николай Николаевич', '1234678902', 'БВТ2201'), (14, 'Олегов Олег Олегович', '1234678903', 'БВТ2201'),
(15, 'Павлов Павел Павлович', '1234678904', 'БВТ2201'),
(16, 'Ренатов Ренат Ренатович', '1234678905', 'БВТ2202'), (17, 'Станиславо Станислав Станиславович', '1234678906', 'БВТ2202'),
(18, 'Тимуров Тимур Тимурович', '1234678907', 'БВТ2202'), (19, 'Усманов Усман Усманович', '1234678908', 'БВТ2202'),
(20, 'Фёдоров Фёдор Фёдорович', '1234678909', 'БВТ2202');

INSERT INTO student_group
VALUES
(1, 'Цифровая экономика и массовые коммуникации', 1), (2, 'Цифровая экономика и массовые коммуникации', 1),
(3, 'Информационные технологии', 2), (4, 'Информационные технологии', 2)