def sum_bytes(foi):
    return sum(field[1] for field in foi)


def extract_dic(msgtype):
    #Main Message List:
    if msgtype == '0109':
        field0109 = [
            ("Header 1",1,'uint8',''),
            ("Data Length",2,'uint16',1),
            ('Message Type',2,'uint16',1),
            ('Interface Major Version',1,'uint8',1),
            ('Interface Minor Version',1,'uint8',1),
            ('UAV Control Client ID',1,'uint8',1),
            ('UAV Type',1,'uint8',1),
            ('UAV Variant (Reserved)',1,'uint8',1),
            ('UAV ID',2,'uint16',1),
            ('Mission Time',4,'uint32',0.001),
            ('UNIX Timestamp UTC',8,'uint64',1)]
        return field0109
    
    #Sub Message List
    if msgtype == '0001':
        field0001 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('Nav Sensor Failure Bitfield',2,'uint16',1)
        ]
        results = sum_bytes(field0001)
        return field0001, results

    if msgtype == '0002':
        field0002 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('RCC Failure Bitfield',2,'uint16',1)
        ]
        results = sum_bytes(field0002)
        return field0002, results

    if msgtype == '0003':
        field0003 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('RPDB Status Bitfield',1,'uint8',1)
        ]
        results = sum_bytes(field0003)
        return field0003, results

    if msgtype == '0004':
        field0004 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('Battery Status Bitfield',2,'uint16',1)
        ]
        results = sum_bytes(field0004)
        return field0004, results

    if msgtype == '0005':
        field0005 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('DroPort Status Bitfield',1,'uint8',1)
        ]
        results = sum_bytes(field0005)
        return field0005, results

    if msgtype == '0006':
        field0006 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('UWB Failure Bitfield',1,'uint8',1)
        ]
        results = sum_bytes(field0006)
        return field0006, results

    if msgtype == '0007':
        field0007 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('RTK Failure Bitfield',2,'uint16',1)
        ]
        results = sum_bytes(field0007)
        return field0007, results

    if msgtype == '0008':
        field0008 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('CA Status Bitfield',1,'uint8',1),
            ("CA Failure Bitfield",2,'uint16','1')
        ]
        results = sum_bytes(field0008)
        return field0008, results

    if msgtype == '0009':
        field0009 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('Flight Status Bitfield',1,'uint8',1),
            ('Motor Fail Id',1,'uint8','')
        ]
        results = sum_bytes(field0009)
        return field0009, results

    if msgtype == '0010':
        field0010 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('Geofence Status Bitfield',1,'uint8',1)
        ]
        results = sum_bytes(field0010)
        return field0010, results

    if msgtype == '0011':
        field0011 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('Flight Comms Status Bitfield',1,'uint8',1)
        ]
        results = sum_bytes(field0011)
        return field0011, results

    if msgtype == '00FF':
        field00FF = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('IMU-Sensor Failure Bit',1,'uint8',1)
        ]
        results = sum_bytes(field00FF)
        return field00FF, results

    if msgtype == '1000':
        field1000 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('Sensor Source Bitfield',1,'uint16',1)
        ]
        results = sum_bytes(field1000)
        return field1000, results

    if msgtype == '1001':
        field1001 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('Active IMU Gx',2,'int16',0.01),
            ('Active IMU Gy',2,'int16',0.01),
            ('Active IMU Gz',2,'int16',0.01),
            ('Active IMU Ax',2,'int16',0.001),
            ('Active IMU Ay',2,'int16',0.001),
            ('Active IMU Az',2,'int16',0.001),
            ('Active IMU Gx MA',2,'int16',0.01),
            ('Active IMU Gy MA',2,'int16',0.01),
            ('Active IMU Gz MA',2,'int16',0.01),
            ('Active IMU Ax MA',2,'int16',0.001),
            ('Active IMU Ay MA',2,'int16',0.001),
            ('Active IMU Az MA',2,'int16',0.001)
        ]
        results = sum_bytes(field1001)
        return field1001, results

    if msgtype == '1002':
        field1002 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('Active Mag Mx',2,'int16',0.1),
            ('Active Mag My',2,'int16',0.1),
            ('Active Mag Mz',2,'int16',0.1),
            ('Active Mag Bx',2,'int16',0.1),
            ('Active Mag By',2,'int16',0.1),
            ('Active Mag Bz',2,'int16',0.1),
            ('Active Mag Heading',2,'int16',0.01),
            ('Active Mag Status',1,'uint8',1)
        ]
        results = sum_bytes(field1002)
        return field1002, results

    if msgtype == '1003':
        field1003 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('Active Baro Pressure',4,'int32',0.01),
            ('Active Baro Altitude',4,'int32',0.01)
        ]
        return field1003, sum_bytes(field1003)

    if msgtype == '1004':
        field1004 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ('Active GNSS GPS ToW',4,'uint32',0.001),
            ('Active GNSS Msg Latency',4,'uint32',1),
            ('Active GNSS Fix Status',1,'uint8',1),
            ('Active GNSS Satellite Nbr',1,'uint8',1),
            ('Active GNSS PDOP',1,'uint8',0.1),
            ('Active GNSS Hacc',1,'uint8',0.1),
            ('Active GNSS Vacc',1,'uint8',0.1),
            ('Active GNSS Latitude',4,'int32',1.0e-7),
            ('Active GNSS Longitude',4,'int32',1.0e-7),
            ('Active GNSS Altitude',4,'int32',0.01),
            ('Active GNSS VelE',2,'int16',0.01),
            ('Active GNSS VelN',2,'int16',0.01),
            ('Active GNSS VelU',2,'int16',0.01)
        ]
        return field1004, sum_bytes(field1004)

    if msgtype == '1010':
        field1010 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("WMM Status",1,'uint8',1),
            ("Mag Declination",2,'int16',0.01),
            ("Mag Inclination",2,'int16',0.01),
            ("Mag Total Intensity",2,'uint16',0.1),
            ("Mag Horizontal Intensity",2,'uint16',0.1)
        ]
        return field1010, sum_bytes(field1010)

    if msgtype == '1100':
        field1100 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Active NavSoln CBIT Bitfield",8,'uint64',1),
            ("Active Nav Alt Filter Source",1,'uint8',1),
            ("Active Nav Yaw Filter Source",1,'uint8',1)
        ]
        return field1100, sum_bytes(field1100)

    if msgtype == '1101':
        field1101 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Active Nav Rate P",2,'int16',0.01),
            ("Active Nav Rate Q",2,'int16',0.01),
            ("Active Nav Rate R",2,'int16',0.01),
            ("Active Nav Acc X",2,'int16',0.001),
            ("Active Nav Acc Y",2,'int16',0.001),
            ("Active Nav Acc Z",2,'int16',0.001),
            ("Active Nav Acc E",2,'int16',0.001),
            ("Active Nav Acc N",2,'int16',0.001),
            ("Active Nav Acc U",2,'int16',0.001),
            ("Active Nav Gravity",2,'int16',0.001)
        ]
        return field1101, sum_bytes(field1101)

    if msgtype == '1102':
        field1102 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Active Nav Roll",2,'int16',0.01),
            ("Active Nav Pitch",2,'int16',0.01),
            ("Active Nav Yaw",2,'int16',0.01)
        ]
        return field1102, sum_bytes(field1102)

    if msgtype == '1103':
        field1103 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Active Nav VelE",2,'int16',0.01),
            ("Active Nav VelN",2,'int16',0.01),
            ("Active Nav VelU",2,'int16',0.01)
        ]
        return field1103, sum_bytes(field1103)

    if msgtype == '1104':
        field1104 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Active Nav Latitude",4,'int32',1.0e-7),
            ("Active Nav Longitude",4,'int32',1.0e-7),
            ("Active Nav Altitude (Uncorrected)",4,'int32',0.01),
            ("Active Nav Altitude (AMSL)",4,'int32',0.01),
            ("Active Nav Height (AGL)",4,'int32',0.01)
        ]
        return field1104, sum_bytes(field1104)

    if msgtype == '1105':
        field1105 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Active Nav Alt Correction Src",1,'uint8',1),
            ("Active Nav Alt Correction",4,'int32',0.01)
        ]
        return field1105, sum_bytes(field1105)

    if msgtype == '1111':
        field1111 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Gnd Station Ref",1,'uint8',1),
            ("Gnd Pressure Ref",4,'uint32',0.01)
        ]
        return field1111, sum_bytes(field1111)

    if msgtype == '1112':
        field1112 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Gnd Elev Ref Src",1,'uint8',1),
            ("Gnd Elev Ref",4,'int32',0.01)
        ]
        return field1112, sum_bytes(field1112)

    if msgtype == '1113':
        field1113 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Takeoff Point Elevation",4,'int32',0.01)
        ]
        return field1113, sum_bytes(field1113)

    if msgtype == '1200':
        field1200 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Target P",2,'int16',0.01),
            ("Target Q",2,'int16',0.01),
            ("Target R",2,'int16',0.01)
        ]
        return field1200, sum_bytes(field1200)

    if msgtype == '1201':
        field1201 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Target Roll",2,'int16',0.01),
            ("Target Pitch",2,'int16',0.01),
            ("Target Yaw",2,'int16',0.01)
        ]
        return field1201, sum_bytes(field1201)

    if msgtype == '1202':
        field1202 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Target VelE",2,'int16',0.01),
            ("Target VelN",2,'int16',0.01),
            ("Target VelU",2,'int16',0.01)
        ]
        return field1202, sum_bytes(field1202)

    if msgtype == '1203':
        field1203 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Target Latitude",4,'int32',0.0000001),
            ("Target Longitude",4,'int32',0.0000001),
            ("Target Altitude",4,'int32',0.01)
        ]
        return field1203, sum_bytes(field1203)
    if msgtype == '1301':
        field1301 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Ctrl Effort Roll",2,'int16',0.1),
            ("Ctrl Effort Pitch",2,'int16',0.1),
            ("Ctrl Effort Yaw",2,'int16',0.1),
            ("Ctrl Effort Throttle",2,'uint16',0.1)
        ]
        return field1301, sum_bytes(field1301)

    if msgtype == '1302':
        field1302 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Motor M1 PWM",2,'uint16',0.1),
            ("Motor M2 PWM",2,'uint16',0.1),
            ("Motor M3 PWM",2,'uint16',0.1),
            ("Motor M4 PWM",2,'uint16',0.1),
            ("Motor M5 PWM",2,'uint16',0.1),
            ("Motor M6 PWM",2,'uint16',0.1)
        ]
        return field1302, sum_bytes(field1302)

    if msgtype == '2001':
        field2001 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU0 Gx",2,'int16',0.01),
            ("IMU0 Gy",2,'int16',0.01),
            ("IMU0 Gz",2,'int16',0.01),
            ("IMU0 Ax",2,'int16',0.001),
            ("IMU0 Ay",2,'int16',0.001),
            ("IMU0 Az",2,'int16',0.001),
            ("IMU0 Gx MA",2,'int16',0.01),
            ("IMU0 Gy MA",2,'int16',0.01),
            ("IMU0 Gz MA",2,'int16',0.01),
            ("IMU0 Ax MA",2,'int16',0.001),
            ("IMU0 Ay MA",2,'int16',0.001),
            ("IMU0 Az MA",2,'int16',0.001)
        ]
        return field2001, sum_bytes(field2001)

    if msgtype == '2002':
        field2002 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU1 Gx",2,'int16',0.01),
            ("IMU1 Gy",2,'int16',0.01),
            ("IMU1 Gz",2,'int16',0.01),
            ("IMU1 Ax",2,'int16',0.001),
            ("IMU1 Ay",2,'int16',0.001),
            ("IMU1 Az",2,'int16',0.001),
            ("IMU1 Gx MA",2,'int16',0.01),
            ("IMU1 Gy MA",2,'int16',0.01),
            ("IMU1 Gz MA",2,'int16',0.01),
            ("IMU1 Ax MA",2,'int16',0.001),
            ("IMU1 Ay MA",2,'int16',0.001),
            ("IMU1 Az MA",2,'int16',0.001)
        ]
        return field2002, sum_bytes(field2002)

    if msgtype == '2003':
        field2003 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU2 Gx",2,'int16',0.01),
            ("IMU2 Gy",2,'int16',0.01),
            ("IMU2 Gz",2,'int16',0.01),
            ("IMU2 Ax",2,'int16',0.001),
            ("IMU2 Ay",2,'int16',0.001),
            ("IMU2 Az",2,'int16',0.001),
            ("IMU2 Gx MA",2,'int16',0.01),
            ("IMU2 Gy MA",2,'int16',0.01),
            ("IMU2 Gz MA",2,'int16',0.01),
            ("IMU2 Ax MA",2,'int16',0.001),
            ("IMU2 Ay MA",2,'int16',0.001),
            ("IMU2 Az MA",2,'int16',0.001)
        ]
        return field2003, sum_bytes(field2003)

    if msgtype == '2101':
        field2101 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Mag0 Mx",2,'int16',0.1),
            ("Mag0 My",2,'int16',0.1),
            ("Mag0 Mz",2,'int16',0.1),
            ("Mag0 Heading",2,'int16',0.01),
            ("Mag0 Status",1,'uint8',1)
        ]
        return field2101, sum_bytes(field2101)

    if msgtype == '2102':
        field2102 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Mag1 Mx",2,'int16',0.1),
            ("Mag1 My",2,'int16',0.1),
            ("Mag1 Mz",2,'int16',0.1),
            ("Mag1 Heading",2,'int16',0.01),
            ("Mag1 Status",1,'uint8',1)
        ]
        return field2102, sum_bytes(field2102)

    if msgtype == '2103':
        field2103 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Mag2 Mx",2,'int16',0.1),
            ("Mag2 My",2,'int16',0.1),
            ("Mag2 Mz",2,'int16',0.1),
            ("Mag2 Heading",2,'int16',0.01),
            ("Mag2 Status",1,'uint8',1)
        ]
        return field2103, sum_bytes(field2103)

    if msgtype == '2201':
        field2201 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Baro0 Press",4,'int32',0.01),
            ("Baro0 Altitude",4,'int32',0.01)
        ]
        return field2201, sum_bytes(field2201)

    if msgtype == '2202':
        field2202 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Baro1 Press",4,'int32',0.01),
            ("Baro1 Altitude",4,'int32',0.01)
        ]
        return field2202, sum_bytes(field2202)

    if msgtype == '2203':
        field2203 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Baro2 Press",4,'int32',0.01),
            ("Baro2 Altitude",4,'int32',0.01)
        ]
        return field2203, sum_bytes(field2203)

    if msgtype == '2301':
        field2301 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("GNSS0 GPS ToW",4,'uint32',0.001),
            ("GNSS0 Msg Latency",4,'uint32',1),
            ("GNSS0 Fix Status",1,'uint8',1),
            ("GNSS0 Nbr Satellite",1,'uint8',1),
            ("GNSS0 PDOP",1,'uint8',0.1),
            ("GNSS0 Hacc",1,'uint8',0.1),
            ("GNSS0 Vacc",1,'uint8',0.1),
            ("GNSS0 Latitude",4,'int32',1e-7),
            ("GNSS0 Longitude",4,'int32',1e-7),
            ("GNSS0 Altitude",4,'int32',0.01),
            ("GNSS0 VelE",2,'int16',0.01),
            ("GNSS0 VelN",2,'int16',0.01),
            ("GNSS0 VelU",2,'int16',0.01)
        ]
        return field2301, sum_bytes(field2301)

    if msgtype == '2302':
        field2302 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("GNSS1 GPS ToW",4,'uint32',0.001),
            ("GNSS1 Msg Latency",4,'uint32',1),
            ("GNSS1 Fix Status",1,'uint8',1),
            ("GNSS1 Nbr Satellite",1,'uint8',1),
            ("GNSS1 PDOP",1,'uint8',0.1),
            ("GNSS1 Hacc",1,'uint8',0.1),
            ("GNSS1 Vacc",1,'uint8',0.1),
            ("GNSS1 Latitude",4,'int32',1e-7),
            ("GNSS1 Longitude",4,'int32',1e-7),
            ("GNSS1 Altitude",4,'int32',0.01),
            ("GNSS1 VelE",2,'int16',0.01),
            ("GNSS1 VelN",2,'int16',0.01),
            ("GNSS1 VelU",2,'int16',0.01)
        ]
        return field2302, sum_bytes(field2302)

    if msgtype == '2303':
        field2303 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("GNSS2 GPS ToW",4,'uint32',0.001),
            ("GNSS2 Msg Latency",4,'uint32',1),
            ("GNSS2 Fix Status",1,'uint8',1),
            ("GNSS2 Nbr Satellite",1,'uint8',1),
            ("GNSS2 PDOP",1,'uint8',0.1),
            ("GNSS2 Hacc",1,'uint8',0.1),
            ("GNSS2 Vacc",1,'uint8',0.1),
            ("GNSS2 Latitude",4,'int32',1e-7),
            ("GNSS2 Longitude",4,'int32',1e-7),
            ("GNSS2 Altitude",4,'int32',0.01),
            ("GNSS2 VelE",2,'int16',0.01),
            ("GNSS2 VelN",2,'int16',0.01),
            ("GNSS2 VelU",2,'int16',0.01)
        ]
        return field2303, sum_bytes(field2303)

    if msgtype == '2401':
        field2401 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Lidar0 Distance",2,'uint16',1)
        ]
        return field2401, sum_bytes(field2401)

    if msgtype == '2501':
        field2501 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Radar0L Distance",2,'uint16',0.01),
            ("Radar0L Bearing",2,'int16',0.01),
            ("Radar0L Relative Velocity",2,'int16',0.01),
            ("Radar0L Relative Heading",2,'int16',0.01),
            ("Radar0L Filtered Obstacle Distance",2,'uint16',0.01)
        ]
        return field2501, sum_bytes(field2501)

    if msgtype == '2502':
        field2502 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Radar60 Distance",2,'uint16',0.01),
            ("Radar60 Bearing",2,'int16',0.01),
            ("Radar60 Relative Velocity",2,'int16',0.01),
            ("Radar60 Relative Heading",2,'int16',0.01),
            ("Radar60 Filtered Obstacle Distance",2,'uint16',0.01)
        ]
        return field2502, sum_bytes(field2502)

    if msgtype == '2503':
        field2503 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Radar120 Distance",2,'uint16',0.01),
            ("Radar120 Bearing",2,'int16',0.01),
            ("Radar120 Relative Velocity",2,'int16',0.01),
            ("Radar120 Relative Heading",2,'int16',0.01),
            ("Radar120 Filtered Obstacle Distance",2,'uint16',0.01)
        ]
        return field2503, sum_bytes(field2503)

    if msgtype == '2504':
        field2504 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Radar180 Distance",2,'uint16',0.01),
            ("Radar180 Bearing",2,'int16',0.01),
            ("Radar180 Relative Velocity",2,'int16',0.01),
            ("Radar180 Relative Heading",2,'int16',0.01),
            ("Radar180 Filtered Obstacle Distance",2,'uint16',0.01)
        ]
        return field2504, sum_bytes(field2504)

    if msgtype == '2505':
        field2505 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Radar240 Distance",2,'uint16',0.01),
            ("Radar240 Bearing",2,'int16',0.01),
            ("Radar240 Relative Velocity",2,'int16',0.01),
            ("Radar240 Relative Heading",2,'int16',0.01),
            ("Radar240 Filtered Obstacle Distance",2,'uint16',0.01)
        ]
        return field2505, sum_bytes(field2505)

    if msgtype == '2506':
        field2506 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Radar300 Distance",2,'uint16',0.01),
            ("Radar300 Bearing",2,'int16',0.01),
            ("Radar300 Relative Velocity",2,'int16',0.01),
            ("Radar300 Relative Heading",2,'int16',0.01),
            ("Radar300 Filtered Obstacle Distance",2,'uint16',0.01)
        ]
        return field2506, sum_bytes(field2506)

    if msgtype == '2507':
        field2507 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Radar0U Distance",2,'uint16',0.01),
            ("Radar0U Bearing",2,'int16',0.01),
            ("Radar0U Relative Velocity",2,'int16',0.01),
            ("Radar0U Relative Heading",2,'int16',0.01),
            ("Radar0U Filtered Obstacle Distance",2,'uint16',0.01)
        ]
        return field2507, sum_bytes(field2507)

        # Pri IMU Nav Orientation Data
    if msgtype == '3001':
        field3001 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU0 Nav Roll",2,'int16',0.01),
            ("IMU0 Nav Pitch",2,'int16',0.01),
            ("IMU0 Nav Yaw",2,'int16',0.01)
        ]
        return field3001, sum_bytes(field3001)

    # Sec IMU Nav Orientation Data
    if msgtype == '3002':
        field3002 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU1 Nav Roll",2,'int16',0.01),
            ("IMU1 Nav Pitch",2,'int16',0.01),
            ("IMU1 Nav Yaw",2,'int16',0.01)
        ]
        return field3002, sum_bytes(field3002)

    # Ter IMU Nav Orientation Data
    if msgtype == '3003':
        field3003 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU2 Nav Roll",2,'int16',0.01),
            ("IMU2 Nav Pitch",2,'int16',0.01),
            ("IMU2 Nav Yaw",2,'int16',0.01)
        ]
        return field3003, sum_bytes(field3003)

    # Pri IMU Nav Velocity Data
    if msgtype == '3004':
        field3004 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU0 Nav VelE",2,'int16',0.01),
            ("IMU0 Nav VelN",2,'int16',0.01),
            ("IMU0 Nav VelU",2,'int16',0.01)
        ]
        return field3004, sum_bytes(field3004)

    # Sec IMU Nav Velocity Data
    if msgtype == '3005':
        field3005 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU1 Nav VelE",2,'int16',0.01),
            ("IMU1 Nav VelN",2,'int16',0.01),
            ("IMU1 Nav VelU",2,'int16',0.01)
        ]
        return field3005, sum_bytes(field3005)

    # Ter IMU Nav Velocity Data
    if msgtype == '3006':
        field3006 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU2 Nav VelE",2,'int16',0.01),
            ("IMU2 Nav VelN",2,'int16',0.01),
            ("IMU2 Nav VelU",2,'int16',0.01)
        ]
        return field3006, sum_bytes(field3006)

    # Pri IMU Nav Position Data
    if msgtype == '3007':
        field3007 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU0 Nav Latitude",4,'int32',1e-7),
            ("IMU0 Nav Longitude",4,'int32',1e-7),
            ("IMU0 Nav Altitude",4,'int32',0.01)
        ]
        return field3007, sum_bytes(field3007)

    # Sec IMU Nav Position Data
    if msgtype == '3008':
        field3008 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU1 Nav Latitude",4,'int32',1e-7),
            ("IMU1 Nav Longitude",4,'int32',1e-7),
            ("IMU1 Nav Altitude",4,'int32',0.01)
        ]
        return field3008, sum_bytes(field3008)

    # Ter IMU Nav Position Data
    if msgtype == '3009':
        field3009 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU2 Nav Latitude",4,'int32',1e-7),
            ("IMU2 Nav Longitude",4,'int32',1e-7),
            ("IMU2 Nav Altitude",4,'int32',0.01)
        ]
        return field3009, sum_bytes(field3009)

    # Active FCC Nav Rdy Bitfield
    if msgtype == '3F00':
        field3F00 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Active FCC Nav Rdy Bitfield",1,'uint8',1)
        ]
        return field3F00, sum_bytes(field3F00)

    # Pri IMU Nav Rdy Bitfield
    if msgtype == '3F01':
        field3F01 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU0 Nav Rdy Bitfield",1,'uint8',1)
        ]
        return field3F01, sum_bytes(field3F01)

    # Sec IMU Nav Rdy Bitfield
    if msgtype == '3F02':
        field3F02 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU1 Nav Rdy Bitfield",1,'uint8',1)
        ]
        return field3F02, sum_bytes(field3F02)

    # Ter IMU Nav Rdy Bitfield
    if msgtype == '3F03':
        field3F03 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("IMU2 Nav Rdy Bitfield",1,'uint8',1)
        ]
        return field3F03, sum_bytes(field3F03)

    # Sec FCC Nav Rdy Bitfield
    if msgtype == '3F04':
        field3F04 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Sec FCC Nav Rdy Bitfield",1,'uint8',1)
        ]
        return field3F04, sum_bytes(field3F04)

    # Precision Landing Status Info Data
    if msgtype == '4000':
        field4000 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("DroPort Mode",1,'uint8',1),
            ("DroPort Status",1,'uint8',1),
            ("Precision Landing Sensor Source",1,'uint8',1),
            ("Precision Landing Status",1,'uint8',1)
        ]
        return field4000, sum_bytes(field4000)

    # DroPort Pairing Info Data
    if msgtype == '4001':
        field4001 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("DroPort Info Status",1,'uint8',1),
            ("Paired DroPort Type",1,'uint8',1),
            ("Paired DroPort ID",2,'uint16',1)
        ]
        return field4001, sum_bytes(field4001)

    # Base Station Pairing Info Data
    if msgtype == '4002':
        field4002 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Base Station Info Status",1,'uint8',1),
            ("Paired Base Station Type",1,'uint8',1),
            ("Paired Base Station ID",2,'uint16',1)
        ]
        return field4002, sum_bytes(field4002)

    # UWB System Status Info Data
    if msgtype == '4101':
        field4101 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("UWB System Status",1,'uint8',1)
        ]
        return field4101, sum_bytes(field4101)

    # UWB Baseline Offset Info Data
    if msgtype == '4102':
        field4102 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("UWB Baseline Offset X",2,'int16',0.01),
            ("UWB Baseline Offset Y",2,'int16',0.01),
            ("UWB Baseline Altitude",2,'int16',0.1),
            ("UWB Baseline Heading",2,'int16',0.1)
        ]
        return field4102, sum_bytes(field4102)

    # Active UWB Air Node Data
    if msgtype == '4111':
        field4111 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Active UWB Ant Source",1,'uint8',1),
            ("Active UWB No. of Ground Nodes",1,'uint8',1),
            ("Active UWB Air Node X-Axis Position",2,'int16',0.01),
            ("Active UWB Air Node Y-Axis Position",2,'int16',0.01),
            ("Active UWB Air Node Z-Axis Position",2,'int16',0.01)
        ]
        return field4111, sum_bytes(field4111)

    # Active Nav UWB Info Data
    if msgtype == '4120':
        field4120 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("Active Nav UWB Soln Status",2,'uint16',1),
            ("Active Nav UWB Vel X",2,'int16',0.01),
            ("Active Nav UWB Vel Y",2,'int16',0.01),
            ("Active Nav UWB Pos X",2,'int16',0.01),
            ("Active Nav UWB Pos Y",2,'int16',0.01),
            ("Active Nav UWB Alt Correction",4,'int32',0.01)
        ]
        return field4120, sum_bytes(field4120)

    # RTK System Status Info Data
    if msgtype == '4201':
        field4201 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("RTK System Status",1,'uint8',1)
        ]
        return field4201, sum_bytes(field4201)

    # RTK Baseline Offset Info Data
    if msgtype == '4202':
        field4202 = [
            ("Message Type",2,'uint16',''),
            ("Message Length",1,'uint8',1),
            ("RTK Baseline Offset X",2,'int16',0.01),
            ("RTK Baseline Offset Y",2,'int16',0.01),
            ("RTK Baseline Offset Z",2,'int16',0.01),
            ("RTK Baseline Offset Yaw",2,'int16',0.01)
        ]
        return field4202, sum_bytes(field4202)

    # Active RTK Data
    if msgtype == '4210':
        field4210 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Active RTK Source", 1, 'uint8', 1),
            ("Active RTK GPS ToW", 4, 'uint32', 0.001),
            ("Active RTK Msg Latency", 4, 'uint32', 1),
            ("Active RTK Fix Status", 1, 'uint8', 1),
            ("Active RTK Nbr Satellite", 1, 'uint8', 1),
            ("Active RTK PDOP", 1, 'uint8', 0.1),
            ("Active RTK Hacc", 2, 'uint16', 0.001),
            ("Active RTK Vacc", 2, 'uint16', 0.001),
            ("Active RTK Rel PosE", 4, 'int32', 0.01),
            ("Active RTK Rel PosN", 4, 'int32', 0.01),
            ("Active RTK Rel PosU", 4, 'int32', 0.01),
            ("Active RTK Latitude", 4, 'int32', 1e-7),
            ("Active RTK Longitude", 4, 'int32', 1e-7),
            ("Active RTK Altitude", 4, 'int32', 0.01),
            ("Active RTK VelE", 2, 'int16', 0.01),
            ("Active RTK VelN", 2, 'int16', 0.01),
            ("Active RTK VelU", 2, 'int16', 0.01),
            ("Active RTK Roll", 2, 'int16', 0.01),
            ("Active RTK Pitch", 2, 'int16', 0.01),
            ("Active RTK Yaw", 2, 'int16', 0.01),
            ("Active RTK Yaw Acc", 2, 'int16', 0.01)
        ]
        return field4210, sum_bytes(field4210)
    # Pri RTK Data
    if msgtype == '4211':
        field4211 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("RTK0 GPS ToW", 4, 'uint32', 0.001),
            ("RTK0 Msg Latency", 4, 'uint32', 1),
            ("RTK0 Fix Status", 1, 'uint8', 1),
            ("RTK0 Nbr Satellite", 1, 'uint8', 1),
            ("RTK0 PDOP", 1, 'uint8', 0.1),
            ("RTK0 Hacc", 2, 'uint16', 0.001),
            ("RTK0 Vacc", 2, 'uint16', 0.001),
            ("RTK0 Rel PosE", 4, 'int32', 0.01),
            ("RTK0 Rel PosN", 4, 'int32', 0.01),
            ("RTK0 Rel PosU", 4, 'int32', 0.01),
            ("RTK0 Latitude", 4, 'int32', 1e-7),
            ("RTK0 Longitude", 4, 'int32', 1e-7),
            ("RTK0 Altitude", 4, 'int32', 0.01),
            ("RTK0 VelE", 2, 'int16', 0.01),
            ("RTK0 VelN", 2, 'int16', 0.01),
            ("RTK0 VelU", 2, 'int16', 0.01),
            ("RTK0 Roll", 2, 'int16', 0.01),
            ("RTK0 Pitch", 2, 'int16', 0.01),
            ("RTK0 Yaw", 2, 'int16', 0.01),
            ("RTK0 Yaw Acc", 2, 'int16', 0.01)
        ]
        return field4211, sum_bytes(field4211)
    # -----------------------
