from src.excel.excel_format import *

sql_recapAll = """
SELECT * FROM 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '20' 
AND CD.type = 'FR' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'FR'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'FR' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A11 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '40' 
AND CD.type = 'FR' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'FR'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'FR' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A12 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '45' 
AND CD.type = 'FR' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'FR'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'FR' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A13 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'FR' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS B1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'AV%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'FR' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS C1
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'DM%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'FR' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS D1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '40' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '45' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'FR' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS E1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%WW%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'FR' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS F1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%SW%' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'FR' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS G1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
Left Join RepairContainer RC On RC.EORNo = CS.EORNo 
WHERE RC.Repaired = 'Yes' AND CD.type = 'FR' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS H1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM EIROUT EO 
Left Join EIRIN EI ON EI.Nomor = EO.EIRIN 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE CD.type = 'FR' 
AND EO.PrincipleCode = '"""+Principle_Code+"""'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""'
) AS I1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'FR' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS J1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'AV%' THEN 1 END)  
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'FR' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS K1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'DM%' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'FR' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS L1 
UNION ALL 
SELECT * FROM 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '20' 
AND CD.type = 'GP' 
AND CS.PrincipleCode = '"""+Principle_Code+"""') +
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'GP'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""') -
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'GP' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A11 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '40' 
AND CD.type = 'GP' 
AND CS.PrincipleCode = '"""+Principle_Code+"""') +
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'GP'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""') -
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'GP' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A12 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '45' 
AND CD.type = 'GP' 
AND CS.PrincipleCode = '"""+Principle_Code+"""') +
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'GP'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""') -
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'GP' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A13 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'GP' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS B1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'AV%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'GP' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS C1
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'DM%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'GP' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS D1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '40' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '45' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'GP' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS E1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%WW%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'GP' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS F1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%SW%' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'GP' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS G1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
Left Join RepairContainer RC On RC.EORNo = CS.EORNo 
WHERE RC.Repaired = 'Yes' AND CD.type = 'GP' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS H1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM EIROUT EO 
Left Join EIRIN EI ON EI.Nomor = EO.EIRIN 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE CD.type = 'GP' 
AND EO.PrincipleCode = '"""+Principle_Code+"""'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""'
) AS I1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'GP' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS J1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'AV%' THEN 1 END)  
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'GP' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS K1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'DM%' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'GP' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS L1 
UNION ALL 
SELECT * FROM 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '20' 
AND CD.type = 'GOH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'GOH'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'GOH' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A11 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '40' 
AND CD.type = 'GOH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'GOH'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'GOH' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A12 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '45' 
AND CD.type = 'GOH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'GOH'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'GOH' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A13 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'GOH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS B1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'AV%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'GOH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS C1
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'DM%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'GOH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS D1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '40' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '45' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'GOH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS E1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%WW%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'GOH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS F1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%SW%' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'GOH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS G1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
Left Join RepairContainer RC On RC.EORNo = CS.EORNo 
WHERE RC.Repaired = 'Yes' AND CD.type = 'GOH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS H1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM EIROUT EO 
Left Join EIRIN EI ON EI.Nomor = EO.EIRIN 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE CD.type = 'GOH' 
AND EO.PrincipleCode = '"""+Principle_Code+"""'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""'
) AS I1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'GOH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS J1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'AV%' THEN 1 END)  
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'GOH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS K1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'DM%' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'GOH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS L1 
UNION ALL 
SELECT * FROM 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '20' 
AND CD.type = 'HC' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'HC'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'HC' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A11 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '40' 
AND CD.type = 'HC' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'HC'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'HC' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A12 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '45' 
AND CD.type = 'HC' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'HC'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'HC' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A13 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'HC' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS B1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'AV%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'HC' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS C1
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'DM%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'HC' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS D1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '40' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '45' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'HC' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS E1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%WW%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'HC' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS F1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%SW%' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'HC' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS G1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
Left Join RepairContainer RC On RC.EORNo = CS.EORNo 
WHERE RC.Repaired = 'Yes' AND CD.type = 'HC' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS H1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM EIROUT EO 
Left Join EIRIN EI ON EI.Nomor = EO.EIRIN 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE CD.type = 'HC' 
AND EO.PrincipleCode = '"""+Principle_Code+"""'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""'
) AS I1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'HC' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS J1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'AV%' THEN 1 END)  
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'HC' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS K1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'DM%' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'HC' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS L1 
UNION ALL 
SELECT * FROM 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '20' 
AND CD.type = 'OT' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'OT'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'OT' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A11 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '40' 
AND CD.type = 'OT' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'OT'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'OT' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A12 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '45' 
AND CD.type = 'OT' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'OT'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'OT' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A13 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'OT' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS B1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'AV%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'OT' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS C1
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'DM%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'OT' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS D1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '40' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '45' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'OT' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS E1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%WW%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'OT' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS F1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%SW%' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'OT' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS G1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
Left Join RepairContainer RC On RC.EORNo = CS.EORNo 
WHERE RC.Repaired = 'Yes' AND CD.type = 'OT' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS H1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM EIROUT EO 
Left Join EIRIN EI ON EI.Nomor = EO.EIRIN 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE CD.type = 'OT' 
AND EO.PrincipleCode = '"""+Principle_Code+"""'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""'
) AS I1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'OT' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS J1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'AV%' THEN 1 END)  
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'OT' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS K1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'DM%' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'OT' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS L1 
UNION ALL 
SELECT * FROM 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '20' 
AND CD.type = 'RF' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'RF'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'RF' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A11 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '40' 
AND CD.type = 'RF' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'RF'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'RF' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A12 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '45' 
AND CD.type = 'RF' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'RF'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'RF' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A13 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'RF' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS B1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'AV%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'RF' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS C1
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'DM%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'RF' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS D1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '40' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '45' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'RF' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS E1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%WW%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'RF' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS F1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%SW%' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'RF' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS G1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
Left Join RepairContainer RC On RC.EORNo = CS.EORNo 
WHERE RC.Repaired = 'Yes' AND CD.type = 'RF' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS H1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM EIROUT EO 
Left Join EIRIN EI ON EI.Nomor = EO.EIRIN 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE CD.type = 'RF' 
AND EO.PrincipleCode = '"""+Principle_Code+"""'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""'
) AS I1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'RF' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS J1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'AV%' THEN 1 END)  
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'RF' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS K1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'DM%' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'RF' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS L1 
UNION ALL 
SELECT * FROM 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '20' 
AND CD.type = 'RH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'RH'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '20' 
AND CD.type = 'RH' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A11 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '40' 
AND CD.type = 'RH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'RH'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '40' 
AND CD.type = 'RH' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A12 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' AND CD.size = '45' 
AND CD.type = 'RH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'RH'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' AND CD.size = '45' 
AND CD.type = 'RH' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A13 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'RH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS B1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'AV%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'RH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS C1
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'DM%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE CD.type = 'RH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS D1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '40' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '45' 
AND IC.CleaningType IN ('%DW%','%CW%') THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'RH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS E1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%WW%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'RH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS F1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%SW%' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE CD.type = 'RH' 
AND EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS G1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
Left Join RepairContainer RC On RC.EORNo = CS.EORNo 
WHERE RC.Repaired = 'Yes' AND CD.type = 'RH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS H1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM EIROUT EO 
Left Join EIRIN EI ON EI.Nomor = EO.EIRIN 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE CD.type = 'RH' 
AND EO.PrincipleCode = '"""+Principle_Code+"""'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""'
) AS I1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'RH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS J1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'AV%' THEN 1 END)  
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'RH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS K1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'DM%' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CD.type = 'RH' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS L1 
UNION ALL 
SELECT * FROM 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' 
AND CD.size = '20' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' 
AND CD.size = '20' 
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' 
AND CD.size = '20' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""')
) AS A11 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' 
AND CD.size = '40' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' 
AND CD.size = '40' 
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' 
AND CD.size = '40' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""') 
) AS A12 
join 
(SELECT 
(SELECT COUNT(*) FROM ContainerStock CS 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
left join ContainerDetails CD On CD.ContNo = CS.ContNo 
where  EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""' 
AND CD.size = '45' 
AND CS.PrincipleCode = '"""+Principle_Code+"""')+
(SELECT COUNT(*) FROM EIROUT EO 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""' 
AND CD.size = '45' 
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""')-
(SELECT COUNT(*) FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""' 
AND CD.size = '45' 
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""') 
) AS A13 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS B1
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'AV%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS C1
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND EI.contCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND EI.contCondition LIKE 'DM%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS D1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' 
AND (IC.CleaningType LIKE '%DW%' OR IC.CleaningType LIKE '%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '40' 
AND (IC.CleaningType LIKE '%DW%' OR IC.CleaningType LIKE '%CW%') THEN 1 END),
COUNT(CASE WHEN CD.size = '45' 
AND (IC.CleaningType LIKE '%DW%' OR IC.CleaningType LIKE '%CW%') THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS E1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%WW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%WW%' THEN 1 END)
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS F1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND IC.CleaningType LIKE '%SW%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND IC.CleaningType LIKE '%SW%' THEN 1 END) 
FROM EIRIN EI 
Left join ContainerDetails CD On CD.ContNo = EI.ContNo 
left Join InterchangeContainer IC On IC.Nomor = EI.IntNo 
AND IC.ContNo = EI.ContNo 
WHERE EI.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= '"""+time_from+"""' 
AND EI.DateIn <= '"""+time_now+"""'
) AS G1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM ContainerStock CS
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
Left Join RepairContainer RC On RC.EORNo = CS.EORNo 
WHERE RC.Repaired = 'Yes' 
AND CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS H1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM EIROUT EO 
Left Join EIRIN EI on EI.Nomor = EO.EIRIN 
Left join ContainerDetails CD On CD.ContNo = EO.ContNo 
WHERE EO.PrincipleCode = '"""+Principle_Code+"""'
AND EO.DateOut >= '"""+time_from+"""' 
AND EO.DateOut <= '"""+time_now+"""'
) AS I1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' THEN 1 END)
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS J1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'AV%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'AV%' THEN 1 END)  
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS K1 
JOIN 
(SELECT 
COUNT(CASE WHEN CD.size = '20' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '40' AND CS.ContCondition LIKE 'DM%' THEN 1 END),
COUNT(CASE WHEN CD.size = '45' AND CS.ContCondition LIKE 'DM%' THEN 1 END) 
FROM ContainerStock CS 
Left join ContainerDetails CD On CD.ContNo = CS.ContNo 
Left Join EIRIN EI On EI.Nomor = CS.EIRNo 
WHERE CS.PrincipleCode = '"""+Principle_Code+"""'
AND EI.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) 
AND EI.DateIn <= '"""+time_now+"""'
) AS L1
"""