API_KEY='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'
usr="FALP\matias.espinoza"
pwd="8779abc"







query=""" 

select top 50 

convert(date,FECHA_EVOLUCION,103) as FECHA,
FICHA,
RUT,
ELEMENT,
EVOLUCION,
EPISODIO,
SECCION,
NOMBRE_PROFESIONAL

 from dbo.Evoluciones_Timeline


where EPISODIO='Episodio de Hospitalizacion'
and [ELEMENT]='Evolución Médica'
and convert(date,FECHA_EVOLUCION,103)>='2023-01-01'
and SECCION='PALIA_DOLOR' """