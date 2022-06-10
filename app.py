import time
from random import randint, choice

class House:
    def __init__(self):
        self.total_floors = randint(5, 10)
        self.floors = {i+1: Floor(i+1, self.total_floors) for i in range(self.total_floors)}

    def work_elevator(self):
        elevator = Elevator(self.total_floors)
        print("The number of storeys of the house:", self.total_floors)

        while True:
            queue_elevator = self.floors[elevator.current_floor].humans
            elevator.check_way()

            print(f'---- Floor {elevator.current_floor} ------')
            print("The queue for the elevator:", [i.need_floor for i in queue_elevator])

            if elevator.check_output():

                print("Inside the elevator: ", [i.need_floor for i in elevator.elevator_car])

                elevator.unload_people(queue_elevator)

                print("The queue for the elevator now:", [i.need_floor for i in queue_elevator])

                elevator.download_people(queue_elevator)

            elif elevator.check_input(queue_elevator):
                elevator.download_people(queue_elevator)

            print("Inside the elevator: ", [i.need_floor for i in elevator.elevator_car])
            print("The remaining people", [i.need_floor for i in queue_elevator])

            if elevator.button:
                elevator.current_floor += 1
            else:
                elevator.current_floor -= 1

            time.sleep(4)

class Floor:
    def __init__(self, floor, floors):
        self.humans = [Human(floor, floors) for i in range(randint(0, 10))]


class Human:
    def __init__(self, floor, floors):
        self.floor = floor
        self.floors = [i for i in range(1, floors+1) if i != self.floor]
        self.need_floor = choice(self.floors)

    def need_way(self):
        if self.need_floor > self.floor:
            return True
        else:
            return False


class Elevator:
    """
    Buttons:
        Up - True
        Down - False
    """

    def __init__(self, max_floor):
        self.initial_floor = 1
        self.max_floor = max_floor
        self.current_floor = 1
        self.limit = 5
        self.elevator_car = []
        self.button = True

    def check_output(self):
        for human in self.elevator_car:
            if human.need_floor == self.current_floor:
                return True

    def check_input(self, queue_people: list):
        for human in queue_people:
            if len(self.elevator_car) < self.limit and human.need_way() == self.button:
                return True

    def check_way(self):
        if self.current_floor == self.max_floor:
            self.button = False
        elif self.current_floor == self.initial_floor:
            self.button = True

    def unload_people(self, queue_people: list):
        initial_number = len(self.elevator_car)
        people_cameout = [i for i in self.elevator_car if i.need_floor == self.current_floor]
        for human in people_cameout:
            if human.need_floor == self.current_floor:
                self.elevator_car.remove(human)
        people_came_out = initial_number - len(self.elevator_car)
        print(people_came_out, 'people got out of the elevator')
        for i in range(people_came_out):
            queue_people.append(Human(self.current_floor, self.max_floor))
        return queue_people

    def download_people(self, floor: list):
        free_space = self.limit - len(self.elevator_car)
        if free_space and floor:
            queue_people = [i for i in floor if i.need_way() == self.button][:free_space]
            print(len(queue_people), "people went into the elevator")
            self.elevator_car.extend(queue_people)
            for i in queue_people:
                floor.remove(i)
            return floor
        else:
            return floor


if __name__ == '__main__':
    house = House()
    house.work_elevator()