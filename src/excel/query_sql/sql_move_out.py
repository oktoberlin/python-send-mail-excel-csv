from src.excel.excel_format import *

sql_mov_out = """Select EIROUT.ContNo as 'Container No',ContainerDetails.Size,ContainerDetails.Type,
EIRIN.DateIn as 'Date In',LEFT(ContainerDetails.Payload,5) as Payload,ContainerDetails.Net as 'Tare',ContainerDetails.Datemnf as 'DMF',
EIROUT.Nomor as 'EIR Out',Concat(ExVessel,'-',ExVoy) as 'Ex Vessel-Voy',BookingNo as 'DO No.',DateOut as 'Date Out',
Concat(Vessel,'-',Voy) as 'Vessel-Voy',Destination,Shipper,EIROUT.VN as 'Truck No',
EIROUT.ContCondition as 'Condition',EIROUT.Seal as 'Seal No.',EIROUT.PrincipleCode as Principal,EIROUT.Remark as 'Remarks' 
From EIROUT 
Left Join ContainerDetails on ContainerDetails.ContNo = EIROUT.ContNo 
Left Join Booking On Booking.Nomor = EIROUT.BookingNo 
Left Join EIRIN on EIRIN.Nomor = EIROUT.EIRIN 
Left Join Interchange on Interchange.Nomor = EIRIN.IntNo 
where EIROUT.PrincipleCode = '"""+Principle_Code+"""' 
AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""' 
group by EIROUT.ContNo,BookingNo order by EIROUT.DateOut"""

sql_mov_out_summary = """
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)
+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
Left Join EIRIN on EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'GP' 
AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' 
AND EIROUT.DateOut <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)
+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'HC' 
AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' 
AND EIROUT.DateOut <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)
+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'OT' AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'FR' AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'RF' AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'TK' AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'GP' AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'HC' AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'OT' AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'FR' AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'RF' AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'RH' AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIROUT.contCondition LIKE 'AV%' THEN 1 END)+COUNT(CASE WHEN EIROUT.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIROUT 
left Join EIRIN On EIRIN.Nomor = EIROut.EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIROUT.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'HT' AND EIROUT.PrincipleCode = '"""+Principle_Code+"""' AND EIROUT.DateOut >= '"""+time_from+"""' AND EIROUT.DateOut <= '"""+time_now+"""' 
"""