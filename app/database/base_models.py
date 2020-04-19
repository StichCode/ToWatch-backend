from psycopg2._psycopg import IntegrityError

from app.database.base_func import add_instance, edit_instance, delete_instance


class BaseModel(object):

    @classmethod
    def all_to_dict(cls):
        return [r.to_dict() for r in cls.query.all()]

    @classmethod
    def delete_by_id(cls, id):
        e = cls._exist(id)
        print(e)
        if not e:
            return False
        delete_instance(cls, id)

    def to_dict(self):
        data = {}
        for attribute, column in self.__mapper__.c.items():
            data[column.key] = getattr(self, attribute)
        return data

    @classmethod
    def from_dict(cls, data: dict, edit=False):
        result = {}
        keys = [column.key for _, column in cls.__mapper__.c.items()]
        for field in keys:
            if field == "id":
                continue
            elif field in data:
                result[field] = data[field]
        try:
            if not edit:
                add_instance(cls, **result)
            else:
                edit_instance(cls, data["id"], result)
        except IntegrityError:
            return False
        return True