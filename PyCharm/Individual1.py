#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def add_train():
    destination = input("Название пункта назначения: ")
    number = int(input("Номер поезда: "))
    time = input("Время отправления: ")

    train = {
        'destination': destination,
        'number': number,
        'time': time,
        }


def list_trains(trains):
    if trains:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:>4} | {:<10} | {:<10} |'.format(
                "№ поезда",
                "Пункт назначении",
                "Время отпрвления"
            )
        )
        print(line)

        for idx, train in enumerate(trains, 1):
            print(
                '| {:>4} | {:<10} | {:<10} | {:>8} |'.format(
                    idx,
                    train.get('number', 0),
                    train.get('destination', ''),
                    train.get('time', '')
                )
            )
            print(line)
    else:
        print("Список поездов пуст.")


def select_trains(trains, time):


        print(
            "Поезде с номером {:>1} отправляется в город {:>1} в {:>1}".format(
                trains.get('number', ''),
                trains.get('destination', ''),
                trains.get('time', '')
            )
        )


def main():
    trains = []
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            train = add_train()
            trains.append(train)
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('number', ''))

        elif command == 'list':
            list_trains(trains)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            num = int(parts[1])
            result = []
            for train in trains:
                if num == train.get('number', ''):
                    print(select_trains(trains))


        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезда;")
            print("list - вывести список поездов;")
            print("select <номер поезда> запросить информации о поезде с этим номером ")
            print("help - отобразить справку")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()

