from ase.cell import Cell


cell = Cell.fromcellpar([4, 4, 4, 90,90,90])
bandpath = cell.bandpath()
print(bandpath)