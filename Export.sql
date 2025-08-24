CREATE DATABASE Export;

CREATE TABLE Export (
    FMID integer NOT NULL,
	MarketName varchar NOT NULL,
	Website varchar NULL,
	Facebook varchar NULL,
	Twitter varchar NULL,
	Youtube varchar NULL,
	OtherMedia varchar NULL,
    street varchar NULL,
	city varchar NULL,
	County varchar NULL,
	State varchar NULL,
	zip varchar NULL,
	Season1Date varchar NULL,
	Season1Time varchar NULL,
	Season2Date varchar NULL,
	Season2Time varchar NULL,
	Season3Date varchar NULL,
	Season3Time varchar NULL,
	Season4Date varchar NULL,
	Season4Time varchar NULL,
    x float4 NULL,
	y float4 NULL,
	Location varchar NULL,
    Credit varchar NULL,
	WIC varchar NULL,
	WICcash varchar NULL,
	SFMNP varchar NULL,
	SNAP varchar NULL,
	Organic varchar NULL,
	Bakedgoods varchar NULL,
	Cheese varchar NULL,
	Crafts varchar NULL,
	Flowers varchar NULL,
	Eggs varchar NULL,
	Seafood varchar NULL,
	Herbs varchar NULL,
	Vegetables varchar NULL,
	Honey varchar NULL,
	Jams varchar NULL,
	Maple varchar NULL,
	Meat varchar NULL,
	Nursery varchar NULL,
	Nuts varchar NULL,
	Plants varchar NULL,
	Poultry varchar NULL,
	Prepared varchar NULL,
	Soap varchar NULL,
	Trees varchar NULL,
	Wine varchar NULL,
	Coffee varchar NULL,
	Beans varchar NULL,
	Fruits varchar NULL,
	Grains varchar NULL,
	Juices varchar NULL,
	Mushrooms varchar NULL,
	PetFood varchar NULL,
	Tofu varchar NULL,
	WildHarvested varchar NULL,
	updateTime varchar NULL,
	CONSTRAINT Export_pk PRIMARY KEY (FMID)
	Review varchar NULL,
);


COPY Export
FROM 'C:\PythonProjects\Export\Export.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE Markets AS
SELECT FMID, MarketName, Website, Facebook, Twitter, Youtube, OtherMedia
FROM Export;

ALTER TABLE Markets
ADD CONSTRAINT Markets_pk PRIMARY KEY (FMID);

CREATE TABLE Address AS
SELECT FMID, street, city, County, State, zip
FROM Export;

ALTER TABLE Address
ADD COLUMN Address_id serial4 NOT NULL,
ADD CONSTRAINT Address_pk PRIMARY KEY (Address_id),
ADD CONSTRAINT Address_Markets_fk FOREIGN KEY (FMID) REFERENCES Markets(FMID);


CREATE TABLE Coordinates AS
SELECT FMID, x, y 
FROM Export;

ALTER TABLE Coordinates
ADD COLUMN Coordinates_id serial4 NOT NULL,
ADD CONSTRAINT Coordinates_pk PRIMARY KEY (Coordinates_id),
ADD CONSTRAINT Coordinates_Markets_fk FOREIGN KEY (FMID) REFERENCES Markets(FMID);


CREATE TABLE Payment AS
SELECT FMID, Credit, WIC, WICcash, SFMNP, SNAP
FROM Export;

ALTER TABLE Payment
ADD COLUMN Payment_id serial4 NOT NULL,
ADD CONSTRAINT Payment_pk PRIMARY KEY (Payment_id),
ADD CONSTRAINT Payment_Markets_fk FOREIGN KEY (FMID) REFERENCES Markets(FMID);



CREATE TABLE Products AS
SELECT	FMID, Organic, Bakedgoods, Cheese, Crafts, Flowers, Eggs, Seafood, Herbs, Vegetables,
Honey, Jams, Maple, Meat, Nursery, Nuts, Plants, Poultry, Prepared, Soap, Trees, Wine, 
Coffee, Beans, Fruits, Grains, Juices, Mushrooms, PetFood, Tofu, WildHarvested
FROM Export;

ALTER TABLE Products
ADD COLUMN Products_id serial4 NOT NULL,
ADD CONSTRAINT Products_pk PRIMARY KEY (Products_id),
ADD CONSTRAINT Products_Markets_fk FOREIGN KEY (FMID) REFERENCES Markets(FMID);

