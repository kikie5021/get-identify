# -*- coding: utf-8 -*-

from datetime import datetime
from app import constants as C
from app import db


class Strain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.SmallInteger)
    test_result = db.Column(db.String)

    def __repr__(self):
        return self.name

    @classmethod
    def exists(cls, name):
        name = name.strip()
        r = cls.query.filter_by(name=name).count() > 0
        return r

    def get_category(self):
        return C.CATEGORY[self.category]


class TestFood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return self.name

    @classmethod
    def exists(cls, name):
        name = name.strip().upper()
        r = cls.query.filter_by(name=name).count() > 0
        return r


class SampleFood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    test_result = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    deleted_at = db.Column(db.DateTime, default=None)

    def __repr__(self):
        return self.name

    def approximate_to(self):
        strains = Strain.query
        num_test_food = TestFood.query.count()
        results = []
        for strain in strains:
            s1 = strain.test_result
            s2 = self.test_result
            diffs = [i for i in range(min(num_test_food, len(s1), len(s2))) if s1[i] != s2[i]]
            percentage = (num_test_food - len(diffs)) / num_test_food
            if percentage > 0.5:
                results.append({
                    'strain': strain,
                    'diffs': diffs,
                    'percentage': percentage,
                    })
        return results
