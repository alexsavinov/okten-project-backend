import os
from uuid import uuid1


class SchoolUtils:
    @staticmethod
    def upload_to(instance, file: str):
        ext = file.split('.')[-1]
        # return os.path.join(instance.user.email, 'schools', f'{uuid1()}.{ext}')
        return os.path.join('schools', f'{uuid1()}.{ext}')
