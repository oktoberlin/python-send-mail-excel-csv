from sources.time import time_yesterday, time_now

time_from = time_yesterday                                  

#if f'{time_now_email_subject} 16:00:01' <= time_now <= f'{time_now_email_subject} 00:00:01':
#  time_from = time_yesterday
print("Enjoy your life...")
print(f'{time_from}-{time_now}')

Principle_Code = 'MSC'

sql1 = """
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

sql2 = """Select 
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

sql2_summary = """
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

sql3 = """Select EIRIN.ContNo,ContainerDetails.size,ContainerDetails.type,contCondition,
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

sql3_summary = """
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

sql4 = """Select EIROUT.ContNo as 'Container No',ContainerDetails.Size,ContainerDetails.Type,
EIRIN.DateIn as 'Date In',LEFT(ContainerDetails.Payload,5),ContainerDetails.Net as 'Tare',ContainerDetails.Datemnf as 'DMF',
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

sql4_summary = """
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

sql5 = """Select 
ContainerStock.ContNo as 'Container No',ContainerDetails.Size as 'Size',ContainerDetails.Type as 'Type',
ContainerStock.ContCondition as 'Condition',LEFT(ContainerDetails.Payload,5) as 'Payload',
If(ContainerDetails.Net=0,Null,Net) as 'Tare',If(length(ContainerDetails.Datemnf) < 3,' ',
ContainerDetails.Datemnf) as 'Date Mnf',Concat(Interchange.Exvessel,'-',Interchange.ExVoy) as 'Ex Vessel Voy',
UPPER(Interchange.Consignee) as 'Customer',EIRIN.DateIn as 'Date IN',ContainerStock.PrincipleCode as Principle,
BlockContainer.Remark as 'Remarks IN',EIRIN.Grade as Grade,EIRIN.IntNo as 'B/L NO' 
From ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join BlockContainer On BlockContainer.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
left Join Interchange On Interchange.Nomor = ContainerStock.IntNo 
left Join InterchangeContainer On InterchangeContainer.Nomor = ContainerStock.IntNo AND 
InterchangeContainer.ContNo = ContainerStock.ContNo 
left Join interchangeDocpaycontainer on InterchangeDocpaycontainer.ContNo = ContainerStock.ContNo 
AND InterchangeDocpaycontainer.IntNo = ContainerStock.IntNo 
left Join interchangeDocpaydetails on InterchangeDocpaydetails.Nomor = InterchangeDocpaycontainer.Nomor 
AND InterchangeDocpaydetails.Size = ContainerDetails.Size 
where ContainerStock.PrincipleCode = '"""+Principle_Code+"""' AND ContainerStock.ContCondition = 'DMG' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
GROUP BY ContainerStock.ContNo order by EIRIN.DateIn"""

sql5_summary = """
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'GP' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'HC' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'OT' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'FR' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'RF' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '20' AND ContainerDetails.type = 'TK' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'GP' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'HC' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'OT' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'   
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'FR' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'RF' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'RH' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
where ContainerDetails.size = '40' AND ContainerDetails.type = 'HT' AND ContainerStock.ContCondition = 'DMG' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
"""

sql6 = """Select 
ContainerStock.ContNo as 'Container No',ContainerDetails.Size as 'Size',ContainerDetails.Type as 'Type',
ContainerStock.ContCondition as 'Condition',LEFT(ContainerDetails.Payload,5) as 'Payload',
If(ContainerDetails.Net=0,Null,Net) as 'Tare',If(length(ContainerDetails.Datemnf) < 3,' ',
ContainerDetails.Datemnf) as 'Date Mnf',Concat(Interchange.Exvessel,'-',Interchange.ExVoy) as 'Ex Vessel Voy',
UPPER(Interchange.Consignee) as 'Customer',EIRIN.DateIn as 'Date IN',
RepairContainer.CompleteRepair as 'Completed Repair',ContainerStock.PrincipleCode as Principle,
RepairContainer.Repaired,BlockContainer.Remark as 'Remarks IN',EIRIN.Grade as Grade,EIRIN.IntNo as 'B/L NO' 
From ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join BlockContainer On BlockContainer.ContNo = ContainerStock.ContNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
left Join Interchange On Interchange.Nomor = ContainerStock.IntNo 
left Join InterchangeContainer On InterchangeContainer.Nomor = ContainerStock.IntNo AND 
InterchangeContainer.ContNo = ContainerStock.ContNo 
left Join interchangeDocpaycontainer on InterchangeDocpaycontainer.ContNo = ContainerStock.ContNo 
AND InterchangeDocpaycontainer.IntNo = ContainerStock.IntNo 
left Join interchangeDocpaydetails on InterchangeDocpaydetails.Nomor = InterchangeDocpaycontainer.Nomor 
AND InterchangeDocpaydetails.Size = ContainerDetails.Size 
where ContainerStock.PrincipleCode = '"""+Principle_Code+"""' AND RepairContainer.Repaired = 'Yes' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
GROUP BY ContainerStock.ContNo order by EIRIN.DateIn"""

sql6_summary = """
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '20' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'GP' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '20' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'HC' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '20' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'OT' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '20' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'FR' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '20' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'RF' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '20' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'TK' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '40' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'GP' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '40' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'HC' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '40' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'OT' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'   
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '40' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'FR' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '40' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'RF' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '40' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'RH' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
UNION ALL 
SELECT 
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' THEN 1 END) AS AV,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS DMG,
COUNT(CASE WHEN ContainerStock.ContCondition LIKE 'AV%' OR ContainerStock.ContCondition LIKE 'DM%' THEN 1 END) AS TOTAL 
FROM ContainerStock 
    Left join ContainerDetails On ContainerDetails.ContNo = ContainerStock.ContNo 
Left Join EIRIN On EIRIN.Nomor = ContainerStock.EIRNo 
Left Join RepairContainer On RepairContainer.EORNo = ContainerStock.EORNo 
where ContainerDetails.size = '40' AND RepairContainer.Repaired = 'Yes' AND ContainerDetails.type = 'HT' 
AND ContainerStock.PrincipleCode = '"""+Principle_Code+"""' 
AND EIRIN.DateIn >= (SELECT MIN(EIRIN.DateIn) FROM EIRIN) AND EIRIN.DateIn <= '"""+time_now+"""'  
"""
