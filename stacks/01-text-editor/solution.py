class TextEditor:
    def __init__(self):
        self.text=""
        self.undo=[]
        self.redo=[]
    def write_text(self, text):
        self.undo.append(self.text)
        self.text+=text
        self.redo.clear()
    def undo_action(self):
        if(self.undo):
            self.redo.append(self.text)
            self.text=self.undo.pop()
        else:
            print("Nothing to undo")
    def redo_action(self):
        if(self.redo):
            self.undo.append(self.text)
            self.text=self.redo.pop()
        else:
            print("Nothing to redo")
    def show_text(self):
        print(f"Text: {self.text}")
        
editor = TextEditor()

editor.write_text("Hello")
editor.write_text(" World")
editor.show_text()

editor.undo_action()
editor.show_text()

editor.redo_action()
editor.show_text()
        