# Sec RTK Data
# -----------------------
    if msgtype == '4212':
        field4212 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("RTK1 GPS ToW", 4, 'uint32', 0.001),
            ("RTK1 Msg Latency", 4, 'uint32', 1),
            ("RTK1 Fix Status", 1, 'uint8', 1),
            ("RTK1 Nbr Satellite", 1, 'uint8', 1),
            ("RTK1 PDOP", 1, 'uint8', 0.1),
            ("RTK1 Hacc", 2, 'uint16', 0.001),
            ("RTK1 Vacc", 2, 'uint16', 0.001),
            ("RTK1 Rel PosE", 4, 'int32', 0.01),
            ("RTK1 Rel PosN", 4, 'int32', 0.01),
            ("RTK1 Rel PosU", 4, 'int32', 0.01),
            ("RTK1 Latitude", 4, 'int32', 1e-7),
            ("RTK1 Longitude", 4, 'int32', 1e-7),
            ("RTK1 Altitude", 4, 'int32', 0.01),
            ("RTK1 VelE", 2, 'int16', 0.01),
            ("RTK1 VelN", 2, 'int16', 0.01),
            ("RTK1 VelU", 2, 'int16', 0.01),
            ("RTK1 Roll", 2, 'int16', 0.01),
            ("RTK1 Pitch", 2, 'int16', 0.01),
            ("RTK1 Yaw", 2, 'int16', 0.01),
            ("RTK1 Yaw Acc", 2, 'int16', 0.01)
        ]
        return field4212, sum_bytes(field4212)
    # Ter RTK Data
    if msgtype == '4213':
        field4213 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("RTK2 GPS ToW", 4, 'uint32', 0.001),
            ("RTK2 Msg Latency", 4, 'uint32', 1),
            ("RTK2 Fix Status", 1, 'uint8', 1),
            ("RTK2 Nbr Satellite", 1, 'uint8', 1),
            ("RTK2 PDOP", 1, 'uint8', 0.1),
            ("RTK2 Hacc", 2, 'uint16', 0.001),
            ("RTK2 Vacc", 2, 'uint16', 0.001),
            ("RTK2 Rel PosE", 4, 'int32', 0.01),
            ("RTK2 Rel PosN", 4, 'int32', 0.01),
            ("RTK2 Rel PosU", 4, 'int32', 0.01),
            ("RTK2 Latitude", 4, 'int32', 1e-7),
            ("RTK2 Longitude", 4, 'int32', 1e-7),
            ("RTK2 Altitude", 4, 'int32', 0.01),
            ("RTK2 VelE", 2, 'int16', 0.01),
            ("RTK2 VelN", 2, 'int16', 0.01),
            ("RTK2 VelU", 2, 'int16', 0.01),
            ("RTK2 Roll", 2, 'int16', 0.01),
            ("RTK2 Pitch", 2, 'int16', 0.01),
            ("RTK2 Yaw", 2, 'int16', 0.01),
            ("RTK2 Yaw Acc", 2, 'int16', 0.01)
        ]
        return field4213, sum_bytes(field4213)
    # Active Nav RTK Data
    if msgtype == '4220':
        field4220 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Active Nav RTK Soln BIT", 4, 'uint32', 1),
            ("Active Nav RTK Soln Status", 1, 'uint8', 1),
            ("Active Nav RTK VelE", 2, 'int16', 0.01),
            ("Active Nav RTK VelN", 2, 'int16', 0.01),
            ("Active Nav RTK Latitude", 4, 'int32', 1e-7),
            ("Active Nav RTK Longitude", 4, 'int32', 1e-7),
            ("Active Nav RTK Alt Correction", 4, 'int32', 0.01),
            ("Active Nav RTK Rel PosE", 4, 'int32', 0.01),
            ("Active Nav RTK Rel PosN", 4, 'int32', 0.01),
            ("Active Nav RTK Rel PosU", 4, 'int32', 0.01)
        ]
        return field4220, sum_bytes(field4220)
    # Pri IMU Nav RTK Data
    if msgtype == '4221':
        field4221 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("IMU0 Nav RTK VelE", 2, 'int16', 0.01),
            ("IMU0 Nav RTK VelN", 2, 'int16', 0.01),
            ("IMU0 Nav RTK Latitude", 4, 'int32', 1e-7),
            ("IMU0 Nav RTK Longitude", 4, 'int32', 1e-7),
            ("IMU0 Nav RTK Alt Correction", 4, 'int32', 0.01),
            ("IMU0 Nav RTK Rel PosE", 4, 'int32', 0.01),
            ("IMU0 Nav RTK Rel PosN", 4, 'int32', 0.01),
            ("IMU0 Nav RTK Rel PosU", 4, 'int32', 0.01)
        ]
        return field4221, sum_bytes(field4221)
    # Pri IMU Nav RTK Data
    # Sec IMU Nav RTK Data
    if msgtype == '4222':
        field4222 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("IMU1 Nav RTK VelE", 2, 'int16', 0.01),
            ("IMU1 Nav RTK VelN", 2, 'int16', 0.01),
            ("IMU1 Nav RTK Latitude", 4, 'int32', 1e-7),
            ("IMU1 Nav RTK Longitude", 4, 'int32', 1e-7),
            ("IMU1 Nav RTK Alt Correction", 4, 'int32', 0.01),
            ("IMU1 Nav RTK Rel PosE", 4, 'int32', 0.01),
            ("IMU1 Nav RTK Rel PosN", 4, 'int32', 0.01),
            ("IMU1 Nav RTK Rel PosU", 4, 'int32', 0.01)
        ]
        return field4222, sum_bytes(field4222)
    # Ter IMU Nav RTK Data
    if msgtype == '4223':
        field4223 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("IMU2 Nav RTK VelE", 2, 'int16', 0.01),
            ("IMU2 Nav RTK VelN", 2, 'int16', 0.01),
            ("IMU2 Nav RTK Latitude", 4, 'int32', 1e-7),
            ("IMU2 Nav RTK Longitude", 4, 'int32', 1e-7),
            ("IMU2 Nav RTK Alt Correction", 4, 'int32', 0.01),
            ("IMU2 Nav RTK Rel PosE", 4, 'int32', 0.01),
            ("IMU2 Nav RTK Rel PosN", 4, 'int32', 0.01),
            ("IMU2 Nav RTK Rel PosU", 4, 'int32', 0.01)
        ]
        return field4223, sum_bytes(field4223)
    # RTK Base Station Info Data
    if msgtype == '4301':
        field4301 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Base Station System Flags", 2, 'uint16', 1),
            ("Base Station Status Flags", 4, 'uint32', 1),
            ("Base Station Satellite Number", 1, 'uint8', 1),
            ("Base Station PDOP", 2, 'uint16', 0.1),
            ("Base Station HDOP", 2, 'uint16', 0.1),
            ("Base Station Hacc", 1, 'uint8', 0.1),
            ("Base Station Vacc", 1, 'uint8', 0.1),
            ("Base Station Latitude", 4, 'int32', 1e-7),
            ("Base Station Longitude", 4, 'int32', 1e-7),
            ("Base Station Altitude", 4, 'int32', 0.01),
            ("Base Station VelE", 2, 'int16', 0.01),
            ("Base Station VelN", 2, 'int16', 0.01),
            ("Base Station VelU", 2, 'int16', 0.01),
            ("Base Station Roll", 2, 'int16', 0.01),
            ("Base Station Pitch", 2, 'int16', 0.01),
            ("Base Station Yaw", 2, 'int16', 0.01)
        ]
        return field4301, sum_bytes(field4301)
    # -----------------------
