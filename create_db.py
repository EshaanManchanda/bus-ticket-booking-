import sqlite3


def insert_bus_data():
    con = sqlite3.connect(database=r'ticketing.db')
    cur = con.cursor()
    try:
        cur.execute(
            "insert into bus values('Andhra Pradesh','Arunachal Pradesh','2966.8','	63','103000',NULL,	NULL,'100',NULL,'100','100')")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Assam'	,'	2557.4  	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Bihar'	,'	1807.9  	'	,'	34   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Andhra Pradesh'	,'	Chhattisgarh'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Goa'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Gujarat'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Haryana'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Andhra Pradesh'	,'	Himachal Pradesh'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Andhra Pradesh'	,'	Jammu and Kashmir'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Andhra Pradesh'	,'	Jharkhand'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Andhra Pradesh'	,'	Karnataka'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Kerala'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Andhra Pradesh'	,'	Madhya Pradesh'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Maharashtra'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Manipur'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Meghalaya'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Mizoram'	,'	2964.20	'	,'	69	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Nagaland'	,'	2780.10	'	,'	62 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Odisha'	,'	901.9 	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Punjab'	,'	2253.60	'	,'	38	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Rajasthan'	,'	1778.60	'	,'	33	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Sikkim'	,'	2054.00	'	,'	44	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Tamil Nadu'	,'	678.40	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Telangana'	,'	335.30	'	,'	7	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Tripura'	,'	2920.30	'	,'	67	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Andhra Pradesh'	,'	Uttar Pradesh'	,'	1771.00	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Andhra Pradesh'	,'	Uttarakhand'	,'	2167.00	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Andhra Pradesh'	,'	West Bengal'	,'	1357.5 	'	,'	28 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Assam'	,'	601.00	'	,'	13	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Bihar'	,'	1439.6 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Chhattisgarh'	,'	2225.70	'	,'	50 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Goa'	,'	3534.40	'	,'	71	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Gujarat'	,'	3318.50	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Haryana'	,'	2648.00	'	,'	51	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Himachal Pradesh'	,'	2556.90	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Jammu and Kashmir'	,'	3,218.7 	'	,'	63 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Jharkhand'	,'	1,625.8 	'	,'	38 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Karnataka'	,'	3436.20	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Kerala'	,'	3901.3 	'	,'	78	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Madhya Pradesh'	,'	2336.40	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Maharashtra'	,'	2858.10	'	,'	57	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Manipur'	,'	723.70	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Meghalaya'	,'	828.3 	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Mizoram'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Nagaland'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Odisha'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Punjab'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Rajasthan'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Sikkim'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Tamil Nadu'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Telangana'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Arunachal Pradesh'	,'	Tripura'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Uttar Pradesh'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Uttarakhand'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	West Bengal'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Arunachal Pradesh'	,'	Andhra Pradesh'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Bihar'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Chhattisgarh'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Goa'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Gujarat'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Haryana'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Himachal Pradesh'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Jammu and Kashmir'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Jharkhand'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Karnataka'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Kerala'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Madhya Pradesh'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Maharashtra'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Manipur'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Meghalaya'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Mizoram'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Nagaland'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Odisha'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Punjab'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Rajasthan'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Sikkim'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Tamil Nadu'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Telangana'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Tripura'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Uttar Pradesh'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Uttarakhand'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	West Bengal'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Andhra Pradesh'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Assam'	,'	Arunachal Pradesh'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Chhattisgarh'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Goa'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Gujarat'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Haryana'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Himachal Pradesh'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Jammu and Kashmir'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Jharkhand'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Karnataka'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Kerala'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Madhya Pradesh'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Maharashtra'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Manipur'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Meghalaya'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Mizoram'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Nagaland'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Odisha'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Punjab'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Rajasthan'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Sikkim'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Tamil Nadu'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Telangana'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Tripura'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Uttar Pradesh'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Uttarakhand'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	West Bengal'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Andhra Pradesh'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Arunachal Pradesh'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Bihar'	,'	Assam'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Goa'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Gujarat'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Haryana'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Chhattisgarh'	,'	Himachal Pradesh'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Chhattisgarh'	,'	Jammu and Kashmir'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Jharkhand'	,'	2557.4  	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Karnataka'	,'	1807.9  	'	,'	34   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Kerala'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Madhya Pradesh'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Chhattisgarh'	,'	Maharashtra'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Manipur'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Meghalaya'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Mizoram'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Nagaland'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Odisha'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Punjab'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Rajasthan'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Sikkim'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Tamil Nadu'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Telangana'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Tripura'	,'	2964.20	'	,'	69	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Chhattisgarh'	,'	Uttar Pradesh'	,'	2780.10	'	,'	62 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Uttarakhand'	,'	901.9 	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	West Bengal'	,'	2253.60	'	,'	38	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Chhattisgarh'	,'	Andhra Pradesh'	,'	1778.60	'	,'	33	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Chhattisgarh'	,'	Arunachal Pradesh'	,'	2054.00	'	,'	44	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Assam'	,'	678.40	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Chhattisgarh'	,'	Bihar'	,'	335.30	'	,'	7	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Gujarat'	,'	2920.30	'	,'	67	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Haryana'	,'	1771.00	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Himachal Pradesh'	,'	2167.00	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Jammu and Kashmir'	,'	1357.5 	'	,'	28 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Jharkhand'	,'	601.00	'	,'	13	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Karnataka'	,'	1439.6 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Kerala'	,'	2225.70	'	,'	50 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Madhya Pradesh'	,'	3534.40	'	,'	71	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Maharashtra'	,'	3318.50	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Manipur'	,'	2648.00	'	,'	51	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Meghalaya'	,'	2556.90	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Mizoram'	,'	3,218.7 	'	,'	63 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Nagaland'	,'	1,625.8 	'	,'	38 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Odisha'	,'	3436.20	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Punjab'	,'	3901.3 	'	,'	78	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Rajasthan'	,'	2336.40	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Sikkim'	,'	2858.10	'	,'	57	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Tamil Nadu'	,'	723.70	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Telangana'	,'	828.3 	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Tripura'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Uttar Pradesh'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Uttarakhand'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	West Bengal'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Andhra Pradesh'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Arunachal Pradesh'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Assam'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Bihar'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Goa'	,'	Chhattisgarh'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Goa'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Haryana'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Himachal Pradesh'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Gujarat'	,'	Jammu and Kashmir'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Jharkhand'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Karnataka'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Kerala'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Madhya Pradesh'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Maharashtra'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Manipur'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Meghalaya'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Mizoram'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Nagaland'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Odisha'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Punjab'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Rajasthan'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Sikkim'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Tamil Nadu'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Telangana'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Tripura'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Uttar Pradesh'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Uttarakhand'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	West Bengal'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Andhra Pradesh'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Arunachal Pradesh'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Assam'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Bihar'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Gujarat'	,'	Chhattisgarh'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Goa'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Gujarat'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Himachal Pradesh'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Jammu and Kashmir'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Jharkhand'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Karnataka'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Kerala'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Madhya Pradesh'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Maharashtra'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Manipur'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Meghalaya'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Mizoram'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Nagaland'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Odisha'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Punjab'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Rajasthan'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Sikkim'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Tamil Nadu'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Telangana'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Tripura'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Uttar Pradesh'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Uttarakhand'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	West Bengal'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Andhra Pradesh'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Arunachal Pradesh'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Assam'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Bihar'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Haryana'	,'	Chhattisgarh'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Haryana'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Goa'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Gujarat'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Jammu and Kashmir'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Jharkhand'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Karnataka'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Kerala'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Madhya Pradesh'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Maharashtra'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Manipur'	,'	2557.4  	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Meghalaya'	,'	1807.9  	'	,'	34   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Mizoram'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Nagaland'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Odisha'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Punjab'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Rajasthan'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Sikkim'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Tamil Nadu'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Telangana'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Tripura'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Uttar Pradesh'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Uttarakhand'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	West Bengal'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Andhra Pradesh'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Arunachal Pradesh'	,'	2964.20	'	,'	69	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Assam'	,'	2780.10	'	,'	62 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Himachal Pradesh'	,'	Bihar'	,'	901.9 	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Himachal Pradesh'	,'	Chhattisgarh'	,'	2253.60	'	,'	38	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Andhra Pradesh'	,'	1778.60	'	,'	33	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Arunachal Pradesh'	,'	2054.00	'	,'	44	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Assam'	,'	678.40	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Bihar'	,'	335.30	'	,'	7	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Chhattisgarh'	,'	2920.30	'	,'	67	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Goa'	,'	1771.00	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Gujarat'	,'	2167.00	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Haryana'	,'	1357.5 	'	,'	28 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Himachal Pradesh'	,'	601.00	'	,'	13	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Jharkhand'	,'	1439.6 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Karnataka'	,'	2225.70	'	,'	50 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Kerala'	,'	3534.40	'	,'	71	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Madhya Pradesh'	,'	3318.50	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Maharashtra'	,'	2648.00	'	,'	51	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Manipur'	,'	2556.90	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Meghalaya'	,'	3,218.7 	'	,'	63 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Mizoram'	,'	1,625.8 	'	,'	38 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Nagaland'	,'	3436.20	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Odisha'	,'	3901.3 	'	,'	78	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Punjab'	,'	2336.40	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Rajasthan'	,'	2858.10	'	,'	57	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Sikkim'	,'	723.70	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Tamil Nadu'	,'	828.3 	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Telangana'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jammu and Kashmir'	,'	Tripura'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Uttar Pradesh'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	Uttarakhand'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jammu and Kashmir'	,'	West Bengal'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Andhra Pradesh'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jharkhand'	,'	Arunachal Pradesh'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Assam'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Bihar'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Chhattisgarh'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Goa'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Gujarat'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Haryana'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Himachal Pradesh'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Jharkhand'	,'	Jammu and Kashmir'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Karnataka'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Kerala'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Madhya Pradesh'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Maharashtra'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Manipur'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Meghalaya'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Mizoram'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Nagaland'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Odisha'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Punjab'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Rajasthan'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Sikkim'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Tamil Nadu'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Telangana'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Tripura'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Uttar Pradesh'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	Uttarakhand'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Jharkhand'	,'	West Bengal'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Andhra Pradesh'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Karnataka'	,'	Arunachal Pradesh'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Assam'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Bihar'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Chhattisgarh'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Goa'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Gujarat'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Haryana'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Himachal Pradesh'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Karnataka'	,'	Jammu and Kashmir'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Jharkhand'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Kerala'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Madhya Pradesh'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Maharashtra'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Manipur'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Meghalaya'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Mizoram'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Nagaland'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Odisha'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Punjab'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Rajasthan'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Sikkim'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Tamil Nadu'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Telangana'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Tripura'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Uttar Pradesh'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	Uttarakhand'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Karnataka'	,'	West Bengal'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Andhra Pradesh'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Arunachal Pradesh'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Assam'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Bihar'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Chhattisgarh'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Goa'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Gujarat'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Haryana'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Kerala'	,'	Himachal Pradesh'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Jammu and Kashmir'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Jharkhand'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Karnataka'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Madhya Pradesh'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Maharashtra'	,'	2557.4  	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Manipur'	,'	1807.9  	'	,'	34   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Meghalaya'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Mizoram'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Nagaland'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Odisha'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Punjab'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Rajasthan'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Sikkim'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Tamil Nadu'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Telangana'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Tripura'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Uttar Pradesh'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	Uttarakhand'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Kerala'	,'	West Bengal'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Madhya Pradesh'	,'	Andhra Pradesh'	,'	2964.20	'	,'	69	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Madhya Pradesh'	,'	Arunachal Pradesh'	,'	2780.10	'	,'	62 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Assam'	,'	901.9 	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Bihar'	,'	2253.60	'	,'	38	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Madhya Pradesh'	,'	Chhattisgarh'	,'	1778.60	'	,'	33	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Goa'	,'	2054.00	'	,'	44	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Gujarat'	,'	678.40	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Haryana'	,'	335.30	'	,'	7	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Madhya Pradesh'	,'	Himachal Pradesh'	,'	2920.30	'	,'	67	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Madhya Pradesh'	,'	Jammu and Kashmir'	,'	1771.00	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Jharkhand'	,'	2167.00	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Kerala'	,'	1357.5 	'	,'	28 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Karnataka'	,'	601.00	'	,'	13	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Maharashtra'	,'	1439.6 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Manipur'	,'	2225.70	'	,'	50 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Meghalaya'	,'	3534.40	'	,'	71	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Mizoram'	,'	3318.50	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Nagaland'	,'	2648.00	'	,'	51	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Odisha'	,'	2556.90	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Punjab'	,'	3,218.7 	'	,'	63 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Rajasthan'	,'	1,625.8 	'	,'	38 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Sikkim'	,'	3436.20	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Tamil Nadu'	,'	3901.3 	'	,'	78	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Telangana'	,'	2336.40	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Tripura'	,'	2858.10	'	,'	57	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Madhya Pradesh'	,'	Uttar Pradesh'	,'	723.70	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Madhya Pradesh'	,'	Uttarakhand'	,'	828.3 	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Madhya Pradesh'	,'	West Bengal'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Andhra Pradesh'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Maharashtra'	,'	Arunachal Pradesh'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Assam'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Bihar'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Chhattisgarh'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Goa'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Gujarat'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Haryana'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Maharashtra'	,'	Himachal Pradesh'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Maharashtra'	,'	Jammu and Kashmir'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Jharkhand'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Kerala'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Madhya Pradesh'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Karnataka'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Manipur'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Meghalaya'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Mizoram'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Nagaland'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Odisha'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Punjab'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Rajasthan'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Sikkim'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Tamil Nadu'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Telangana'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Tripura'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Uttar Pradesh'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	Uttarakhand'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Maharashtra'	,'	West Bengal'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Andhra Pradesh'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Arunachal Pradesh'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Assam'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Bihar'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Chhattisgarh'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Goa'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Gujarat'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Haryana'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Manipur'	,'	Himachal Pradesh'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Jammu and Kashmir'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Jharkhand'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Kerala'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Madhya Pradesh'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Maharashtra'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Karnataka'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Meghalaya'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Mizoram'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Nagaland'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Odisha'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Punjab'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Rajasthan'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Sikkim'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Tamil Nadu'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Telangana'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Tripura'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Uttar Pradesh'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	Uttarakhand'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Manipur'	,'	West Bengal'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Andhra Pradesh'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Arunachal Pradesh'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Assam'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Bihar'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Chhattisgarh'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Goa'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Gujarat'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Haryana'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Meghalaya'	,'	Himachal Pradesh'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Meghalaya'	,'	Jammu and Kashmir'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Jharkhand'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Kerala'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Meghalaya'	,'	Madhya Pradesh'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Maharashtra'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Manipur'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Karnataka'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Mizoram'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Nagaland'	,'	2557.4  	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Odisha'	,'	1807.9  	'	,'	34   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Punjab'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Rajasthan'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Sikkim'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Tamil Nadu'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Telangana'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Tripura'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Uttar Pradesh'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	Uttarakhand'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Meghalaya'	,'	West Bengal'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Andhra Pradesh'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Arunachal Pradesh'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Assam'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Bihar'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Chhattisgarh'	,'	2964.20	'	,'	69	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Goa'	,'	2780.10	'	,'	62 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Gujarat'	,'	901.9 	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Haryana'	,'	2253.60	'	,'	38	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Himachal Pradesh'	,'	1778.60	'	,'	33	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Jammu and Kashmir'	,'	2054.00	'	,'	44	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Jharkhand'	,'	678.40	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Kerala'	,'	335.30	'	,'	7	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Madhya Pradesh'	,'	2920.30	'	,'	67	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Maharashtra'	,'	1771.00	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Manipur'	,'	2167.00	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Meghalaya'	,'	1357.5 	'	,'	28 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Karnataka'	,'	601.00	'	,'	13	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Nagaland'	,'	1439.6 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Odisha'	,'	2225.70	'	,'	50 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Punjab'	,'	3534.40	'	,'	71	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Rajasthan'	,'	3318.50	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Sikkim'	,'	2648.00	'	,'	51	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Tamil Nadu'	,'	2556.90	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Telangana'	,'	3,218.7 	'	,'	63 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Tripura'	,'	1,625.8 	'	,'	38 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Uttar Pradesh'	,'	3436.20	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	Uttarakhand'	,'	3901.3 	'	,'	78	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Mizoram'	,'	West Bengal'	,'	2336.40	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Andhra Pradesh'	,'	2858.10	'	,'	57	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Arunachal Pradesh'	,'	723.70	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Assam'	,'	828.3 	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Bihar'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Chhattisgarh'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Goa'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Gujarat'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Haryana'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Himachal Pradesh'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Nagaland'	,'	Jammu and Kashmir'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Jharkhand'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Kerala'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Madhya Pradesh'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Maharashtra'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Manipur'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Meghalaya'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Karnataka'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Mizoram'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Odisha'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Punjab'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Rajasthan'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Sikkim'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Tamil Nadu'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Telangana'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Tripura'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Uttar Pradesh'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	Uttarakhand'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Nagaland'	,'	West Bengal'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Andhra Pradesh'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Arunachal Pradesh'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Assam'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Bihar'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Chhattisgarh'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Goa'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Gujarat'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Haryana'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Himachal Pradesh'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Jammu and Kashmir'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Jharkhand'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Kerala'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Madhya Pradesh'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Maharashtra'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Manipur'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Meghalaya'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Karnataka'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Nagaland'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Mizoram'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Punjab'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Rajasthan'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Sikkim'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Tamil Nadu'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Telangana'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Tripura'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Uttar Pradesh'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	Uttarakhand'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Odisha'	,'	West Bengal'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Andhra Pradesh'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Arunachal Pradesh'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Assam'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Bihar'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Chhattisgarh'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Goa'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Gujarat'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Haryana'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Himachal Pradesh'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Jammu and Kashmir'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Jharkhand'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Kerala'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Madhya Pradesh'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Maharashtra'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Manipur'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Meghalaya'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Karnataka'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Nagaland'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Odisha'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Mizoram'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Rajasthan'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Sikkim'	,'	2557.4  	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Tamil Nadu'	,'	1807.9  	'	,'	34   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Telangana'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Tripura'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Uttar Pradesh'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	Uttarakhand'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Punjab'	,'	West Bengal'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Rajasthan'	,'	Andhra Pradesh'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Rajasthan'	,'	Arunachal Pradesh'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Assam'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Bihar'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Chhattisgarh'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Goa'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Gujarat'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Haryana'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Himachal Pradesh'	,'	2964.20	'	,'	69	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Rajasthan'	,'	Jammu and Kashmir'	,'	2780.10	'	,'	62 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Jharkhand'	,'	901.9 	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Kerala'	,'	2253.60	'	,'	38	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Madhya Pradesh'	,'	1778.60	'	,'	33	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Maharashtra'	,'	2054.00	'	,'	44	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Manipur'	,'	678.40	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Meghalaya'	,'	335.30	'	,'	7	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Karnataka'	,'	2920.30	'	,'	67	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Nagaland'	,'	1771.00	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Odisha'	,'	2167.00	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Punjab'	,'	1357.5 	'	,'	28 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Mizoram'	,'	601.00	'	,'	13	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Sikkim'	,'	1439.6 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Tamil Nadu'	,'	2225.70	'	,'	50 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Telangana'	,'	3534.40	'	,'	71	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Tripura'	,'	3318.50	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Uttar Pradesh'	,'	2648.00	'	,'	51	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	Uttarakhand'	,'	2556.90	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Rajasthan'	,'	West Bengal'	,'	3,218.7 	'	,'	63 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Andhra Pradesh'	,'	1,625.8 	'	,'	38 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Arunachal Pradesh'	,'	3436.20	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Assam'	,'	3901.3 	'	,'	78	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Bihar'	,'	2336.40	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Chhattisgarh'	,'	2858.10	'	,'	57	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Goa'	,'	723.70	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Gujarat'	,'	828.3 	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Haryana'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Himachal Pradesh'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Jammu and Kashmir'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Jharkhand'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Kerala'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Madhya Pradesh'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Maharashtra'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Manipur'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Meghalaya'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Karnataka'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Nagaland'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Odisha'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Punjab'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Rajasthan'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Mizoram'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Tamil Nadu'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Telangana'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Tripura'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Uttar Pradesh'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	Uttarakhand'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Sikkim'	,'	West Bengal'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Andhra Pradesh'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Tamil Nadu'	,'	Arunachal Pradesh'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Assam'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Bihar'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Chhattisgarh'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Goa'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Gujarat'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Haryana'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Tamil Nadu'	,'	Himachal Pradesh'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Tamil Nadu'	,'	Jammu and Kashmir'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Jharkhand'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Kerala'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Madhya Pradesh'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Maharashtra'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Manipur'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Meghalaya'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Karnataka'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Nagaland'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Odisha'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Punjab'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Rajasthan'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Sikkim'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Mizoram'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Telangana'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Tripura'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Uttar Pradesh'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	Uttarakhand'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tamil Nadu'	,'	West Bengal'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Andhra Pradesh'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Telangana'	,'	Arunachal Pradesh'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Assam'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Bihar'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Chhattisgarh'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Goa'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Gujarat'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Haryana'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Telangana'	,'	Himachal Pradesh'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Jammu and Kashmir'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Jharkhand'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Kerala'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Madhya Pradesh'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Maharashtra'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Manipur'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Meghalaya'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Karnataka'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Nagaland'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Odisha'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Punjab'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Rajasthan'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Sikkim'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Tamil Nadu'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Mizoram'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Tripura'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Telangana'	,'	Uttar Pradesh'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	Uttarakhand'	,'	2557.4  	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Telangana'	,'	West Bengal'	,'	1807.9  	'	,'	34   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Andhra Pradesh'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Arunachal Pradesh'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Assam'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Bihar'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Chhattisgarh'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Goa'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Gujarat'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Haryana'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Himachal Pradesh'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Jammu and Kashmir'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Jharkhand'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Kerala'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Madhya Pradesh'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Maharashtra'	,'	2964.20	'	,'	69	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Manipur'	,'	2780.10	'	,'	62 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Meghalaya'	,'	901.9 	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Karnataka'	,'	2253.60	'	,'	38	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Nagaland'	,'	1778.60	'	,'	33	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Odisha'	,'	2054.00	'	,'	44	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Punjab'	,'	678.40	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Rajasthan'	,'	335.30	'	,'	7	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Sikkim'	,'	2920.30	'	,'	67	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Tamil Nadu'	,'	1771.00	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Telangana'	,'	2167.00	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Mizoram'	,'	1357.5 	'	,'	28 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Uttar Pradesh'	,'	601.00	'	,'	13	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	Uttarakhand'	,'	1439.6 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Tripura'	,'	West Bengal'	,'	2225.70	'	,'	50 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Uttar Pradesh'	,'	Andhra Pradesh'	,'	3534.40	'	,'	71	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Uttar Pradesh'	,'	Arunachal Pradesh'	,'	3318.50	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Assam'	,'	2648.00	'	,'	51	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Bihar'	,'	2556.90	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Uttar Pradesh'	,'	Chhattisgarh'	,'	3,218.7 	'	,'	63 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Goa'	,'	1,625.8 	'	,'	38 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Gujarat'	,'	3436.20	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Haryana'	,'	3901.3 	'	,'	78	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Uttar Pradesh'	,'	Himachal Pradesh'	,'	2336.40	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Uttar Pradesh'	,'	Jammu and Kashmir'	,'	2858.10	'	,'	57	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Jharkhand'	,'	723.70	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Kerala'	,'	828.3 	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Uttar Pradesh'	,'	Madhya Pradesh'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Maharashtra'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Manipur'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Meghalaya'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Karnataka'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Nagaland'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Odisha'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Punjab'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Rajasthan'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Sikkim'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Tamil Nadu'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Telangana'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Tripura'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Mizoram'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	Uttarakhand'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttar Pradesh'	,'	West Bengal'	,'	3119.80	'	,'	60	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Uttarakhand'	,'	Andhra Pradesh'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Uttarakhand'	,'	Arunachal Pradesh'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Assam'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Bihar'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Chhattisgarh'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Goa'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Gujarat'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Haryana'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Uttarakhand'	,'	Himachal Pradesh'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	Uttarakhand'	,'	Jammu and Kashmir'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Jharkhand'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Kerala'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Madhya Pradesh'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Maharashtra'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Manipur'	,'	902.8  	'	,'	18	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Meghalaya'	,'	740.20	'	,'	16	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Karnataka'	,'	1583.4  	'	,'	30   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Nagaland'	,'	1954.6  	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Odisha'	,'	2147.20	'	,'	31	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Punjab'	,'	2,562.8  	'	,'	47   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Rajasthan'	,'	1378.80	'	,'	29   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Sikkim'	,'	541.5  	'	,'	12   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Tamil Nadu'	,'	1012.40	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Telangana'	,'	1114.10	'	,'	21	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Tripura'	,'	834.50	'	,'	14 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Uttar Pradesh'	,'	2874.00	'	,'	63	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	Mizoram'	,'	2,427.4 	'	,'	52	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	Uttarakhand'	,'	West Bengal'	,'	2903.9 	'	,'	52 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	West Bengal'	,'	Andhra Pradesh'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	West Bengal'	,'	Arunachal Pradesh'	,'	2293.00	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Assam'	,'	2,233.4 	'	,'	40	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Bihar'	,'	1,211.2 	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Chhattisgarh'	,'	3021.60	'	,'	58	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Goa'	,'	3486.7 	'	,'	68	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Gujarat'	,'	1921.8 	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Haryana'	,'	2443.50	'	,'	46	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	West Bengal'	,'	Himachal Pradesh'	,'	337.5 	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	West Bengal'	,'	Jammu and Kashmir'	,'	320.00	'	,'	8	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Jharkhand'	,'	559.80	'	,'	19	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Kerala'	,'	334.10	'	,'	11	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Madhya Pradesh'	,'	1780.50	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Maharashtra'	,'	1,133.0 	'	,'	32	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Manipur'	,'	490.30	'	,'	14	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Meghalaya'	,'	2,195.1 	'	,'	50	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Karnataka'	,'	2,909.5 	'	,'	55	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Nagaland'	,'	2767.90	'	,'	53	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Odisha'	,'	1133.40	'	,'	27 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Punjab'	,'	3,567.3 	'	,'	73	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Rajasthan'	,'	2916.50	'	,'	60 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Sikkim'	,'	1122.00	'	,'	29 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Tamil Nadu'	,'	2,117.9 	'	,'	43	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Telangana'	,'	2600.70	'	,'	54 	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Tripura'	,'	1559.1 	'	,'	35	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute("	insert into bus  values ('	West Bengal'	,'	Uttar Pradesh'	,'	2966.8  	'	,'	63   	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Uttarakhand'	,'	1025.00	'	,'	22	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")
        cur.execute(
            "	insert into bus  values ('	West Bengal'	,'	Mizoram'	,'	1811.10	'	,'	39	'	,'	103000',	NULL,	NULL,'	100',	NULL,'	100','	100')	")

        con.commit()
    except Exception as ex:
        print(ex)
    con.close()


