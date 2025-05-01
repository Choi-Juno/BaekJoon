N = int(input())

classroom = {
    "Algorithm": 204,
    "DataAnalysis": 207,
    "ArtificialIntelligence": 302,
    "CyberSecurity": "B101",
    "Network": 303,
    "Startup": 501,
    "TestStrategy": 105,
}

for i in range(N):
    seminar = input()
    print(classroom[seminar])
