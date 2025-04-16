import uuid

# Base entity

class Base:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

# Animal sort
class Animal_Sort(Base):
    _id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sort_name = CharField(max_length=30)

#Type of sickness
class Diagnosis_Type(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sort_name = models.CharField(max_length=30)
    description = models.TextField()

# Treatment
class Treatment(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #animal_id = models.ForeignKey()
    #diagnosis_id = models.ForeignKey()
    date_time = models.DateTimeField()
    realised_id = models.BooleanField()
    description = models.TextField()

# Medicals
class Medicals(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_time = models.DateTimeField()
    treatment_medicals = models.ManyToManyField(Treatment, "treatments_medicals")
    description = models.TextField()

# Diagnosis
class Diagnosis(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #animal_id = models.ForeignKey()
    date_time = models.DateTimeField()
    cured = models.BooleanField(False)
    #animal_diagnosis_id = models.ManyToManyField()
    treatments = models.ForeignKey(Treatment, related_name="diagnoses", on_delete=models.CASCADE)
    type = models.ForeignKey(Diagnosis_Type, related_name="type", on_delete=models.CASCADE)

# Animal
class Animal(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    animal_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    patient_number = models.CharField(max_length=100)
    sterilised = models.BooleanField(False)
    animal_sort_id = models.ForeignKey(Animal_Sort, related_name="sort", on_delete=models.CASCADE)
    diagnoses = models.ForeignKey(Diagnosis, related_name="diagnoses", on_delete=models.CASCADE)