def create_db():
    con = sqlite3.connect(database=r'ticketing.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS passenger(pid INTEGER PRIMARY KEY AUTOINCREMENT, fname text, lname text, phone text, email text, fromD text, toD text, totseat text, aduseat text, chiseat text, oldseat  text, type text, mealcost text, totfare text, pstatus text, bookingid text, transacttionid text, class text, noofmeals text, pricepermeal text)")

    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS bus(fromD text, toD text,kms text, hrs text, departure text, arrival text,type text, totseats text, fare text, mealcost text, petrolrate text)")
    con.commit()
    # (fromD varchar (30) , toD varchar (30), kms float(10) ,hrs int (2),departure Time (3),arrival Time (3),type char (2) ,tseats int (3),fare float (10),mealCost int (4),petrolrate int (3))

    # cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    # con.commit()

    # cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT, Category text, Supplier text, Name text , price text , qty text, status text)")
    # con.commit()

    # cur.execute("CREATE TABLE IF NOT EXISTS customer(billno INTEGER PRIMARY KEY , name text, contact text,price text, date text)")
    # con.commit()
    con.close()


create_db()

con = sqlite3.connect(database=r'ticketing.db')
cur = con.cursor()
cur.execute("select * from bus")
res=cur.fetchall()
# print(len(res))
if len(res)==0:
    insert_bus_data()
else:
    print("already exist")
