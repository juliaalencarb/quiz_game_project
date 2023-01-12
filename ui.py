from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UseInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            bg=THEME_COLOR,
            padx=20,
            pady=20)

        self.score_display = Label(
            text=f"Score: {self.quiz.score}",
            bg=THEME_COLOR,
            font=("Arial", 14, "italic"))
        self.score_display.grid(row=0, column=1)

        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white")
        self.text = self.canvas.create_text(
            150,
            125,
            text="Question here",
            width=280,
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=20,
            pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(
            image=true_img,
            highlightthickness=0,
            pady=5,
            padx=50,
            command=self.is_question_true)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(
            image=false_img,
            highlightthickness=0,
            pady=5,
            padx=5,
            command=self.is_question_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text=f"Congratulations, you've finished the quiz.\n         Score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def is_question_true(self):
        self.give_feedback(self.quiz.check_answer("true"))
        # if self.quiz.check_answer("true"):
        #     self.score_display.config(text=f"Score: {self.quiz.score}")
        #     self.get_next_question()
        # else:
        #     self.get_next_question()

    def is_question_false(self):
        self.give_feedback(self.quiz.check_answer("false"))
        # if self.quiz.check_answer("false"):
        #     self.score_display.config(text=f"Score: {self.quiz.score}")
        #     self.get_next_question()
        # else:
        #     self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.score_display.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
