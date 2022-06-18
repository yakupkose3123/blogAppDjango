import uuid
#! Random ıd üretme kütüphanesi
def get_random_code():
    code = str(uuid.uuid4())[:11].replace("-","") # integer olarak dönüyor o yüzden str ye çevirdik. Bu uzun bir id, ben ilk 11 karakteri al aradaki - leri kaldır dedik.
    return code
