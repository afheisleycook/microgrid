import sqlite3
from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class EnergyModel(object):
    name: str
    peak_usage = Decimal
    power_average = Decimal
    power_under = Decimal

    @property
    def __str__(self):
        return f" name {self.name} peak{self.peak_usage} average:{self.power_average} power_under: {self.power_under}"


def main():
    app = sqlite3.connect("../app.db")
    conn = app.cursor()
    with open("setup.sql", "r+") as t:
        lines = t.readlines()
        for line in lines:
            print(conn.execute(line).fetchall())
    app.commit()

main()