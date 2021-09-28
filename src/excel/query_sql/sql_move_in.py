from src.excel.excel_format import *

sql_mov_in = """Select EIRIN.ContNo,ContainerDetails.size,ContainerDetails.type,LEFT(contCondition,2),
cleaningtype.Name,LEFT(ContainerDetails.Payload,5),If(Net=0,Null,Net),If(length(Datemnf) < 3,' ',Datemnf),EIRIN.DATEOUTPORT,
EIRIN.DateIn,Concat(Exvessel,'-',ExVoy),UPPER(interchange.Consignee),
EIRIN.VN,EIRIN.IntNo,EIRIN.PrincipleCode,EIRIN.Grade,EIRIN.Remark 
From EIRIN 
left Join cleaningtype On cleaningtype.PrincipleCode = EIRIN.PrincipleCode 
left Join Interchange On Interchange.Nomor = EIRIN.IntNo 
left Join InterchangeContainer On InterchangeContainer.Nomor = EIRIN.IntNo AND 
InterchangeContainer.ContNo = EIRIN.ContNo 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
left Join interchangeDocpaycontainer on InterchangeDocpaycontainer.contno = eirin.contno 
AND InterchangeDocpaycontainer.intno=EIRIN.intNo 
left Join interchangeDocpaydetails on InterchangeDocpaydetails.nomor = InterchangeDocpaycontainer.nomor 
AND InterchangeDocpaydetails.Size = ContainerDetails.Size 
where EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
GROUP BY EIRIN.NOMOR order by EIRIN.DateIn"""

sql_mov_in_summary = """
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'GP' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'HC' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'OT' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'FR' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'RF' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'TK' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'GP' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'HC' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'OT' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'FR' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'RF' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'RH' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
UNION ALL 
SELECT 
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN EIRIN.contCondition LIKE 'AV%' OR EIRIN.contCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM EIRIN 
Left join ContainerDetails On ContainerDetails.ContNo = EIRIN.ContNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'HT' 
AND EIRIN.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= '"""+time_from+"""' AND EIRIN.DateIn <= '"""+time_now+"""' 
"""