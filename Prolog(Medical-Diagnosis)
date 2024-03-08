symptom(fever).
symptom(cough).
symptom(headache).
symptom(runny_nose).
symptom(sore_throat).

disease(flu, [fever, cough, headache]).
disease(cold, [cough, runny_nose, sore_throat]).

diagnose(Disease) :-
  disease(Disease, Symptoms),
  findall(Symptom, (symptom(Symptom), member(Symptom, Symptoms)), PatientSymptoms),
  length(PatientSymptoms, SymptomCount),
  SymptomCount >= 2.