# RFCC Status Info Data
# -----------------------
    if msgtype == '5001':
        field5001 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Nav Processor Temp", 2, 'int16', 0.01),
            ("Ctrl Processor Temp", 2, 'int16', 0.01),
            ("RFCC Pri/Active Status", 1, 'uint8', 1),
            ("Pri CBIT Bitfield", 4, 'uint32', 1),
            ("Sec CBIT Bitfield", 4, 'uint32', 1)
        ]
        return field5001, sum_bytes(field5001)
    # -----------------------
    # 15RPDB Status Info Data
    # -----------------------
    if msgtype == '5101':
        field5101 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Batt1 Voltage", 2, 'uint16', 0.01),
            ("Batt2 Voltage", 2, 'uint16', 0.01),
            ("Batt1 Temp", 1, 'int8', 1),
            ("Batt2 Temp", 1, 'int8', 1),
            ("Motor1 Current", 2, 'uint16', 0.01),
            ("Motor2 Current", 2, 'uint16', 0.01),
            ("Motor3 Current", 2, 'uint16', 0.01),
            ("Motor4 Current", 2, 'uint16', 0.01),
            ("Motor5 Current", 2, 'uint16', 0.01),
            ("Motor6 Current", 2, 'uint16', 0.01),
            ("BusA Current", 2, 'uint16', 0.01),
            ("BusB Current", 2, 'uint16', 0.01),
            ("15RPDB CBIT Bitfield", 8, 'uint64', 1)
        ]
        return field5101, sum_bytes(field5101)
    # -----------------------
    # 35RPDB Status Info Data
    # -----------------------
    if msgtype == '5102':
        field5102 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Batt1 Voltage", 2, 'uint16', 0.01),
            ("Batt2 Voltage", 2, 'uint16', 0.01),
            ("Batt1 Temp", 1, 'int8', 1),
            ("Batt2 Temp", 1, 'int8', 1),
            ("Motor1 Current", 2, 'uint16', 0.01),
            ("Motor2 Current", 2, 'uint16', 0.01),
            ("Motor3 Current", 2, 'uint16', 0.01),
            ("Motor4 Current", 2, 'uint16', 0.01),
            ("Motor5 Current", 2, 'uint16', 0.01),
            ("Motor6 Current", 2, 'uint16', 0.01),
            ("BusA Current", 2, 'uint16', 0.01),
            ("BusB Current", 2, 'uint16', 0.01),
            ("EP Current", 2, 'uint16', 0.01),
            ("35RPDB CBIT Bitfield", 8, 'uint64', 1),
            ("Aux VMon Status", 1, 'uint8', 1),
            ("Aux Batt1 Voltage", 2, 'uint16', 0.01),
            ("Aux Batt2 Voltage", 2, 'uint16', 0.01)
        ]
        return field5102, sum_bytes(field5102)
    # -----------------------
    # Flight Info Data
    # -----------------------
    if msgtype == '6000':
        field6000 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Sortie Count", 1, 'uint8', 1),
            ("System Battery", 2, 'uint16', 0.01),
            ("Flight Mode", 1, 'uint8', 1),
            ("Flight Sub Mode", 1, 'uint8', 1),
            ("Flight Failure Mode", 1, 'uint8', 1),
            ("Position Ctrl Mode", 1, 'uint8', 1),
            ("Target Flight Mode", 1, 'uint8', 1),
            ("Target Flight Sub Mode", 1, 'uint8', 1),
            ("Flight Mode Cmd Availability", 4, 'uint32', 1),
            ("UAV Status 1", 1, 'uint8', 1)
        ]
        return field6000, sum_bytes(field6000)
    # -----------------------
    # Flight Waypoint Info Data
    # -----------------------
    if msgtype == '6001':
        field6001 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Target Route Number", 1, 'uint8', 1),
            ("Target WP Number", 1, 'uint8', 1),
            ("Target WP Loiter Time", 2, 'uint16', 1),
            ("Target WP Latitude", 4, 'int32', 1e-7),
            ("Target WP Longitude", 4, 'int32', 1e-7)
        ]
        return field6001, sum_bytes(field6001)
    # -----------------------
    # Flight Plan Status Info Data
    # -----------------------
    if msgtype == '6002':
        field6002 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Uploading Status", 2, 'uint16', 1),
            ("FlyZone ID", 4, 'uint32', 1),
            ("Mission Route ID", 4, 'uint32', 1),
            ("Home Route ID", 4, 'uint32', 1),
            ("ELP ID", 4, 'uint32', 1),
            ("Syncing Status", 2, 'uint16', 1)
        ]
        return field6002, sum_bytes(field6002)
    # -----------------------
    # Flight Time Info Data
    # -----------------------
    if msgtype == '6003':
        field6003 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Elapsed Flight Time", 2, 'uint16', 1),
            ("Remaining Flight Time", 2, 'uint16', 1),
            ("RH Travel Time", 2, 'uint16', 1),
            ("ETA Time (Reserved)", 2, 'uint16', 1),
            ("Battery Discharge Boundary Time", 2, 'uint16', 1)
        ]
        return field6003, sum_bytes(field6003)
