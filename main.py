import itertools

def getAlRoutes(listOfKnots: list[str])-> list[tuple[str, ...]]:
    """
    各ノットの巡回順を全通り生成する
    """
    return list(itertools.permutations(listOfKnots))

def initMapEdegeToDistance()-> dict[str, dict[str, float]]:
    """
    各エッジの距離を初期化する
    """
    mapEdgeToDistance = {
        "F1": {},
        "a": {},
        "b": {},
        "c":{},
        "d":{}
    }
    mapEdgeToDistance["F1"]["a"] = 11.25
    mapEdgeToDistance["F1"]["b"] = 8.5
    mapEdgeToDistance["F1"]["c"] = 11.00
    mapEdgeToDistance["F1"]["d"] = 12.00

    mapEdgeToDistance["a"]["a"] = float("inf")
    mapEdgeToDistance["a"]["b"] = 4.0
    mapEdgeToDistance["a"]["c"] = 11.00
    mapEdgeToDistance["a"]["d"] = 12.00

    mapEdgeToDistance["b"]["a"] = 4.0
    mapEdgeToDistance["b"]["b"] = float("inf")
    mapEdgeToDistance["b"]["c"] = 9.0
    mapEdgeToDistance["b"]["d"] = 9.5

    mapEdgeToDistance["c"]["a"] = 11.0
    mapEdgeToDistance["c"]["b"] = 9.0
    mapEdgeToDistance["c"]["c"] = float("inf")
    mapEdgeToDistance["c"]["d"] = 4.25

    mapEdgeToDistance["d"]["a"] = 12.00
    mapEdgeToDistance["d"]["b"] = 9.5
    mapEdgeToDistance["d"]["c"] = 4.25
    mapEdgeToDistance["d"]["d"] = float("inf")

    return mapEdgeToDistance


def calcSumDistance(route: tuple[str, ...], mapEdgeToDistance: dict[str, dict[str, float]]) -> float:
    """
    ルートの距離を計算する
    """
    sumDistance = 0.0
    # F1から最初のノットへの距離を加算
    sumDistance += mapEdgeToDistance["F1"][route[0]]
    for i in range(len(route) - 1):
        sumDistance += mapEdgeToDistance[route[i]][route[i + 1]]
    return sumDistance


if __name__ == "__main__":
    mapEdgeToDistance = initMapEdegeToDistance()

    listOfKnots = ["a", "b", "c", "d"]
    listOfRoutes = getAlRoutes(listOfKnots)

    minRoute = None
    distanceOfMinRoute = float("inf")
    for route in listOfRoutes:
        sumDistance = calcSumDistance(route, mapEdgeToDistance)
        if sumDistance < distanceOfMinRoute:
            minRoute = route
            distanceOfMinRoute = sumDistance


    print("Ans is {}".format(minRoute))
