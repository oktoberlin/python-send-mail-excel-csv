from src.excel.excel_format import *

sql_stockList = """Select 
CS.ContNo as 'Container No',
CD.Size as 'Size',
CD.Type as 'Type',
LEFT(CS.ContCondition,2) as 'Condition',
LEFT(CD.Payload,5) as 'Payload',
If(CD.Net=0,Null,Net) as 'Tare',
If(length(CD.Datemnf) < 3,' ',CD.Datemnf) as 'Date Mnf',
Concat(I.Exvessel,'-',I.ExVoy) as 'Ex Vessel Voy',
UPPER(I.Consignee) as 'Customer',
EI.DateIn as 'Date IN',
CS.PrincipleCode as Principle,
BC.Remark as 'Remarks IN',
EI.Grade as Grade,
EI.IntNo as 'B/L NO' 
From ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join BlockContainer BC On BC.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left Join Interchange I On I.Nomor = CS.IntNo 
left Join InterchangeContainer IC On IC.Nomor = CS.IntNo AND IC.ContNo = CS.ContNo 
left Join interchangeDocpaycontainer IDC on IDC.ContNo = CS.ContNo AND IDC.IntNo = CS.IntNo 
left Join interchangeDocpaydetails IDD on IDD.Nomor = IDC.Nomor AND IDD.Size = CD.Size 
where CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
GROUP BY CS.ContNo order by EI.DateIn"""

sql_stockList_summary = """
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '20' 
AND CD.type = 'GP' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '20' 
AND CD.type = 'HC' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '20' AND CD.type = 'OT' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '20' AND CD.type = 'FR' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '20' 
AND CD.type = 'RF' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '20' 
AND CD.type = 'TK' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '40' 
AND CD.type = 'GP' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '40' 
AND CD.type = 'HC' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '40' 
AND CD.type = 'OT' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'   
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '40' 
AND CD.type = 'FR' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '40' 
AND CD.type = 'RF' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '40' 
AND CD.type = 'RH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN CS.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN CS.ContCondition LIKE 'AV%' 
OR CS.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
where CD.size = '40' 
AND CD.type = 'HT' 
AND CS.PrincipleCode = '"""+Principle_Code+"""' 
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'  
"""