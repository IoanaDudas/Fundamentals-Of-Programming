import configparser
from ui import *

class Settings:
    def __init__(self, fileName):
        self._fileName = fileName
        self._inMemory = False

    def start(self):
        with open(self._fileName, "r") as f:
            config_string = "[SETTINGS]\n" + f.read()
        config = configparser.ConfigParser()
        config.read_string(config_string)
        for i in config["SETTINGS"]:
            config["SETTINGS"][i] = config["SETTINGS"][i].strip('"')
        repository = config["SETTINGS"]["repository"]
        gradeRepo = ''
        studentRepo = ''
        disciplineRepo = ''
        undoController = UndoController()

        if repository == "inmemory":
            gradeRepo = IterGradeRepo()
            studentRepo = IterStudentRepo()
            disciplineRepo = IterDisciplineRepo()
            self._inMemory = True
        elif repository == "text-file":
            gradeRepo = RepoGradeT(undoController, config["SETTINGS"]["grades"])
            studentRepo = RepoStudentsT(gradeRepo, undoController, config["SETTINGS"]["students"])
            disciplineRepo = RepoDisciplinesT(gradeRepo, undoController, config["SETTINGS"]["disciplines"])
        elif repository == "binary-file":
            gradeRepo = RepoGradeB(undoController, config["SETTINGS"]["grades"])
            studentRepo = RepoStudentsB(gradeRepo, undoController, config["SETTINGS"]["students"])
            disciplineRepo = RepoDisciplinesB(gradeRepo, undoController, config["SETTINGS"]["disciplines"])

        service = Service(studentRepo, disciplineRepo, gradeRepo, undoController, self._inMemory)
        UI = ui(service)
        UI.menu()


settings = Settings("settings.properties")
settings.start()





