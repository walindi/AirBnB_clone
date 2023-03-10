# create a dictionary representation
d = {
    '__class__': 'BaseModel',
    'id': '123',
    'created_at': '2022-03-09T14:30:00.000000',
    'updated_at': '2022-03-09T14:30:00.000000',
    'name': 'John Doe'
}

# recreate the instance
b = BaseModel(**d)

# verify that the instance was created correctly
assert b.__class__.__name__ == 'BaseModel'
assert b.id == '123'
assert b.created_at == datetime(2022, 3, 9, 14, 30)
assert b.updated_at == datetime(2022, 3, 9, 14, 30)
assert b.name == 'John Doe'

