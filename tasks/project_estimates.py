# https://bohdan-lesiv.github.io/omnomnom/python-04.html

class Task:
    def __init__(self, name, best_case, most_likely, worst_case):
        self.name = name
        self.a = best_case
        self.m = most_likely
        self.b = worst_case

    def weighted_estimate(self):
        """Return the estimate calculated by ``Etask = (a + 4m + b) / 6`` formulae."""

    def standard_deviation(self):
        """Return the deviation calculated by ``SDtask = (b − a) / 6`` formulae."""


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def weighted_estimate(self):
        """
        Return a sum of the estimates for all tasks.

        Formulae: ``Eproject = ∑Etask``
        """

    def standard_error(self):
        """
        Return a standard error for the project.

        Formulae: ``SEproject = √∑SEtask²``
        """


class ConfidenceInterval95:
    def __init__(self, project):
        self.project = project

    def max_duration(self):
        """
        Return the max duration of the project.

        Formulae: ``CIproject = Eproject + 2 x SEproject``
        """

    def min_duration(self):
        """
        Return the min duration of the project.

        Formulae: ``CIproject = Eproject - 2 x SEproject``
        """

    def __str__(self):
        return (
            "Project's 95% confidence interval: "
            f"{self.min_duration()} ... {self.max_duration()} points"
        )


if __name__ == "__main__":
    project = Project(input("Project name: "))
    while True:
        project.add_task(
            Task(
                input("Task name                     : "),
                float(input("Best-case estimate in points  : ")),
                float(input("Most-likely estimate in points: ")),
                float(input("Worst-case estimate in points : ")),
            )
        )
        if input("Do you want to add one more task? (y/n) : ").lower() in ("n", "no"):
            break
    print(ConfidenceInterval95(project))