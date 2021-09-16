import os

gui_files = [i.split(".")[0] for i in os.listdir("../gui") if ".py" in i and not "recorder" in i and not "mainwindow" in i]

print("Headers: ")
for fn in gui_files:
    print(f"from {fn} import Ui_Form as {fn}_helper")

# print("Adding windows: ")
# for fn in gui_files:
#     print(f"MainWindow.{fn}_window = QWidget()")
#     print(f"helper = {fn}_helper().setupUi(MainWindow.{fn}_window)")

print("Adding windows: ")
for fn in gui_files:
    print(f"MainWindow.{fn}_window = FormPrototype()")
    print(f"helper = {fn}_helper().setupUi(MainWindow.{fn}_window)")

print("Showing windows: ")
for fn in gui_files:
    print(f"MainWindow.{fn}_window.show()")

print("Assingning DB:")
for fn in gui_files:
    print(f"MainWindow.{fn}_window.db = db")

print("Assigning Config:")
print("======================================")

print("Assigning Date:")
for fn in gui_files:
    print(f"MainWindow.{fn}_window.curr_date = MainWindow.curr_date")
