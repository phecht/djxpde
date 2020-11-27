import sqlite3
from sqlite3 import Error

# should be run in a folder called utils.
# A couple of things:
# 1) You need to run makemigrations and migrate after updating models.
# 2) You need to get something like sqlitebrowser and import the csv file and name it july2020.
# 3) You all need to "run" lookups/slmpdata_crime_category.csv 

def sql_connection():
    try:
        conn = sqlite3.connect('../db.sqlite3')
        return conn
    except Error:
        print(Error)


def sql_fetch(conn):
    cursorObj = conn.cursor()
    cursorObj.execute('select * FROM july2020')
    return cursorObj


def sql_insert(conn, enties):
    cursorObj = conn.cursor()
    cursorObj.execute('''INSERT INTO  slmpd_crime_reports(category_id, neighborhood_id, cadaddress, cadstreet, codedmonth,
        complaint, crimecode, crimedesc, dateoccur, district, flagadmin, flagcrime, flagunfounded, importneighborhood,
        leadaddress, leadstreet, locationcomment, locationname, rcount, xcoord, ycoord)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', entities)
    conn.commit()
# 5+8+7=20


def fixnull(field):
    if not field:
        return ' '
    else:
        return field


conn = sql_connection()
inputrows = sql_fetch(conn)

for inrow in inputrows:
    complaint = inrow[0]
    codedmonth = inrow[1]
    dateoccur = inrow[2]
    flagcrime = inrow[3]
    if not flagcrime:
        flagcrime = ' '
    flagunfound = inrow[4]
    if not flagunfound:
        flagunfound = ' '
    flagcadmin = inrow[5]
    if not flagcadmin:
        flagcadmin = ' '
    count = inrow[6]
    flagcleanup = inrow[7]
    if not flagcleanup:
        flagcleanup = ' '
    crime1 = str(inrow[8])
    if len(crime1) == 5:
        crime1 = "0" + crime1
    crimecode = crime1[:2]
    crimeother = crime1[2:]
    district = inrow[9]
    desc = inrow[10]
    ileadaddress = fixnull(inrow[11])
    ileadstreet = fixnull(inrow[12])
    neighborhood = inrow[13]
    locationname = fixnull(inrow[14])
    locationcomment = fixnull(inrow[15])
    cadaddress = fixnull(inrow[16])
    cadstreet = fixnull(inrow[17])
    xcord = inrow[18]
    ycord = inrow[19]
    entities = (int(crimecode), int(neighborhood), cadaddress, cadstreet, codedmonth, complaint, crime1, desc, dateoccur, district, flagcadmin,
                flagcrime, flagunfound, neighborhood, ileadaddress, ileadstreet, locationcomment, locationname, count, xcord, ycord)

    sql_insert(conn, entities)
    # print(complaint, inrow[1], crimecode, crimeother )
    print(entities)


# Raw SQL to import into sqlite
""" BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "slmpd_crime_category" (
	"id"	integer NOT NULL,
	"category"	text NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "slmpd_crime_neighborhood" (
	"id"	integer NOT NULL,
	"name"	text NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (1,'Homicide');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (2,'Rape');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (3,'Robbery');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (4,'Assault');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (5,'Burglary');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (6,'Larceny');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (7,'Vehicle Theft');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (8,'Arson');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (9,'Other Assaults');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (10,'Forgery');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (11,'Fraud');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (12,'Embezzlement');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (13,'Stolen Property');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (14,'Vandalism');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (15,'Weapons');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (16,'Prostitution and Vice');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (17,'Sex Offenses (other)');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (18,'Drugs');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (19,'Gambling');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (20,'Offenses to Family/Child');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (21,'DUI');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (22,'Liquor Laws');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (23,'Drunkenness');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (24,'Disorderly Conduct');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (25,'Vagrancy');
INSERT INTO "slmpd_crime_category" ("id","category") VALUES (26,'All Other Crime');

INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (1,'Carondelet');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (2,'Patch');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (3,'Holly Hills');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (4,'Boulevard Heights');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (5,'Bevo Mill');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (6,'Princeton Heights');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (7,'Southampton');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (8,'St. Louis Hills');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (9,'Lindenwood Park (neighborhood)');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (10,'Ellendale');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (11,'Clifton Heights');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (12,'The Hill');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (13,'Southwest Garden');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (14,'Northampton');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (15,'Tower Grove South');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (16,'Dutchtown');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (17,'Mount Pleasant');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (18,'Marine Villa');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (19,'Gravois Park (neighborhood)');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (20,'Kosciusko');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (21,'Soulard');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (22,'Benton Park (neighborhood)');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (23,'McKinley Heights');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (24,'Fox Park (neighborhood)');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (25,'Tower Grove East');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (26,'Compton Heights');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (27,'Shaw');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (28,'Botanical Heights');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (29,'Tiffany');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (30,'Benton Park West');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (31,'The Gate District');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (32,'Lafayette Square');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (33,'Peabody Darst Webbe');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (34,'LaSalle Park (neighborhood)');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (35,'Downtown');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (36,'Downtown West');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (37,'Midtown');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (38,'Central West End');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (39,'Forest Park South East');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (40,'Kings Oak');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (41,'Cheltenham');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (42,'Clayton-Tamm');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (43,'Franz Park (neighborhood)');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (44,'Hi-Pointe');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (45,'Wydown Skinker');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (46,'Skinker DeBaliviere');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (47,'DeBaliviere Place');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (48,'West End');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (49,'Visitation Park (neighborhood)');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (50,'Wells Goodfellow');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (51,'Academy');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (52,'Kingsway West');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (53,'Fountain Park (neighborhood)');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (54,'Lewis Place');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (55,'Kingsway East');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (56,'Greater Ville');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (57,'The Ville');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (58,'Vandeventer');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (59,'Jeff Vanderlou');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (60,'St. Louis Place');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (61,'Carr Square');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (62,'Columbus Square');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (63,'Old North St. Louis');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (64,'Near North Riverfront');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (65,'Hyde Park (neighborhood)');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (66,'College Hill');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (67,'Fairground Neighborhood');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (68,'O’Fallon');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (69,'Penrose');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (70,'Mark Twain I-70 Industrial');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (71,'Mark Twain');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (72,'Walnut Park East');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (73,'North Pointe');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (74,'Baden');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (75,'Riverview');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (76,'Walnut Park East');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (77,'Covenant Blu - Grand Center');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (78,'Hamilton Heights');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (79,'North Riverfront');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (80,'Carondelet Park');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (81,'Tower Grove Park');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (82,'Forest Park');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (83,'Fairgrounds Park');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (84,'Penrose Park');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (85,'O’Fallon Park');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (86,'Calvary - Bellefontaine Cemeteries');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (87,'Botanical Garden');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (88,'Wilmore Park');
INSERT INTO "slmpd_crime_neighborhood" ("id","name") VALUES (89,'Neighborhood Unknown');

COMMIT; """
