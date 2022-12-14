import pytest
from tomato_cooker.grill import GrillTomatoCooker
from tomato_cooker.models import TomaticProblem, tomatic


@pytest.fixture
def graellador_path():
    return tomatic.MODEL_DEFINITION_PATH


@pytest.fixture
def solvers():
    return ["chuffed", "coin-bc"]


@pytest.fixture
def tomato_cooker(graellador_path, solvers):
    return GrillTomatoCooker(graellador_path, solvers)


@pytest.fixture
def tomatic_instance():
    return TomaticProblem(
        nPersones=32,
        nLinies=8,
        nSlots=4,
        nNingus=2,
        nDies=5,
        maxTorns=6,
        nTorns=[
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
            9,
        ],
        indisponibilitats=[
            [{1}, {1}, {1}, {1}, {1}],
            [{2}, {2}, {2}, {2}, {2}],
            [{3}, {3}, {3}, {3}, {3}],
            [{4}, {4}, {4}, {4}, {4}],
            [{1}, {2}, {3}, {4}, {1}],
            [{2}, {3}, {4}, {1}, {2}],
            [{3}, {4}, {1}, {2}, {3}],
            [{4}, {1}, {2}, {3}, {4}],
            [{4}, {3}, {2}, {1}, {4}],
            [{2}, {1}, {3}, {4}, {2}],
            [{1}, {2}, {3}, {4}, {1}],
            [{2}, {3}, {4}, {1}, {2}],
            [{3}, {4}, {1}, {2}, {3}],
            [{4}, {1}, {2}, {3}, {4}],
            [{4}, {3}, {2}, {1}, {4}],
            [{2}, {1}, {3}, {4}, {2}],
            [{1}, {1}, {1}, {1}, {1}],
            [{2}, {2}, {2}, {2}, {2}],
            [{3}, {3}, {3}, {3}, {3}],
            [{4}, {4}, {4}, {4}, {4}],
            [{1}, {2}, {3}, {4}, {1}],
            [{2}, {3}, {4}, {1}, {2}],
            [{3}, {4}, {1}, {2}, {3}],
            [{4}, {1}, {2}, {3}, {4}],
            [{4}, {3}, {2}, {1}, {4}],
            [{2}, {1}, {3}, {4}, {2}],
            [{1}, {2}, {3}, {4}, {1}],
            [{2}, {3}, {4}, {1}, {2}],
            [{3}, {4}, {1}, {2}, {3}],
            [{4}, {1}, {2}, {3}, {4}],
            [{4}, {3}, {2}, {1}, {4}],
            [{2}, {1}, {3}, {4}, {2}],
        ],
    )
