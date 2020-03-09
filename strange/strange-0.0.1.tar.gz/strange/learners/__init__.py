from strange.learners._ar import AR
from strange.learners._black_box import BlackBox
from strange.learners._black_box import blackbox
from strange.learners._black_box import DifferentiableBlackBox
from strange.learners._boosted import boost
from strange.learners._boosted import Boosted
from strange.learners._predict_constant import PredictConstant
from strange.learners._predict_last import PredictLast

__all__ = [
    "AR",
    "BlackBox",
    "Boosted",
    "boost",
    "DifferentiableBlackBox",
    "blackbox",
    "PredictConstant",
    "PredictLast",
]
