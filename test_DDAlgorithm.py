from DDAlgorithm import dd_algorithm, set_seed
from DDAlgorithmSlow import dd_algorithm_slow, set_seed_slow
import random


import random


class Test:
    # Values of Theta used
    # 0.13436424411240122
    # 0.9560342718892494
    # 0.23796462709189137
    # 0.23604808973743452
    # 0.6229016948897019
    # 0.793340083761663
    # 0.32383276483316237
    # 0.2267058593810488
    # 0.46300735781502145
    # 0.5714025946899135
    # 0.4523795535098186
    # 0.4745706786885481
    # 0.2590084917154736
    # 0.10682853770165568
    # 0.965242141552123
    # 0.36152277491407514
    # 0.5219839097124932
    # 0.18126486333322134
    # 0.6771258268002703
    # 0.9056396761745207
    # 0.16494947983319797
    # 0.9582093798172728
    # 0.9248652516259452
    # 0.7123429878269185
    # 0.376962302390386
    # 0.7472912662232836
    # 0.6484972199788831
    # 0.11295717017616302
    # 0.5481190538116991
    # 0.5390815646058106
    # 0.01227824739797545
    # 0.07742178385330412
    # 0.5703284231368732
    # 0.5289353829404123
    # 0.5486946056438222
    # 0.32870052053309795
    # 0.6820045605879779
    # 0.6394736947203203
    # 0.20985124453651727
    # 0.4586067093870614
    # 0.38102068999577143
    # 0.6394267984578837
    # 0.038551839337380045
    # 0.40853587925449375
    # 0.2718754143840908
    # 0.8882680764524881
    # 0.35184625582788265
    # 0.5481578284163297
    # 0.06688397634275167

    def test_dd_algorithm_correctness(self):
        # Test the algorithm against a verified, slower implementation
        for i in range(1, 50):
            random.seed(i)
            theta = random.random()
            set_seed(i)
            dd_algorithm_result = dd_algorithm(40*i, theta, 30*i)
            set_seed(i)
            dd_algorithm_slow_result = dd_algorithm_slow(40*i, theta, 30*i, False)
            assert (dd_algorithm_result == dd_algorithm_slow_result)
        assert True

    def test_dd_algorithm_performance(self):
        # Test the algorithm performance with a large dataset
        dd_algorithm(4000000, 0.7, 1000000)
