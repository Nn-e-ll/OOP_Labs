from abc import ABC, abstractmethod


class Control(ABC):

    def setPosition(self, x, y):
        print(f"Установка позиции по ({x}, {y})")

    def getPosition(self):
        print("Получение позиции")


# Создание класса-фабрики для генерации контролов
class ControlFactory(ABC):
    @abstractmethod
    def createForm(self):
        pass

    @abstractmethod
    def createLabel(self):
        pass

    @abstractmethod
    def createTextBox(self):
        pass

    @abstractmethod
    def createComboBox(self):
        pass

    @abstractmethod
    def createButton(self):
        pass


class Form(Control):
    @abstractmethod
    def addControl(self, control):
        pass


class Label(Control):
    @abstractmethod
    def setText(self, text):
        pass

    @abstractmethod
    def getText(self):
        pass


class TextBox(Control):
    @abstractmethod
    def setText(self, text):
        pass

    @abstractmethod
    def getText(self):
        pass

    @abstractmethod
    def onValueChanged(self):
        pass


class ComboBox(Control):
    @abstractmethod
    def setSelectedIndex(self, index):
        pass

    @abstractmethod
    def getSelectedIndex(self):
        pass

    @abstractmethod
    def setItems(self, items):
        pass

    @abstractmethod
    def getItems(self):
        pass


class Button(Control):
    @abstractmethod
    def setText(self, text):
        pass

    @abstractmethod
    def getText(self):
        pass

    @abstractmethod
    def click(self):
        pass


# Создание классов контролов для различных операционных систем
class WindowsControlFactory(ControlFactory):
    def createForm(self):
        return WindowsForm()

    def createLabel(self):
        return WindowsLabel()

    def createTextBox(self):
        return WindowsTextBox()

    def createComboBox(self):
        return WindowsComboBox()

    def createButton(self):
        return WindowsButton()


class LinuxControlFactory(ControlFactory):
    def createForm(self):
        return LinuxForm()

    def createLabel(self):
        return LinuxLabel()

    def createTextBox(self):
        return LinuxTextBox()

    def createComboBox(self):
        return LinuxComboBox()

    def createButton(self):
        return LinuxButton()


class MacOSControlFactory(ControlFactory):
    def createForm(self):
        return MacOSForm()

    def createLabel(self):
        return MacOSLabel()

    def createTextBox(self):
        return MacOSTextBox()

    def createComboBox(self):
        return MacOSComboBox()

    def createButton(self):
        return MacOSButton()


# Создание классов контролов для каждой операционной системы
class LinuxForm(Form):
    def addControl(self, control):
        print(f"Добавление контролла Control в форму Linux")


class LinuxLabel(Label):
    def setText(self, text):
        print(f"Установка текста '{text}' для метки Linux")

    def getText(self):
        print("Получение текста из метки Linux")


class LinuxTextBox(TextBox):
    def setText(self, text):
        print(f"Установка текста '{text}' для текстового поля Linux")

    def getText(self):
        print("Получение текста из текстового поля Linux")

    def onValueChanged(self):
        print("Событие OnValueChanged для текстового поля Linux")


class LinuxComboBox(ComboBox):
    def setSelectedIndex(self, index):
        print(f"Установка выбранного индекса {index} для комбинированного поля Linux")

    def getSelectedIndex(self):
        print("Получение выбранного индекса из комбинированного поля Linux")

    def setItems(self, items):
        print(f"Установка элементов {items} для комбинированного поля Linux")

    def getItems(self):
        print("Получение элементов из комбинированного поля Linux")


class LinuxButton(Button):
    def setText(self, text):
        print(f"Установка текста '{text}' для кнопки Linux")

    def getText(self):
        print("Получение текста из кнопки Linux")

    def click(self):
        print("Событие клика для кнопки Linux")


class WindowsForm(Form):
    def addControl(self, control):
        print(f"Добавление контролла Control в форму Windows")


class WindowsLabel(Label):
    def setText(self, text):
        print(f"Установка текста '{text}' для метки Windows")

    def getText(self):
        print("Получение текста из метки Windows")


class WindowsTextBox(TextBox):
    def setText(self, text):
        print(f"Установка текста '{text}' для текстового поля Windows")

    def getText(self):
        print("Получение текста из текстового поля Windows")

    def onValueChanged(self):
        print("Событие OnValueChanged для текстового поля Windows")


class WindowsComboBox(ComboBox):
    def setSelectedIndex(self, index):
        print(f"Установка выбранного индекса {index} для комбинированного поля Windows")

    def getSelectedIndex(self):
        print("Получение выбранного индекса из комбинированного поля Windows")

    def setItems(self, items):
        print(f"Установка элементов {items} для комбинированного поля Windows")

    def getItems(self):
        print("Получение элементов из комбинированного поля Windows")


class WindowsButton(Button):
    def setText(self, text):
        print(f"Установка текста '{text}' для кнопки Windows")

    def getText(self):
        print("Получение текста из кнопки Windows")

    def click(self):
        print("Событие клика для кнопки Windows")


class MacOSForm(Form):
    def addControl(self, control):
        print(f"Добавление контролла Control в форму MacOS")


class MacOSLabel(Label):
    def setText(self, text):
        print(f"Установка текста '{text}' для метки MacOS")

    def getText(self):
        print("Получение текста из метки MacOS")


class MacOSTextBox(TextBox):
    def setText(self, text):
        print(f"Установка текста '{text}' для текстового поля MacOS")

    def getText(self):
        print("Получение текста из текстового поля MacOS")

    def onValueChanged(self):
        print("Событие OnValueChanged для текстового поля MacOS")


class MacOSComboBox(ComboBox):
    def setSelectedIndex(self, index):
        print(f"Установка выбранного индекса {index} для комбинированного поля MacOS")

    def getSelectedIndex(self):
        print("Получение выбранного индекса из комбинированного поля MacOS")

    def setItems(self, items):
        print(f"Установка элементов {items} для комбинированного поля MacOS")

    def getItems(self):
        print("Получение элементов из комбинированного поля MacOS")


class MacOSButton(Button):
    def setText(self, text):
        print(f"Установка текста '{text}' для кнопки MacOS")

    def getText(self):
        print("Получение текста из кнопки MacOS")

    def click(self):
        print("Событие клика для кнопки MacOS")


if __name__ == '__main__':
    # Создание экземпляров контролов для различных операционных систем
    LinuxFactory = LinuxControlFactory()
    LinuxForm = LinuxFactory.createForm()
    LinuxLabel = LinuxFactory.createLabel()
    LinuxTextBox = LinuxFactory.createTextBox()
    LinuxComboBox = LinuxFactory.createComboBox()
    LinuxButton = LinuxFactory.createButton()

    # Симуляция вызова методов контролов
    LinuxForm.setPosition(10, 10)
    LinuxForm.addControl(LinuxLabel)
    LinuxLabel.setText("Пример текста")
    LinuxLabel.getText()
    LinuxTextBox.setPosition(20, 20)
    LinuxTextBox.setText("Введенный текст")
    LinuxTextBox.getText()
    LinuxTextBox.onValueChanged()
    LinuxComboBox.setPosition(30, 30)
    LinuxComboBox.setSelectedIndex(0)
    LinuxComboBox.getSelectedIndex()
    LinuxComboBox.setItems(["Элемент 1", "Элемент 2"])
    LinuxComboBox.getItems()
    LinuxButton.setPosition(40, 40)
    LinuxButton.setText("Нажми меня")
    LinuxButton.getText()
    LinuxButton.click()