# -----------------------
# Subsystem Status Info Data
# -----------------------
    if msgtype == '6101':
        field6101 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Subsystem Status", 1, 'uint8', 1)
        ]
        return field6101, sum_bytes(field6101)
    # -----------------------
    # Joysticks Info Data
    # -----------------------
    if msgtype == '6102':
        field6102 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Joystick Cmd X", 1, 'int8', 1),
            ("Joystick Cmd Y", 1, 'int8', 1),
            ("Joystick Cmd Yaw", 2, 'int16', 0.01),
            ("Joystick Cmd Height", 2, 'int16', 0.01)
        ]
        return field6102, sum_bytes(field6102)
    # -----------------------
    # LTE Radio Info Data
    # -----------------------
    if msgtype == '9F01':
        field9F01 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Radio Availability and Active Indicator", 1, 'uint8', 1),
            ("Radio Access Tech", 1, 'uint8', 1),
            ("Pri Radio RSRP (wwan0)", 1, 'uint8', -1),
            ("Sec Radio RSRP (wwan1)", 1, 'uint8', -1),
            ("Pri Radio RSRQ (wwan0)", 1, 'uint8', -0.1),
            ("Sec Radio RSRQ (wwan1)", 1, 'uint8', -0.1),
            ("Pri Telco (wwan0)", 2, 'uint16', 1),
            ("Sec Telco (wwan1)", 2, 'uint16', 1)
        ]
        return field9F01, sum_bytes(field9F01)
    # -----------------------
    # Active Battery Data Source
    # -----------------------
    if msgtype == 'A000':
        fieldA000 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Battery Voltage", 2, 'uint16', 0.01),
            ("Battery Temperature", 2, 'int16', 0.1),
            ("Battery Percentage", 1, 'uint8', 1),
            ("Battery Cycle Count", 2, 'uint16', 1),
            ("Battery Health", 1, 'uint8', 1),
            ("Battery Voltage Data Source", 1, 'uint8', 1)
        ]
        return fieldA000, sum_bytes(fieldA000)
    # -----------------------
    # Battery 1 BMS Data
    # -----------------------
    if msgtype == 'A001':
        fieldA001 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Manufacturer Code", 2, 'uint16', 1),
            ("Battery 1 Model", 2, 'uint16', 1),
            ("Battery 1 Voltage", 2, 'uint16', 0.01),
            ("Battery 1 Current", 2, 'int16', 0.01),
            ("Battery 1 Temperature", 2, 'int16', 0.1),
            ("Battery 1 Percentage", 1, 'uint8', 1),
            ("Battery 1 Cycle Count", 2, 'uint16', 1),
            ("Battery 1 Health", 1, 'uint8', 1),
            ("Battery 1 Cell 1 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 2 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 3 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 4 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 5 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 6 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 7 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 8 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 9 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 10 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 11 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 12 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 13 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Cell 14 Voltage", 2, 'uint16', 0.001),
            ("Battery 1 Designed Capacity", 2, 'uint16', 1),
            ("Battery 1 Remaining Capacity", 2, 'uint16', 1),
            ("Battery 1 Error Code", 4, 'uint32', 1),
            ("Battery 1 Temperature Sensor 1", 2, 'int16', 0.1),
            ("Battery 1 Temperature Sensor 2", 2, 'int16', 0.1),
            ("Battery 1 Temperature Sensor 3", 2, 'int16', 0.1),
            ("Battery 1 Temperature Sensor 4", 2, 'int16', 0.1)
        ]
        return fieldA001, sum_bytes(fieldA001)
    # -----------------------
    # Battery 2 BMS Data
    # -----------------------
    if msgtype == 'A002':
        fieldA002 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Manufacturer Code", 2, 'uint16', 1),
            ("Battery 2 Model", 2, 'uint16', 1),
            ("Battery 2 Voltage", 2, 'uint16', 0.01),
            ("Battery 2 Current", 2, 'int16', 0.01),
            ("Battery 2 Temperature", 2, 'int16', 0.1),
            ("Battery 2 Percentage", 1, 'uint8', 1),
            ("Battery 2 Cycle Count", 2, 'uint16', 1),
            ("Battery 2 Health", 1, 'uint8', 1),
            ("Battery 2 Cell 1 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 2 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 3 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 4 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 5 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 6 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 7 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 8 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 9 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 10 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 11 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 12 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 13 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Cell 14 Voltage", 2, 'uint16', 0.001),
            ("Battery 2 Designed Capacity", 2, 'uint16', 1),
            ("Battery 2 Remaining Capacity", 2, 'uint16', 1),
            ("Battery 2 Error Code", 4, 'uint32', 1),
            ("Battery 2 Temperature Sensor 1", 2, 'int16', 0.1),
            ("Battery 2 Temperature Sensor 2", 2, 'int16', 0.1),
            ("Battery 2 Temperature Sensor 3", 2, 'int16', 0.1),
            ("Battery 2 Temperature Sensor 4", 2, 'int16', 0.1)
        ]
        return fieldA002, sum_bytes(fieldA002)
    # -----------------------
    # Winch Info Data
    # -----------------------
    if msgtype == 'A003':
        fieldA003 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Winch Flags", 1, 'uint8', 1),
            ("Winch Storage State", 1, 'uint8', 1),
            ("Winch Status", 1, 'uint8', 1),
            ("Winch Cutter Status", 1, 'uint8', 1),
            ("Winch Cutter Board Status", 1, 'uint8', 1),
            ("Winch FCC Cmd", 1, 'uint8', 1)
        ]
        return fieldA003, sum_bytes(fieldA003)               
    # -----------------------
    # Downward Lidar Data
    # -----------------------
    if msgtype == 'A100':
        fieldA100 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Raw Distance", 2, 'uint16', 0.01),
            ("True Distance", 2, 'uint16', 0.01),
            ("Confidence Level", 1, 'uint8', 1),
            ("Temperature", 1, 'int8', 1),
            ("Landing Status Bitfield", 1, 'uint8', 1)
        ]
        return fieldA100, sum_bytes(fieldA100) 
    # -----------------------
    # Software Version Info Data
    # -----------------------
    if msgtype == 'F001':
        fieldF001 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Major Version No.", 1, 'uint8', 1),
            ("Minor Version No.", 1, 'uint8', 1)
        ]
        return fieldF001, sum_bytes(fieldF001) 
    # -----------------------
    # Aircraft Config Info Data
    # -----------------------
    if msgtype == 'F002':
        fieldF002 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Aircraft Configuration Bitfield", 1, 'uint8', 1)
        ]
        return fieldF002, sum_bytes(fieldF002)
    # -----------------------
    # Config Params Info Data
    # -----------------------
    if msgtype == 'F003':
        fieldF003 = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Gain ID", 1, 'uint8', 1),
            ("Gain Value", 4, 'int32', 0.001),
            ("Gain Written Flag", 1, 'uint8', 1),
            ("Cal ID", 1, 'uint8', 1),
            ("Cal Value", 4, 'float32', 1),
            ("Cal Written Flag", 1, 'uint8', 1)
        ]
        return fieldF003, sum_bytes(fieldF003)
    # -----------------------
    # Engineering Data
    # -----------------------
    if msgtype == 'FFFF':
        fieldFFFF = [
            ("Message Type", 2, 'uint16', 1),
            ("Message Length", 1, 'uint8', 1),
            ("Engineering Data 1", 2, 'int16', 1),
            ("Engineering Data 2", 2, 'int16', 1),
            ("Engineering Data 3", 2, 'int16', 1),
            ("Engineering Data 4", 2, 'int16', 1),
            ("Engineering Data 5", 2, 'int16', 1),
            ("Engineering Data 6", 2, 'int16', 1),
            ("Engineering Data 7", 2, 'int16', 1),
            ("Engineering Data 8", 2, 'int16', 1),
            ("Engineering Data 9", 2, 'int16', 1),
            ("Engineering Data 10", 4, 'int32', 1),
            ("Engineering Data 11", 4, 'int32', 1),
            ("Engineering Data 12", 4, 'int32', 1)
        ]
        return fieldFFFF, sum_bytes(fieldFFFF)
