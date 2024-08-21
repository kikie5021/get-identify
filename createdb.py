# -*- coding: utf-8 -*-

from app.models import Strain, TestFood, SampleFood
from app import constants as C
from app import db

db.create_all()

pathogenic_strains = [
    Strain(name='Escherichia coli O157:H7', category=C.PATHOGENIC, test_result='--+-++-++--+++++++---+++'),
    Strain(name='Listeria monocytogenes', category=C.PATHOGENIC, test_result='++-+++++--++-++++-++++++'),
    Strain(name='Salmonella Choleraesuis', category=C.PATHOGENIC, test_result='--+-+--++---++++++--+--+'),
    Strain(name='Salmonella Enteritidis', category=C.PATHOGENIC, test_result='--+++----++++-+--++--+--'),
    Strain(name='Salmonella Typhi', category=C.PATHOGENIC, test_result='----+--++---+++++-+-+-++'),
    Strain(name='Salmonella Typhimurium', category=C.PATHOGENIC, test_result='--+-++-+++--++++++--+-++'),
    Strain(name='Staphylococcus aureus', category=C.PATHOGENIC, test_result='--+-+--++--+-+-++----++-'),
    Strain(name='Yersinia enterocolitica', category=C.PATHOGENIC, test_result='++-+++-++-++--++++-+++++'),
    ]

non_pathogenic_strains = [
    Strain(name='Bacillus cereus', category=C.NON_PATHOGENIC, test_result='----+-+++--+-+----+++++-'),
    Strain(name='Citrobacter freundii', category=C.NON_PATHOGENIC, test_result='--+-+--+++-+-+-++-+-+-+-'),
    Strain(name='Enterococcus faecalis', category=C.NON_PATHOGENIC, test_result='++-++++++-++-++++-++++++'),
    Strain(name='Klebsiella pneumoniae', category=C.NON_PATHOGENIC, test_result='--+---+---+++-+--++--+--'),
    Strain(name='Listeria innocua', category=C.NON_PATHOGENIC, test_result='++--+-+++--+-+--+-++++++'),
    Strain(name='Proteus mirabilis', category=C.NON_PATHOGENIC, test_result='--+---+--+-------+------'),
    Strain(name='Pseudomonas aeruginosa', category=C.NON_PATHOGENIC, test_result='--+---------+----+------'),
    Strain(name='Serratia marcescens', category=C.NON_PATHOGENIC, test_result='--+---+-----+----+------'),
    Strain(name='Shigella dysentheriae', category=C.NON_PATHOGENIC, test_result='----++-++----++++++-+-+-'),
    ]

test_foods = [
    TestFood(name='ADO'),
    TestFood(name='ARG'),
    TestFood(name='ARA'),
    TestFood(name='CEL'),
    TestFood(name='DEX'),
    TestFood(name='DUC'),
    TestFood(name='ESC'),
    TestFood(name='FRU'),
    TestFood(name='GAL'),
    TestFood(name='HYS'),
    TestFood(name='INO'),
    TestFood(name='LAC'),
    TestFood(name='LYS'),
    TestFood(name='MAL'),
    TestFood(name='MEL'),
    TestFood(name='MANI'),
    TestFood(name='MANO'),
    TestFood(name='ORN'),
    TestFood(name='RHA'),
    TestFood(name='SAL'),
    TestFood(name='SOR'),
    TestFood(name='SUC'),
    TestFood(name='TRE'),
    TestFood(name='XYL'),
    ]

db.session.add_all(pathogenic_strains + non_pathogenic_strains + test_foods)
db.session.commit()
