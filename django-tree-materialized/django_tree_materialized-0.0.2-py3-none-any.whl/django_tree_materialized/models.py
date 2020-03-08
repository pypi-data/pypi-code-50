from django.conf import settings
from django.db import models, transaction
from django.db.models import Q

from . import exceptions


class MPTree(models.Model):
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)
    level = models.IntegerField(null=True)
    path = models.CharField(null=True, max_length=1024)

    @classmethod
    def number_to_str(cls, num):
        mp_tree_steplen = getattr(settings, 'MPTREE_STEPLEN', 6)
        chars = "0123456789abcdefghijklmnopqrstuvwxyz"

        s = ""
        while num:
            s = chars[num % len(chars)] + s
            num //= len(chars)

        return str(s).rjust(mp_tree_steplen, '0')

    @classmethod
    def str_to_number(cls, num_str):
        chars = "0123456789abcdefghijklmnopqrstuvwxyz"
        num = 0
        for i, c in enumerate(reversed(num_str)):
            num += chars.index(c) * (len(chars) ** i)
        return num

    # Create node
    @classmethod
    def create(cls, parent=None, **kwargs):

        obj = cls.objects.create(**kwargs)
        obj.level = 1

        if parent:
            obj.parent = parent
            obj.level = parent.level + 1
            obj.path = obj.parent.path + cls.number_to_str(obj.id)
        else:
            obj.path = cls.number_to_str(obj.id)

        obj.save()
        return obj

    @classmethod
    def delete(cls, obj: int) -> None:
        cls.objects.filter(id=obj).delete()

    def get_family(self, include_self: bool = True) -> models.QuerySet:
        """
            Getting a family list
        """
        mp_tree_steplen = getattr(settings, 'MPTREE_STEPLEN', 6)

        sql = []
        for item in [self.path[i:i + mp_tree_steplen] for i in range(0, len(self.path), mp_tree_steplen)]:
            id_obj = int(item)
            if include_self:
                sql.append(id_obj)
            else:
                if id_obj != self.id:
                    sql.append(id_obj)

        return self.__class__.objects.filter(id__in=sql)

    def get_children(self, include_self: bool = True):
        if include_self:
            return self.__class__.objects.filter(path__startswith=self.path)
        else:
            return self.__class__.objects.filter(~Q(id=self.id), Q(path__startswith=self.path))

    def get_parent(self):
        """
            Getting a parent
        """
        return self.parent

    def get_root(self):
        """
            Getting root object
        """
        mp_tree_steplen = getattr(settings, 'MPTREE_STEPLEN', 6)

        sql = []
        for item in [self.path[i:i + mp_tree_steplen] for i in range(0, len(self.path), mp_tree_steplen)]:
            sql.append(int(item))

        return self.__class__.objects.filter(id__in=sql, level=1)[:1].get()

    def move(self, obj):
        mp_tree_steplen = getattr(settings, 'MPTREE_STEPLEN', 6)

        for item in self.get_children():
            if obj.id == item.id:
                raise exceptions.InvalidMove("Unable to transfer object")

        with transaction.atomic():
            for item in self.get_children(include_self=False):
                item.path = obj.path + item.path

                level = [item.path[i:i + mp_tree_steplen] for i in range(0, len(item.path), mp_tree_steplen)]
                item.level = len(level)
                item.save()

            self.parent_id = obj.id
            self.path = obj.path + self.path

            level = [self.path[i:i + mp_tree_steplen] for i in range(0, len(self.path), mp_tree_steplen)]
            self.level = len(level)

            self.save()

        return obj
