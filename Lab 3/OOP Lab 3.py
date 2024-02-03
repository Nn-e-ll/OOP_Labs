import time


class Command:
    def execute(self):
        pass

    def undo(self):
        pass


class Action1(Command):
    def execute(self):
        print("Выполнено действие 1")

    def undo(self):
        print("Отменено действие 1")


class Action2(Command):
    def execute(self):
        print("Выполнено действие 2")

    def undo(self):
        print("Отменено действие 2")


class Action3(Command):
    def execute(self):
        print("Выполнено действие 3")

    def undo(self):
        print("Отменено действие 3")


class VirtualKeyboard:
    def __init__(self):
        self.actions = {}  # Словарь для хранения назначенных действий
        self.history = []  # Список для отслеживания последних выполненных действий

    def assign_action(self, key, action):
        self.actions[key] = action  # Назначение действия на определенную клавишу
        print(f"Клавиша {key} назначена на действие {action.__class__.__name__}")

    def press_key(self, key):
        if key in self.actions:  # Если клавиша назначена на определенное действие
            action = self.actions[key]  # Получаем соответствующее действие
            action.execute()  # Выполняем действие
            self.history.append(action)  # Добавляем действие в историю
            print(f"Нажата клавиша {key}")

    def undo_last_action(self):
        if self.history:  # Если в истории есть действия
            action = self.history.pop()  # Извлекаем последнее действие
            action.undo()  # Отменяем его выполнение
            print(f"Отменено действие для клавиши {action.__class__.__name__}")
# Пример использования


if __name__ == '__main__':
    keyboard = VirtualKeyboard()

    keyboard.assign_action("F1", Action1())
    keyboard.assign_action("Ctrl+Alt+X", Action2())
    keyboard.assign_action("Shift+Z", Action3())

    keyboard.press_key("F1")  # Выполнено действие 1
    time.sleep(1)  # Задержка в 1 секунду

    keyboard.press_key("Ctrl+Alt+X")  # Выполнено действие 2
    time.sleep(1)  # Задержка в 1 секунду

    keyboard.press_key("Shift+Z")  # Выполнено действие 3
    time.sleep(1)  # Задержка в 1 секунду

    keyboard.undo_last_action()  # Отменено действие 3
    time.sleep(1)  # Задержка в 1 секунду

    keyboard.assign_action("F1", Action3())
    keyboard.assign_action("Ctrl+Alt+X", Action1())

    keyboard.undo_last_action()

    keyboard.press_key("F1")  # Выполнено действие 3
    time.sleep(1)  # Задержка в 1 секунду

    keyboard.press_key("Ctrl+Alt+X")  # Выполнено действие 1
    time.sleep(1)  # Задержка в 1 секунду

    keyboard = VirtualKeyboard()

    keyboard.press_key("F1")  # Выполнено действие 1 (новое переназначение)
    time.sleep(1)  # Задержка в 1 секунду

    keyboard.press_key("Ctrl+Alt+X")  # Выполнено действие 2 (новое переназначение)
    time.sleep(1)  # Задержка в 1 секунду
