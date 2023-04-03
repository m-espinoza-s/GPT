API_KEY="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"
usr="FALP\matias.espinoza"
pwd="8779abc"







query=""" 

select top 10 

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